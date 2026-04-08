""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

__matrix_client_v3_user__userId__filter_post_filter_id = dependencies.DynamicVariable("__matrix_client_v3_user__userId__filter_post_filter_id")

__matrix_client_v3_room_keys_version_post_version = dependencies.DynamicVariable("__matrix_client_v3_room_keys_version_post_version")

__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id = dependencies.DynamicVariable("__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id")

__matrix_client_v3_rooms__room_id__send_m_reaction__txnId__put_event_id = dependencies.DynamicVariable("__matrix_client_v3_rooms__room_id__send_m_reaction__txnId__put_event_id")

__matrix_client_v3_createRoom_post_room_id = dependencies.DynamicVariable("__matrix_client_v3_createRoom_post_room_id")

__matrix_client_v3_account_whoami_get_user_id = dependencies.DynamicVariable("__matrix_client_v3_account_whoami_get_user_id")

__matrix_client_v3_sync_get_next_batch = dependencies.DynamicVariable("__matrix_client_v3_sync_get_next_batch")

__ordering_____matrix_client_v3_rooms__room_id__leave_forget = dependencies.DynamicVariable("__ordering_____matrix_client_v3_rooms__room_id__leave_forget")

def parse__matrixclientv3useruserIdfilterpost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["filter_id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("__matrix_client_v3_user__userId__filter_post_filter_id", temp_7262)


def parse__matrixclientv3room_keysversionpost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8173 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_8173 = str(data["version"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("__matrix_client_v3_room_keys_version_post_version", temp_8173)


def parse__matrixclientv3roomsroom_idsendmroommessagetxnIdput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7680 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7680 = str(data["event_id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id", temp_7680)


def parse__matrixclientv3roomsroom_idsendmreactiontxnIdput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5581 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5581 = str(data["event_id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5581:
        dependencies.set_variable("__matrix_client_v3_rooms__room_id__send_m_reaction__txnId__put_event_id", temp_5581)


def parse__matrixclientv3createRoompost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2060 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_2060 = str(data["room_id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2060:
        dependencies.set_variable("__matrix_client_v3_createRoom_post_room_id", temp_2060)


def parse__matrixclientv3accountwhoamiget(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5588 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5588 = str(data["user_id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5588):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5588:
        dependencies.set_variable("__matrix_client_v3_account_whoami_get_user_id", temp_5588)


def parse__matrixclientv3syncget(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9060 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9060 = str(data["next_batch"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9060:
        dependencies.set_variable("__matrix_client_v3_sync_get_next_batch", temp_9060)

req_collection = requests.RequestCollection([])
# Endpoint: /_matrix/client/v3/rooms/{room_id}/redact/{event_id_msg}/{txnId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("redact"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("txnId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{room_id}/redact/{event_id_msg}/{txnId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{room_id}/redact/{event_id_reaction}/{txnId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("redact"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_reaction__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("txnId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{room_id}/redact/{event_id_reaction}/{txnId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/profile/{userId}/{keyName}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload("keyName", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/profile/{userId}/{keyName}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/profile/{userId}/{keyName}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload("keyName", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/profile/{userId}/{keyName}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/profile/{userId}/{keyName}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload("keyName", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"displayname\":\"Alice Wonderland\"}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/profile/{userId}/{keyName}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/account_data/{type}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account_data"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["org.example.custom.config"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/account_data/{type}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/account_data/{type}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account_data"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("type", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"recent_rooms\":[\"!CSdCumndWvWcUBPJvj:localhost\",\"!RHUwAtcdMzPzNemmEW:localhost\",\"!vwxwawZCvobyHxBrSi:localhost\"]}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/account_data/{type}"
)
req_collection.add_request(request)

# Endpoint: /.well-known/matrix/client, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(".well-known"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/.well-known/matrix/client"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/receipt/{receiptType}/{eventId}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("receipt"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["m.read"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "thread_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["main"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/receipt/{receiptType}/{eventId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/filter, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("filter"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "room":
        {
            "state":
                {
                    "lazy_load_members":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("""
                }
            ,
            "timeline":
                {
                    "unread_thread_notifications":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("""
                }
        }
    }"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse__matrixclientv3useruserIdfilterpost,
            'dependencies':
            [
                __matrix_client_v3_user__userId__filter_post_filter_id.writer()
            ]
        }

    },

],
requestId="/_matrix/client/v3/user/{userId}/filter"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/messages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["s24_3_6_13_19_1_1_10_0_1_2_1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dir="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["b"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["50"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["""{\"lazy_load_members\":true}"""]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/messages"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/typing/{userId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("typing"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "typing":"""),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/typing/{userId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/version, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("version"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/version"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/version, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("version"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "algorithm":"""),
    primitives.restler_fuzzable_group("algorithm", ['m.megolm_backup.v1.curve25519-aes-sha2']  ,quoted=True, examples=["m.megolm_backup.v1.curve25519-aes-sha2"]),
    primitives.restler_static_string(""",
    "auth_data":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"public_key\":\"JpgORSZpbMfmXUpoJ+D60IKs7yTE99kUkKhx/htCuyc\",\"signatures\":{\"@admin:localhost\":{\"ed25519:GXPVQLSNGE\":\"97adbiIEdvxd7nRg0J+Ddq8eE6BJgWD53iBIMoxGRhgyJqKdovdGX3AzbLl5UCnnJXsKkKEG79uSjRcY3HkjAQ\",\"ed25519:ZXtjuPWSwVp5tCUUxIPcPZBvI+vSB9/93nRkWRpU4TA\":\"j3VPaKhfAG6Y5og3Oqne/SJcerVx1+eiFPd73aMNQVHcK8UbQA2WVnOVfpnsE54z+BNN5XJ62ncFW1et60ZBCA\"}}}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse__matrixclientv3room_keysversionpost,
            'dependencies':
            [
                __matrix_client_v3_room_keys_version_post_version.writer()
            ]
        }

    },

],
requestId="/_matrix/client/v3/room_keys/version"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["s26_3_6_13_19_1_1_10_0_1_2_1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("membership="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["join"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("not_membership="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["leave"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/members"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/keys/upload, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("upload"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "device_keys":
        {
            "algorithms":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["m.olm.v1.curve25519-aes-sha2"]),
    primitives.restler_static_string(""",
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["m.megolm.v1.aes-sha2"]),
    primitives.restler_static_string("""
            ],
            "device_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GXPVQLSNGE"]),
    primitives.restler_static_string(""",
            "keys":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"curve25519:GXPVQLSNGE\":\"ownpE9+W30Rsl2u+vEQJzvTEZWMoUTXVLQ9bNpuavGI\",\"ed25519:GXPVQLSNGE\":\"KuA8WSX6WxBNZhAn++scFqtNX3y0KPvsdMkgw/ZRvfM\"}"]),
    primitives.restler_static_string(""",
            "signatures":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"@admin:localhost\":{\"ed25519:GXPVQLSNGE\":\"QpNs04ij2Oe8hSzvd2/deiSNFTygNKr6isMhVj5/BvutB2mUzsVxM7kaKarBtxqHMJ4aTCKCFwL4ZnvZsCSMAw\"}}"]),
    primitives.restler_static_string(""",
            "user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@admin:localhost"]),
    primitives.restler_static_string("""
        }
    ,
    "fallback_keys":
        {
        }
    ,
    "one_time_keys":
        {
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/keys/upload"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/profile/{userId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/profile/{userId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/thirdparty/protocols, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("thirdparty"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("protocols"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/thirdparty/protocols"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/invite, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("invite"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/invite"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{room_id}/leave, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("leave"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            
            'dependencies':
            [
                __ordering_____matrix_client_v3_rooms__room_id__leave_forget.writer()
            ]
        }

    },

],
requestId="/_matrix/client/v3/rooms/{room_id}/leave"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/read_markers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("read_markers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/read_markers"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user_directory/search, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user_directory"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "search_term":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@user1:localhost"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user_directory/search"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/keys/query, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("query"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "device_keys":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"@admin:localhost\":[]}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/keys/query"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{room_id}/send/m.room.message/{txnId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("send"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("m.room.message"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("txnId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "body":"""),
    primitives.restler_custom_payload("body", quoted=True),
    primitives.restler_static_string(""",
    "msgtype":"""),
    primitives.restler_fuzzable_group("msgtype", ['m.text']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse__matrixclientv3roomsroom_idsendmroommessagetxnIdput,
            'dependencies':
            [
                __matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.writer()
            ]
        }

    },

],
requestId="/_matrix/client/v3/rooms/{room_id}/send/m.room.message/{txnId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{room_id}/send/m.reaction/{txnId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("send"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("m.reaction"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("txnId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "m.relates_to":
        {
            "event_id":"""),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.reader(), quoted=True),
    primitives.restler_static_string(""",
            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "rel_type":"""),
    primitives.restler_fuzzable_group("rel_type", ['m.annotation']  ,quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse__matrixclientv3roomsroom_idsendmreactiontxnIdput,
            'dependencies':
            [
                __matrix_client_v3_rooms__room_id__send_m_reaction__txnId__put_event_id.writer()
            ]
        }

    },

],
requestId="/_matrix/client/v3/rooms/{room_id}/send/m.reaction/{txnId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/send/{eventType}/{txnId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("send"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["m.reaction"]),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("txnId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"m.relates_to\":{\"rel_type\":\"m.annotation\",\"event_id\":\"$wX2IfGLEUAi92fdyK3A69EH_sNxkGEzWdkCVG6Tibt4\",\"key\":\"😑\"}}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/send/{eventType}/{txnId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/voip/turnServer, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("voip"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("turnServer"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/voip/turnServer"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_static_string(__matrix_client_v3_room_keys_version_post_version.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "rooms":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"!RHUwAtcdMzPzNemmEW:localhost\":{\"sessions\":{\"oRBQ46sOMFHUOjV9qaVHzjXEbnUXy02fb0vYcqQLn4k\":{\"first_message_index\":0,\"forwarded_count\":0,\"is_verified\":false,\"session_data\":{\"ciphertext\":\"R76D98N4Mez1nvRKrTCcdKJTVXkU2iMPvTsVi5m+SElmAwEAo6njHjfPOIj1pC9R0m45Ib302cNLo666h9C+EZYPzsdUWUVqdug0zzlAMAGfpfBfC/3P5PPOYGznAGa05xuPDP4JABxGRQGjK5u/lfYecnwvvuBWcdgUREElJUbrnHGWQ34E95CguXbTSdWL38STNhhWlFdE+n2HB2FMoun+mDMtHBiTOydFNJxX/kE/D/mNMlOHSXD49AE7s2LpG5rF7Br+nRs2tYIaYEKH6A5Pffubw6s7Vtf+xZTsYJenp9S45xOEIeQPa68xl3D9UkNsOuUTc5GOPIZ/ztZD88hNB4XuHgBL7uy2VaCzfYY6MmG7H7ItbRaOWQez4SS/y/dbBZY8KPwdaoN8OZTVY9JkY4uNmtQnr49n2W4/uL4AC2J3P25r4EoGf/WM/q8Cq2NPJp3wm+jCmE8nU24bdk0WvIEkNV0+hz+mkNlz27DiiQcTNze+Nr9rtRJuS6NqUsD3DCoelFtxOghZ8DYenHF0oaYTcDNFW8Fd3s0peotT1OmVE6k7DiSphtxJXyW32Pwf+rm5tMCcDiP16qnGQYB2MltjgKRYaGtEWuCDSuhhSYPsrHlmM/bCJTtMm2X68Zqbz1Bb3alrZva1I/nPrQ\",\"ephemeral\":\"XfuM2sJ7Pfs2YpUqX+oMg6WXg7Eawr8obocTNNB5z1s\",\"mac\":\"SM9y+v0YhQU\"}}}},\"!vwxwawZCvobyHxBrSi:localhost\":{\"sessions\":{\"9ZbPs3ZlGNL4Z/TN4sbOcxSw9cY7h8BmfF2HsSpexCQ\":{\"first_message_index\":0,\"forwarded_count\":0,\"is_verified\":false,\"session_data\":{\"ciphertext\":\"Z2ISIsnbY7RoZOw+9dxAd9rRQP5gaxwWsdTANawL/IYk3k8EtCldw3pWnlgbxIUUxmr8VnNcPOmhjCkgU/xCq0suLdhsIeDunYLqPgDGPj5veqouJL//wzgPnWsFLdJF4J+GbED8HACP4qF4cCbC09Ayu4f97H7+lNXHXL+8nT4tnHbDxyC5V4xkzEcFzPXC6M+mTQkk/UKZZRT/QgKdBi4r9L7BetUrPQjhE3z5YSpXBDyH+bnomlmJkc3FAHqqX5VHJ+wlJ/1vj42G5msMUXtJT1gJeKw1dkTPFofF09YxCd7eLsOQaztpq1utbALQEVC9QbDLRy/ydZTYAgiU9029v4DEx4IGT120bPmQJ00/xkN3lmDe4c4eptdYoFfJZAvku7zIMcF7nR2NI+mSAi9rSgviKuuB7C6JXVL+HfAXbuGapCaNn2+uT+EjEee7JlHN5oxGhTSKG9Epa8bq3N83RAKSTe34qrWPK+IXwHlPIZKNpJwnEBLL4nJfbZJn1OkUnxsWb/tbAZpkvoiXrJbJYu2how2I6drPS9oPSlDt4haC9cPUrWvLFH1W1QVFrdJCS5Cz8SWyckuy/j2c8KQruzCcb0iZfxFr8P7oZEEtdszV1+abxN+JmJaWn8U6YyHCivmGZAxKzuDPPuDYzw\",\"ephemeral\":\"ehSonqikdKfArv98XrKrKi2vwRvPXw9TtGLEKSaUmgQ\",\"mac\":\"CdNl+H40n1w\"}}}}}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/capabilities, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("capabilities"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/capabilities"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/createRoom, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("createRoom"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_custom_payload("name", quoted=True),
    primitives.restler_static_string(""",
    "preset":"""),
    primitives.restler_fuzzable_group("preset", ['private_chat','public_chat','trusted_private_chat']  ,quoted=True),
    primitives.restler_static_string(""",
    "room_alias_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "topic":"""),
    primitives.restler_custom_payload("topic", quoted=True),
    primitives.restler_static_string(""",
    "visibility":"""),
    primitives.restler_fuzzable_group("visibility", ['public','private']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse__matrixclientv3createRoompost,
            'dependencies':
            [
                __matrix_client_v3_createRoom_post_room_id.writer()
            ]
        }

    },

],
requestId="/_matrix/client/v3/createRoom"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushrules, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushrules"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushrules"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/keys/signatures/upload, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("signatures"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("upload"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"@admin:localhost\":{\"GXPVQLSNGE\":{\"user_id\":\"@admin:localhost\",\"device_id\":\"GXPVQLSNGE\",\"algorithms\":[\"m.olm.v1.curve25519-aes-sha2\",\"m.megolm.v1.aes-sha2\"],\"keys\":{\"curve25519:GXPVQLSNGE\":\"ownpE9+W30Rsl2u+vEQJzvTEZWMoUTXVLQ9bNpuavGI\",\"ed25519:GXPVQLSNGE\":\"KuA8WSX6WxBNZhAn++scFqtNX3y0KPvsdMkgw/ZRvfM\"},\"signatures\":{\"@admin:localhost\":{\"ed25519:6BTihlh179CLeWGPlKdIzifr1HvwjrvdzOynKkhxt18\":\"HdtlOBc1ZymjIBxeeDKAzuxqORk/FpYdbLbAgjc52+2oVY7cjJ++UzymfmszSWZfmNiRFFvHfhU8ehzN2ItrAQ\"}}}}}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/keys/signatures/upload"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/versions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("versions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/versions"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/keys/device_signing/upload, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("device_signing"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("upload"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "master_key":
        {
            "keys":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"ed25519:ZXtjuPWSwVp5tCUUxIPcPZBvI+vSB9/93nRkWRpU4TA\":\"ZXtjuPWSwVp5tCUUxIPcPZBvI+vSB9/93nRkWRpU4TA\"}"]),
    primitives.restler_static_string(""",
            "signatures":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"@admin:localhost\":{\"ed25519:GXPVQLSNGE\":\"kNwA8MI1p5xaz0oZZb8dp1r0Dc1oTLOJlJLPMjyRN7IsfjqlmzzNPxhnF1r9XDXXn9Vi2x1yr2PRR6OLY5uMAQ\",\"ed25519:ZXtjuPWSwVp5tCUUxIPcPZBvI+vSB9/93nRkWRpU4TA\":\"t0+7WPj1/TbepzKcVlncA8fz6A3aWVziPt6OBoWGDrJgobrOdZ4VHU6Xs8kaRiTnWsK71jo/W/xcXGyWy+JSCg\"}}"]),
    primitives.restler_static_string(""",
            "usage":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["master"]),
    primitives.restler_static_string("""
            ],
            "user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@admin:localhost"]),
    primitives.restler_static_string("""
        }
    ,
    "self_signing_key":
        {
            "keys":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"ed25519:6BTihlh179CLeWGPlKdIzifr1HvwjrvdzOynKkhxt18\":\"6BTihlh179CLeWGPlKdIzifr1HvwjrvdzOynKkhxt18\"}"]),
    primitives.restler_static_string(""",
            "signatures":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"@admin:localhost\":{\"ed25519:ZXtjuPWSwVp5tCUUxIPcPZBvI+vSB9/93nRkWRpU4TA\":\"dIGTe1GfFDoZ2P0v1DdBHI3Sd1exc4ki8cLa2AOMMWT1pRSeeAGz3kjkDLFziBDs7fr7avQIOaZDKIMOWK0UAQ\"}}"]),
    primitives.restler_static_string(""",
            "usage":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["self_signing"]),
    primitives.restler_static_string("""
            ],
            "user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@admin:localhost"]),
    primitives.restler_static_string("""
        }
    ,
    "user_signing_key":
        {
            "keys":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"ed25519:OZtrFAGfNTA0GKRwVVuW50FGSqZ7+oubLfZEzUfqCdM\":\"OZtrFAGfNTA0GKRwVVuW50FGSqZ7+oubLfZEzUfqCdM\"}"]),
    primitives.restler_static_string(""",
            "signatures":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"@admin:localhost\":{\"ed25519:ZXtjuPWSwVp5tCUUxIPcPZBvI+vSB9/93nRkWRpU4TA\":\"5R8B3C5Z5y9Ek2Lkih1v6TSRlIng8QFZeb1zCGdw6rJ66qvKbnZOag8ItP3h06Jc1l9RM8mM+y76PPwgz8zACw\"}}"]),
    primitives.restler_static_string(""",
            "usage":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["user_signing"]),
    primitives.restler_static_string("""
            ],
            "user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@admin:localhost"]),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/keys/device_signing/upload"
)
req_collection.add_request(request)

# Endpoint: /.well-known/matrix/support, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(".well-known"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("support"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/.well-known/matrix/support"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/appservice/{appserviceId}/ping, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("appservice"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["telegram"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ping"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "transaction_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["mautrix-go_1683636478256400935_123"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/appservice/{appserviceId}/ping"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/auth_metadata, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth_metadata"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/auth_metadata"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/media/config, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("config"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/media/config"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/media/download/matrix.leap04/{mediaId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("download"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matrix.leap04"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ascERGshawAWawugaAcauga"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("timeout_ms="),
    primitives.restler_custom_payload("timeout_ms", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/media/download/matrix.leap04/{mediaId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/media/download/matrix.leap04/{mediaId}/{fileName}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("download"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matrix.leap04"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ascERGshawAWawugaAcauga"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["filename.jpg"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("timeout_ms="),
    primitives.restler_custom_payload("timeout_ms", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/media/download/matrix.leap04/{mediaId}/{fileName}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/media/preview_url, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("preview_url"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("url="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["https://matrix.org"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ts="),
    primitives.restler_fuzzable_int("1", examples=["1510610716656"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/media/preview_url"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/media/thumbnail/matrix.leap04/{mediaId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("thumbnail"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matrix.leap04"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ascERGshawAWawugaAcauga"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("width="),
    primitives.restler_fuzzable_int("1", examples=["64"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height="),
    primitives.restler_fuzzable_int("1", examples=["64"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("method="),
    primitives.restler_custom_payload("method", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeout_ms="),
    primitives.restler_custom_payload("timeout_ms", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("animated="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/media/thumbnail/matrix.leap04/{mediaId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/room_summary/{roomIdOrAlias}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_summary"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["matrix.org"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["elsewhere.ca"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/room_summary/{roomIdOrAlias}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/hierarchy, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hierarchy"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("suggested_only="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("max_depth="),
    primitives.restler_fuzzable_int("1", examples=["5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["next_batch_token"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/hierarchy"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{room_id}/relations/{event_id_msg}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("relations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{room_id}/relations/{event_id_msg}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/relations/{eventId}/{relType}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("relations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["org.example.my_relation"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page2_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page3_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dir="),
    primitives.restler_fuzzable_group("dir", ['b','f']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("recurse="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/relations/{eventId}/{relType}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/relations/{eventId}/{relType}/{eventType}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("relations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["org.example.my_relation"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["m.room.message"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page2_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page3_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dir="),
    primitives.restler_fuzzable_group("dir", ['b','f']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("recurse="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/relations/{eventId}/{relType}/{eventType}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/threads, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("threads"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("include="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["all"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["next_batch_token"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/threads"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/timestamp_to_event, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timestamp_to_event"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ts="),
    primitives.restler_fuzzable_int("1", examples=["1432684800000"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dir="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["f"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/timestamp_to_event"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/3pid, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("3pid"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/3pid"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/3pid, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("3pid"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "three_pid_creds":
        {
            "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["d0nt-T3ll"]),
    primitives.restler_static_string(""",
            "id_access_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["abc123_OpaqueString"]),
    primitives.restler_static_string(""",
            "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["matrix.org"]),
    primitives.restler_static_string(""",
            "sid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["abc123987"]),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/3pid"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/3pid/add, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("3pid"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("add"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auth":
        {
            "session":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["xxxxx"]),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.type.foo"]),
    primitives.restler_static_string("""
        }
    ,
    "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["d0nt-T3ll"]),
    primitives.restler_static_string(""",
    "sid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["abc123987"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/3pid/add"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/3pid/bind, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("3pid"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("bind"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["d0nt-T3ll"]),
    primitives.restler_static_string(""",
    "id_access_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["abc123_OpaqueString"]),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.org"]),
    primitives.restler_static_string(""",
    "sid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["abc123987"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/3pid/bind"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/3pid/delete, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("3pid"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example@example.org"]),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.org"]),
    primitives.restler_static_string(""",
    "medium":"""),
    primitives.restler_fuzzable_group("medium", ['email','msisdn']  ,quoted=True, examples=["email"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/3pid/delete"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/3pid/email/requestToken, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("3pid"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("email"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requestToken"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["monkeys_are_GREAT"]),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["alice@example.org"]),
    primitives.restler_static_string(""",
    "next_link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://example.org/congratulations.html"]),
    primitives.restler_static_string(""",
    "send_attempt":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "id_access_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["id.example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/3pid/email/requestToken"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/3pid/msisdn/requestToken, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("3pid"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("msisdn"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requestToken"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["monkeys_are_GREAT"]),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GB"]),
    primitives.restler_static_string(""",
    "next_link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://example.org/congratulations.html"]),
    primitives.restler_static_string(""",
    "phone_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["07700900001"]),
    primitives.restler_static_string(""",
    "send_attempt":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "id_access_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["id.example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/3pid/msisdn/requestToken"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/3pid/unbind, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("3pid"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unbind"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example@example.org"]),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.org"]),
    primitives.restler_static_string(""",
    "medium":"""),
    primitives.restler_fuzzable_group("medium", ['email','msisdn']  ,quoted=True, examples=["email"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/3pid/unbind"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/deactivate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deactivate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auth":
        {
            "session":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["xxxxx"]),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.type.foo"]),
    primitives.restler_static_string("""
        }
    ,
    "erase":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.org"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/deactivate"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/password, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("password"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auth":
        {
            "session":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["xxxxx"]),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.type.foo"]),
    primitives.restler_static_string("""
        }
    ,
    "logout_devices":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
    "new_password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["ihatebananas"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/password"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/password/email/requestToken, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("password"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("email"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requestToken"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["monkeys_are_GREAT"]),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["alice@example.org"]),
    primitives.restler_static_string(""",
    "next_link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://example.org/congratulations.html"]),
    primitives.restler_static_string(""",
    "send_attempt":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "id_access_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["id.example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/password/email/requestToken"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/password/msisdn/requestToken, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("password"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("msisdn"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requestToken"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["monkeys_are_GREAT"]),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GB"]),
    primitives.restler_static_string(""",
    "next_link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://example.org/congratulations.html"]),
    primitives.restler_static_string(""",
    "phone_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["07700900001"]),
    primitives.restler_static_string(""",
    "send_attempt":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "id_access_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["id.example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/account/password/msisdn/requestToken"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/account/whoami, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("whoami"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse__matrixclientv3accountwhoamiget,
            'dependencies':
            [
                __matrix_client_v3_account_whoami_get_user_id.writer()
            ]
        }

    },

],
requestId="/_matrix/client/v3/account/whoami"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/admin/whois/{userId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("whois"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/admin/whois/{userId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/delete_devices, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete_devices"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auth":
        {
            "session":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["xxxxx"]),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.type.foo"]),
    primitives.restler_static_string("""
        }
    ,
    "devices":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["QBUAZIFURK"]),
    primitives.restler_static_string(""",
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["AUIECTSRND"]),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/delete_devices"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/devices, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/devices"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/devices/{deviceId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["QBUAZIFURK"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auth":
        {
            "session":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["xxxxx"]),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.type.foo"]),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/devices/{deviceId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/devices/{deviceId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["QBUAZIFURK"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/devices/{deviceId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/devices/{deviceId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("deviceId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["My other phone"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/devices/{deviceId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/directory/list/appservice/{networkId}/{roomId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("directory"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("appservice"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["irc"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "visibility":"""),
    primitives.restler_fuzzable_group("visibility", ['public','private']  ,quoted=True, examples=["public"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/directory/list/appservice/{networkId}/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/directory/list/room/{roomId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("directory"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/directory/list/room/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/directory/list/room/{roomId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("directory"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "visibility":"""),
    primitives.restler_fuzzable_group("visibility", ['private','public']  ,quoted=True, examples=["public"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/directory/list/room/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/events/{event_id_msg}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/events/{event_id_msg}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/events/{event_id_reaction}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_reaction__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/events/{event_id_reaction}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/join/{roomId}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("join"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("{roomId}"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["matrix.org"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["elsewhere.ca"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string(""",
    "third_party_signed":
        {
            "mxid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@bob:example.org"]),
    primitives.restler_static_string(""",
            "sender":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@alice:example.org"]),
    primitives.restler_static_string(""",
            "signatures":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"example.org\":{\"ed25519:0\":\"some9signature\"}}"]),
    primitives.restler_static_string(""",
            "token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["random8nonce"]),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/join/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/join/{roomAlias}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("join"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("{roomAlias}"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["matrix.org"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["elsewhere.ca"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string(""",
    "third_party_signed":
        {
            "mxid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@bob:example.org"]),
    primitives.restler_static_string(""",
            "sender":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@alice:example.org"]),
    primitives.restler_static_string(""",
            "signatures":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"example.org\":{\"ed25519:0\":\"some9signature\"}}"]),
    primitives.restler_static_string(""",
            "token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["random8nonce"]),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/join/{roomAlias}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/joined_rooms, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("joined_rooms"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/joined_rooms"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/keys/changes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("changes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_static_string(__matrix_client_v3_sync_get_next_batch.reader(), quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["s75689_5632_2435"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/keys/changes"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/keys/claim, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("claim"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "one_time_keys":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"@alice:example.com\":{\"JLAFKJWSCS\":\"signed_curve25519\"}}"]),
    primitives.restler_static_string(""",
    "timeout":"""),
    primitives.restler_custom_payload("timeout", quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/keys/claim"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/knock/{roomId}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("knock"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("{roomId}"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["matrix.org"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["elsewhere.ca"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/knock/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/knock/{roomAlias}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("knock"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("{roomAlias}"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["matrix.org"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["elsewhere.ca"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/knock/{roomAlias}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/notifications, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["xxxxx"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("only="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["highlight"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/notifications"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/presence/{userId}/status, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presence"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/presence/{userId}/status"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/presence/{userId}/status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presence"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "presence":"""),
    primitives.restler_fuzzable_group("presence", ['online','offline','unavailable']  ,quoted=True, examples=["online"]),
    primitives.restler_static_string(""",
    "status_msg":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["I am here."]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/presence/{userId}/status"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/publicRooms, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("publicRooms"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("server="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/publicRooms"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/publicRooms, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("publicRooms"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("server="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "filter":
        {
            "generic_search_term":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["foo"]),
    primitives.restler_static_string(""",
            "room_types":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=[None]),
    primitives.restler_static_string(""",
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["m.space"]),
    primitives.restler_static_string("""
            ]
        }
    ,
    "include_all_networks":"""),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(""",
    "limit":"""),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string(""",
    "third_party_instance_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["irc-freenode"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/publicRooms"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushers"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushers/set, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("set"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "app_display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Mat Rix"]),
    primitives.restler_static_string(""",
    "app_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["com.example.app.ios"]),
    primitives.restler_static_string(""",
    "append":"""),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(""",
    "data":
        {
            "format":"""),
    primitives.restler_fuzzable_group("format", ['event_id_only']  ,quoted=True, examples=["event_id_only"]),
    primitives.restler_static_string(""",
            "url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://push-gateway.location.here/_matrix/push/v1/notify"]),
    primitives.restler_static_string("""
        }
    ,
    "device_display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["iPhone 9"]),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["http"]),
    primitives.restler_static_string(""",
    "lang":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["en"]),
    primitives.restler_static_string(""",
    "profile_tag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["xxyyzz"]),
    primitives.restler_static_string(""",
    "pushkey":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["APA91bHPRgkF3JUikC4ENAHEeMrd41Zxv3hVZjC9KtT8OvPVGJ-hQMRKRrZuJAEcl7B338qju59zJMjw2DELjzEvxwYv7hH5Ynpc1ODQ0aT4U4OFEeco8ohsN5PjL1iC2dNtk2BAokeMCg2ZXKqpc8FXKmhX94kIxQ"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushers/set"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushrules/global, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushrules"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("global"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushrules/global"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushrules/global/{kind}/{ruleId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushrules"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("global"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["content"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["nocake"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushrules/global/{kind}/{ruleId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushrules/global/{kind}/{ruleId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushrules"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("global"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["content"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["nocake"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushrules/global/{kind}/{ruleId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushrules/global/{kind}/{ruleId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushrules"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("global"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["content"]),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("ruleId", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["someRuleId"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("after="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["anotherRuleId"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "actions":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["notify"]),
    primitives.restler_static_string("""
    ],
    "pattern":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["cake*lie"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushrules/global/{kind}/{ruleId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushrules/global/{kind}/{ruleId}/actions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushrules"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("global"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["content"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["nocake"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("actions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushrules/global/{kind}/{ruleId}/actions"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushrules/global/{kind}/{ruleId}/actions, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushrules"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("global"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["room"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["#spam:example.com"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("actions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "actions":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["{\"set_tweak\":\"highlight\"}"]),
    primitives.restler_static_string(""",
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["notify"]),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushrules/global/{kind}/{ruleId}/actions"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushrules/global/{kind}/{ruleId}/enabled, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushrules"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("global"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["content"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["nocake"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enabled"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushrules/global/{kind}/{ruleId}/enabled"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/pushrules/global/{kind}/{ruleId}/enabled, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushrules"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("global"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["content"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["nocake"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enabled"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "enabled":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/pushrules/global/{kind}/{ruleId}/enabled"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/refresh, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("refresh"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "refresh_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["some_token"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/refresh"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/register, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("register"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("kind="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["user"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auth":
        {
            "session":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["xxxxx"]),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["example.type.foo"]),
    primitives.restler_static_string("""
        }
    ,
    "device_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GHTYAJCE"]),
    primitives.restler_static_string(""",
    "inhibit_login":"""),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(""",
    "initial_device_display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Jungle Phone"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["ilovebananas"]),
    primitives.restler_static_string(""",
    "refresh_token":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["cheeky_monkey"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/register"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/register/available, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("register"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("available"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("username="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["my_cool_localpart"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/register/available"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/register/email/requestToken, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("register"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("email"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requestToken"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["monkeys_are_GREAT"]),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["alice@example.org"]),
    primitives.restler_static_string(""",
    "next_link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://example.org/congratulations.html"]),
    primitives.restler_static_string(""",
    "send_attempt":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "id_access_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["id.example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/register/email/requestToken"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/register/msisdn/requestToken, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("register"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("msisdn"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requestToken"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["monkeys_are_GREAT"]),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GB"]),
    primitives.restler_static_string(""",
    "next_link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://example.org/congratulations.html"]),
    primitives.restler_static_string(""",
    "phone_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["07700900001"]),
    primitives.restler_static_string(""",
    "send_attempt":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "id_access_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["id.example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/register/msisdn/requestToken"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("roomId", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "sessions":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"sessionid1\":{\"first_message_index\":1,\"forwarded_count\":0,\"is_verified\":true,\"session_data\":{\"ciphertext\":\"base64+ciphertext+of+JSON+data\",\"ephemeral\":\"base64+ephemeral+key\",\"mac\":\"base64+mac+of+ciphertext\"}}}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["sessionid"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["sessionid"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("sessionId", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "first_message_index":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "forwarded_count":"""),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string(""",
    "is_verified":"""),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(""",
    "session_data":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"ciphertext\":\"base64+ciphertext+of+JSON+data\",\"ephemeral\":\"base64+ephemeral+key\",\"mac\":\"base64+mac+of+ciphertext\"}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/version/{version}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("version"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_room_keys_version_post_version.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/version/{version}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/version/{version}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("version"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_room_keys_version_post_version.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/version/{version}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/version/{version}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("version"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_room_keys_version_post_version.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "algorithm":"""),
    primitives.restler_fuzzable_group("algorithm", ['m.megolm_backup.v1.curve25519-aes-sha2']  ,quoted=True, examples=["m.megolm_backup.v1.curve25519-aes-sha2"]),
    primitives.restler_static_string(""",
    "auth_data":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"public_key\":\"abcdefg\",\"signatures\":{\"@alice:example.org\":{\"ed25519:deviceid\":\"signature\"}}}"]),
    primitives.restler_static_string(""",
    "version":"""),
    primitives.restler_static_string(__matrix_client_v3_room_keys_version_post_version.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/version/{version}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/aliases, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("aliases"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/aliases"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/ban, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ban"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string(""",
    "user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@cheeky_monkey:matrix.org"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/ban"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/context/{eventId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("context"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["3"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["66696p746572"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/context/{eventId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/event/{eventId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["$asfDuShaf7Gafaw:matrix.org"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/event/{eventId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{room_id}/forget, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forget"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'pre_send':
        {
            'dependencies':
            [
                __ordering_____matrix_client_v3_rooms__room_id__leave_forget.reader()
            ]
        }

    },

],
requestId="/_matrix/client/v3/rooms/{room_id}/forget"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/initialSync, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!636q39766251:example.com"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("initialSync"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/initialSync"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/invite , method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!d41d8cd:matrix.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("invite "),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string(""",
    "user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@cheeky_monkey:matrix.org"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/invite "
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{room_id}/join, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("join"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{room_id}/join"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/joined_members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!636q39766251:example.com"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("joined_members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/joined_members"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/kick, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!e42d8c:matrix.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("kick"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string(""",
    "user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@cheeky_monkey:matrix.org"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/kick"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/report, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!637q39766251:example.com"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/report"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/report/{eventId}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_rooms__room_id__send_m_room_message__txnId__put_event_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string(""",
    "score":"""),
    primitives.restler_fuzzable_int("1", examples=["-100"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/report/{eventId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/state, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("state"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/state"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/state/{eventType}/{stateKey}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("state"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["m.room.name"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=[""]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["event"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/state/{eventType}/{stateKey}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/state/{eventType}/{stateKey}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!636q39766251:example.com"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("state"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["m.room.member"]),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("stateKey", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"avatar_url\":\"mxc://localhost/SEsfnsuifSDFSSEF\",\"displayname\":\"Alice Margatroid\",\"membership\":\"join\"}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/state/{eventType}/{stateKey}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/unban, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unban"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string(""",
    "user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["@cheeky_monkey:matrix.org"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/unban"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/{roomId}/upgrade, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("upgrade"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "new_version":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["2"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{roomId}/upgrade"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/search, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("next_batch="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["YWxsCgpOb25lLDM1ODcwOA"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "search_categories":
        {
            "room_events":
                {
                    "groupings":
                        {
                            "group_by":
                            [
                                {
                                    "key":"""),
    primitives.restler_fuzzable_group("key", ['room_id','sender']  ,quoted=True, examples=["room_id"]),
    primitives.restler_static_string("""
                                }
                            ]
                        }
                    ,
                    "keys":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["content.body"]),
    primitives.restler_static_string("""
                    ],
                    "order_by":"""),
    primitives.restler_fuzzable_group("order_by", ['recent','rank']  ,quoted=True, examples=["recent"]),
    primitives.restler_static_string(""",
                    "search_term":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["martians and men"]),
    primitives.restler_static_string("""
                }
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/search"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/sendToDevice/{eventType}/{txnId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sendToDevice"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["m.new_device"]),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("txnId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "messages":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"@alice:example.com\":{\"TLLBEANAAG\":{\"example_content_key\":\"value\"}}}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/sendToDevice/{eventType}/{txnId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/sync, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sync"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filter="),
    primitives.restler_static_string(__matrix_client_v3_user__userId__filter_post_filter_id.reader(), quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["s72594_4483_1934"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("full_state="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("set_presence="),
    primitives.restler_custom_payload("set_presence", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeout="),
    primitives.restler_custom_payload("timeout", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("use_state_after="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse__matrixclientv3syncget,
            'dependencies':
            [
                __matrix_client_v3_sync_get_next_batch.writer()
            ]
        }

    },

],
requestId="/_matrix/client/v3/sync"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/thirdparty/location, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("thirdparty"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("location"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alias="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["#matrix:matrix.org"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/thirdparty/location"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/thirdparty/location/{protocol}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("thirdparty"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("location"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["irc"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/thirdparty/location/{protocol}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/thirdparty/protocol/{protocol}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("thirdparty"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("protocol"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["irc"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/thirdparty/protocol/{protocol}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/thirdparty/user, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("thirdparty"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("userid="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["@bob:matrix.org"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/thirdparty/user"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/thirdparty/user/{protocol}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("thirdparty"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["irc"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/thirdparty/user/{protocol}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/filter/{filterId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("filter"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_user__userId__filter_post_filter_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/filter/{filterId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/openid/request_token, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("openid"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("request_token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/openid/request_token"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/rooms/{roomId}/account_data/{type}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account_data"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["org.example.custom.room.config"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/rooms/{roomId}/account_data/{type}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/rooms/{roomId}/account_data/{type}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account_data"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("type", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"custom_account_data_key\":\"custom_account_data_value\"}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/rooms/{roomId}/account_data/{type}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/rooms/{roomId}/tags, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/rooms/{roomId}/tags"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/rooms/{roomId}/tags/{tag}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["u.work"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/rooms/{roomId}/tags/{tag}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/rooms/{roomId}/tags/{tag}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_createRoom_post_room_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("tag", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "order":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.25"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/rooms/{roomId}/tags/{tag}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/users/{userId}/report, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(__matrix_client_v3_account_whoami_get_user_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "reason":"""),
    primitives.restler_custom_payload("reason", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/users/{userId}/report"
)
req_collection.add_request(request)

# Endpoint: /_matrix/media/v1/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/media/v1/create"
)
req_collection.add_request(request)

# Endpoint: /_matrix/media/v3/config, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("config"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/media/v3/config"
)
req_collection.add_request(request)

# Endpoint: /_matrix/media/v3/download/matrix.leap04/{mediaId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("download"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matrix.leap04"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ascERGshawAWawugaAcauga"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("allow_remote="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeout_ms="),
    primitives.restler_custom_payload("timeout_ms", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("allow_redirect="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/media/v3/download/matrix.leap04/{mediaId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/media/v3/download/matrix.leap04/{mediaId}/{fileName}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("download"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matrix.leap04"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ascERGshawAWawugaAcauga"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["filename.jpg"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("allow_remote="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeout_ms="),
    primitives.restler_custom_payload("timeout_ms", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("allow_redirect="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/media/v3/download/matrix.leap04/{mediaId}/{fileName}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/media/v3/preview_url, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("preview_url"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("url="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["https://matrix.org"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ts="),
    primitives.restler_fuzzable_int("1", examples=["1510610716656"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/media/v3/preview_url"
)
req_collection.add_request(request)

# Endpoint: /_matrix/media/v3/thumbnail/matrix.leap04/{mediaId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("thumbnail"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matrix.leap04"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ascERGshawAWawugaAcauga"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("width="),
    primitives.restler_fuzzable_int("1", examples=["64"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height="),
    primitives.restler_fuzzable_int("1", examples=["64"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("method="),
    primitives.restler_custom_payload("method", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("allow_remote="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeout_ms="),
    primitives.restler_custom_payload("timeout_ms", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("allow_redirect="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("animated="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/media/v3/thumbnail/matrix.leap04/{mediaId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/media/v3/upload, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("upload"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filename="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["War and Peace.pdf"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/media/v3/upload"
)
req_collection.add_request(request)

# Endpoint: /_matrix/media/v3/upload/matrix.leap04/{mediaId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("upload"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matrix.leap04"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("mediaId", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filename="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["War and Peace.pdf"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/media/v3/upload/matrix.leap04/{mediaId}"
)
req_collection.add_request(request)
