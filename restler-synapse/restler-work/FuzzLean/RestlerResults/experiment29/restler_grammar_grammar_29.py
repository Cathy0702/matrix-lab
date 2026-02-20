""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

__matrix_client_v3_createRoom_post_room_id = dependencies.DynamicVariable("__matrix_client_v3_createRoom_post_room_id")

def parse__matrixclientv3createRoompost(data, **kwargs):
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
            temp_7262 = str(data["room_id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("__matrix_client_v3_createRoom_post_room_id", temp_7262)

req_collection = requests.RequestCollection([])
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

],
requestId="/_matrix/client/v3/account/whoami"
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
    "topic":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
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

],
requestId="/_matrix/client/v3/rooms/{room_id}/send/m.room.message/{txnId}"
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
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Saying farewell - thanks for the support!"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/{room_id}/leave"
)
req_collection.add_request(request)
