#!/usr/bin/env python3
#
#
from datetime import datetime, timedelta
from csv import reader
import requests

ulanzi_url = "http://192.168.x.x"  # URL der Ulanzi Pixelclock

tomorrow = datetime.now() + timedelta(1)
#print("Tomorrow = ", tomorrow.strftime('%d.%m.%Y'))


# Funktionen definieren
#
# Funktion an Ulanzi senden
def ulanzi_senden(url,data):
    response = requests.post(url, json=data)

#Funktion Check Tonne
def check_tonne(farbe):
    datei= farbe+".csv"
    with open(datei, 'r') as csv_file:
        csv_reader = reader(csv_file)
        data = list(csv_reader)
        print(data)
        if tomorrow.strftime('%d.%m.%Y') in str(data):
            print("Passt!")
            print(farbe)
            url = ulanzi_url + '/api/notify'
            if farbe == "gelb":
                data = {
                    "text": "Achtung! Morgen gelbe Tonne! Rausstellen nicht vergessen! ",
                    "color": [239,245,66],
                    #"repeat": 1
                    "hold": bool(1)
                }
            if farbe == "blau":
                data = {
                    "text": "Achtung! Morgen blaue Tonne! Rausstellen nicht vergessen! ",
                    "color": [0,0,255],
                    #"repeat": 1
                    "hold": bool(1)
                }
            if farbe == "bio":
                data = {
                    "text": "Achtung! Morgen Biomüll! Tonne rausstellen nicht vergessen! ",
                    "color": [196,133,65],
                    #"repeat": 1
                    "hold": bool(1)
                }
            elif farbe == "rest":
                data = {
                    "text": "Achtung! Morgen Restmüll! Tonne rausstellen nicht vergessen! ",
                    "color": [201,200,197],
                    #"repeat": 1
                    "hold": bool(1)
                }
            ulanzi_senden(url, data)
# Ende Funktionen

# Start Programm

check_tonne("rest") # Restmüll
check_tonne("gelb") # Gelbe Tonne
check_tonne("blau") # Blaue Tonne
check_tonne("bio") # Biomüll
