import requests
TOKEN="syt_c2xpdTA3MDI_ANMgoCrBRuWFixRnwoUC_1Gt5pF"
ROOM_ID = "!ZxHimQycFrBWMJyOAZ:matrix.chowchow"
url_base = "http://localhost:8008/_matrix/client/v3/rooms/{}/send/m.room.encrypted/"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

for i in range(10000000):
    url = url_base.format(ROOM_ID, i)
    data = {
        "msgtype": "m.text",
        "body": "Hello from python!"
    }

    r = requests.put(url, headers=headers, json=data)
    print(i, r.status_code)