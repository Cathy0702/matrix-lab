import socket

HOST = "198.162.52.40"
PORT = 8008

body = b'{ "fuzz": false }'
content_length = len(body)  # 18

req = (
    b"PUT /_matrix/client/v3/rooms/!LTQaXvsEkvbSvpSnIV:matrix.chowchow/send/m.reaction/333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333 HTTP/1.1\r\n"
    b"Host: localhost:8008\r\n"
    b"Accept: application/json\r\n"
    b"Content-Type: application/json\r\n"
    b"Authorization: Bearer syt_c2xpdTA3MDI_UXsuiggNjkqpBLAAXtHg_01kUsf\r\n"
    b"Content-Length: " + str(content_length).encode() + b"\r\n"
    b"\r\n"
    + body
)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(req)

resp = s.recv(8192)
print(resp.decode(errors="ignore"))

s.close()