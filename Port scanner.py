import socket

text = input()
portStart = 0
portEnd = 100
timeout = 1.0
lista = text.split()
url = ''
URLBylo = False
TBylo = False
PBylo = False

def scan(url, PortStart, PortEnd,timeout):
    print("\033[1;32;40m", end = "")
    for i in range(PortStart, PortEnd):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        if s.connect_ex((url, i)) == 0: 
            print(i, " Port is open")
        s.close()

i = 0
while i < len(lista) and not PBylo:
    if lista[i] == '-p':
        portStart = int(lista[i + 1])
        portEnd = int(lista[i + 2])
        PBylo = True
    elif lista[i] == '-T' and not TBylo:
        timeout = float(lista[i + 1])
        TBylo = True
    elif not URLBylo:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            s.connect((lista[i], 80))
            url = lista[i]
            URLBylo = True
        except:
            pass
    i += 1

scan(url, portStart, portEnd, timeout)
