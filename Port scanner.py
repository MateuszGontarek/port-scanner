import socket
def scan(url, portStart = 0, portEnd = 100):
    for i in range(portStart, portEnd):
        location = (url, i)
        if a_socket.connect_ex(location) == 0: print(i, "Port is open")
        else: print(i, "Port is not open")
        a_socket.close()

a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a_socket.settimeout(1)

url = input('Specify url: ')
wants = input('Do you want to specify port range: ')

if wants == 'yes':
    portStart = int(input('The port you want to start: '))
    portEnd = int(input('The port you want to end: '))
    scan(url, portStart, portEnd)
else: scan(url)
