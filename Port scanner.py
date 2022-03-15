import socket
a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = "www.google.com"
for i in range(100):
    location = (url, i)
    if a_socket.connect_ex(location) == 0: print(i, "Port is open")
    else: print(i, "Port is not open")

a_socket.close()