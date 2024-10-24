# Aufgabe 6
# Schreibe ein Programm, ds eine Datei mit dem Namen rechnung.txt öffnet und deren Inhalt auf dem Bildschirm ausgibt
# Erstelle einen Ordner mit dem Namen dateien. Speichere darin eine Datei namens rechnung.txt und finde heraus wie du die Datei öffnen und in der Print ausgabe lesen kannst.
# Verwende FileNotFoundError wenn die Datei nicht existiert. Recherchiere wie du die Datei einbinden kannst.

import os

# Step 1: Create a folder named "dateien"
folder_name = "dateien"
if os.path.exists(folder_name) == False:
    os.makedirs(folder_name)  # Creates the folder if it doesn't exist
else:
    pass  # if the folder is already there, then do nothing.

# Step 2: Create a file named "rechnung.txt" and write some content to it
file_path = os.path.join(folder_name, "rechnung.txt")  # Path to the file
with open(file_path, "w") as file:  # Open the file in write mode
    file.write("Dies ist der Inhalt der Rechnung.\n")  # Write some content

# Step 3: Try to open "rechnung.txt" and print its contents
try:
    with open(file_path, "r") as datei:  # Open the file in read mode
        inhalt = datei.read()  # Read the content of the file
        print(inhalt)  # Print the content
except FileNotFoundError:
    print("Fehler: Datei rechnung.txt nicht gefunden!")  # Error message if file not found
