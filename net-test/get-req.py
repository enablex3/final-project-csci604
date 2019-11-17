import socket, time

site = "google.com"
port = 80
req = "GET / HTTP/1.0\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
startTime = time.time()
s.connect((site, port))
s.sendall(req.encode())
endTime = round(((time.time() - startTime) * 1000000), 3)
print('{} microseconds...'.format(endTime))
