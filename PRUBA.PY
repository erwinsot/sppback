import subprocess
import os

import time

#ff=subprocess.run("cd..", shell=True)
#time.sleep(2)
comand=input("escribe el comando: ")
os.chdir('c:/Users/simbionte/Documents/')
subprocess.run(comand, shell=True)

#print(ff)
