#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <curl/curl.h>

#define NUM_THREADS 8   // adjust this (4, 8, 16, etc.)

const char *TOKEN = "syt_c2xpdTA3MDI_ANMgoCrBRuWFixRnwoUC_1Gt5pF";
const char *ROOM_ID = "!ZxHimQycFrBWMJyOAZ:matrix.chowchow";

void *worker(void *arg) {
    long tid = (long)arg;

    CURL *curl = curl_easy_init();
    if (!curl) return NULL;

    char auth[1024];
    snprintf(auth, sizeof(auth), "Authorization: Bearer %s", TOKEN);

    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, auth);
    headers = curl_slist_append(headers, "Content-Type: application/json");

    const char *body = "{\"msgtype\":\"m.text\",\"body\":\"Hello\"}";

    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "PUT");
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, body);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, (long)strlen(body));
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL); // discard response

    char url[4096];

    for (long i = 0; ; i++) {
        // unique txnId per thread
        snprintf(url, sizeof(url),
            "http://localhost:8008/_matrix/client/v3/rooms/%s/send/m.room.encrypted/", ROOM_ID);

        curl_easy_setopt(curl, CURLOPT_URL, url);

        // CURLcode res = curl_easy_perform(curl);
        // if (res != CURLE_OK) {
        //     fprintf(stderr, "[T%ld] error: %s\n", tid, curl_easy_strerror(res));
        // }

        // optional light progress signal
        // if (i % 100000 == 0) {
        //     printf("[T%ld] %ld\n", tid, i);
        //     fflush(stdout);
        // }
    }

    curl_slist_free_all(headers);
    curl_easy_cleanup(curl);
    return NULL;
}

int main() {
    curl_global_init(CURL_GLOBAL_ALL);

    pthread_t threads[NUM_THREADS];

    for (long i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL, worker, (void *)i);
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    curl_global_cleanup();
    return 0;
}