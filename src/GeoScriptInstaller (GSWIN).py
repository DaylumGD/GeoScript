import firebase_admin
from firebase_admin.firestore import client

import sys
import ctypes

import shutil
import os
import time

from consolemenu import ConsoleMenu
consolemenu = ConsoleMenu()

#Initalizing
print('Initalizing...')

def admin_check():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
            return False
if admin_check() == False:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
print('Permitions elivated...')
time.sleep(0.1)

firecred = {
  "apiKey": "Private Google key",
  "authDomain": "personal-projects-808b0.firebaseapp.com",
  "projectId": "personal-projects-808b0",
  "storageBucket": "personal-projects-808b0.appspot.com",
  "messagingSenderId": "718249760844",
  "appId": "1:718249760844:web:aa26afd6a3fa310be3fce9",
  "measurementId": "G-DBL2S6GS1X",
  "databaseURL": "personal-projects-808b0.appspot.com"
}


app = firebase_admin.initialize_app(options=firecred)
db = client(app)
print('Firebase connection secured...')
time.sleep(0.1)

consolemenu.clear_screen()
print('GeoScript installer')