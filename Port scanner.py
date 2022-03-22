import socket
def scan(url = 'www.google.com', PortStart = 0, PortEnd = 100):
    for i in range(PortStart, PortEnd):
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a_socket.settimeout(1)
        if a_socket.connect_ex((url, i)) == 0: 
            print("\033[1;32;40m")
            print(i, " Port is open")
        else: 
            print("\033[1;31;40m")
            print(i, " Port is not open")
        a_socket.close()

url = input('Specify url: ')
wants = input('Do you want to specify port range: ')

if wants == 'yes':
    portStart = int(input('The port you want to start: '))
    portEnd = int(input('The port you want to end: '))
    scan(url, portStart, portEnd)
else: 
    scan(url)
