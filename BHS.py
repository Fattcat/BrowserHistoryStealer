import os
import shutil
import sqlite3
import csv
from datetime import datetime

# Adresár na USB disku, kam budeme ukladať históriu prehliadačov
usb_directory = 'E:/CpBrowserHistory'

# Vytvoríme adresár na USB disku, ak ešte neexistuje
if not os.path.exists(usb_directory):
    os.makedirs(usb_directory)

# Kontrola prehliadača Chrome
chrome_source_path = os.path.expanduser('~') + '/AppData/Local/Google/Chrome/User Data/Default'
chrome_history_path = chrome_source_path + '/History'
chrome_destination = usb_directory + '/ChromeHistory.csv'

if os.path.exists(chrome_history_path):
    # Pripojenie k SQLite databáze Chrome histórie
    connection = sqlite3.connect(chrome_history_path)
    cursor = connection.cursor()

    # Získanie histórie navštívených stránok z databázy
    cursor.execute("SELECT url, title, last_visit_time FROM urls")
    history_rows = cursor.fetchall()

    # Uloženie histórie do CSV súboru
    with open(chrome_destination, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Title', 'URL'])

        for row in history_rows:
            url, title, last_visit_time = row
            timestamp = datetime(1601, 1, 1) + datetime.timedelta(microseconds=last_visit_time)
            writer.writerow([timestamp, title, url])

    # Zatvorenie pripojenia k databáze
    cursor.close()
    connection.close()

    print('História prehliadača Chrome bola skopírovaná a uložená.')
else:
    print('Prehliadač Chrome nie je nainštalovaný alebo nemá prítomnú históriu.')

# Kontrola prehliadača Edge
edge_source_path = os.path.expanduser('~') + '/AppData/Local/Microsoft/Edge/User Data/Default'
edge_history_path = edge_source_path + '/History'
edge_destination = usb_directory + '/EdgeHistory.csv'

if os.path.exists(edge_history_path):
    # Pripojenie k SQLite databáze Edge histórie
    connection = sqlite3.connect(edge_history_path)
    cursor = connection.cursor()

    # Získanie histórie navštívených stránok z databázy
    cursor.execute("SELECT url, title, last_visit_time FROM urls")
    history_rows = cursor.fetchall()

    # Uloženie histórie do CSV súboru
    with open(edge_destination, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Title', 'URL'])

        for row in history_rows:
            url, title, last_visit_time = row
            timestamp = datetime(1601, 1, 1) + datetime.timedelta(microseconds=last_visit_time)
            writer.writerow([timestamp, title, url])

    # Zatvorenie pripojenia k databáze
    cursor.close()
    connection.close()

    print('História prehliadača Edge bola skopírovaná a uložená.')
else:
    print('Prehliadač Edge nie je nainštalovaný alebo nemá prítomnú históriu.')
