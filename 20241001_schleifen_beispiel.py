namens_liste = [
    "Matthias",
    "Anas",
    "Fatjon",
    "Oliver",
    "Ina",
]

# normale for Schleife
for name in namens_liste:
    print(name) # -> gibt für jeden Eintrag in der Liste den Namen aus


# Beispiel For Schleife mit kleinem Usecase

def update(name):
    print(name + " ist 25 Jahre alt")

name = "Oliver"
for index in range(len(namens_liste)):
    if namens_liste[index] == name:
        print(f"Wir haben {name} gefunden")
        update(name)
    else:
        print(f"Wir konnten {name} nicht finden")



# Beispiel While Schleife

anzahl = 0
while True: # -> Bedingung die erfüllt werden soll
    anzahl += 1 # -> in jedem Schleifendurchlauf wird die Variable anzahl um 1 erhöht

    if anzahl == 5: # -> wenn die Variable anzahl gleich 5 ist ....
        print("5 wird übersprungen",anzahl) # -> wird der print ausgegeben
        continue # -> bricht den Vorgang der Schleife ab und springt wieder zum Anfang der Schleife


    if anzahl > 10: # -> wenn die Variable anzahl größer als 10 ist ... 
        print("Schleife beendet") # -> gib den Print aus
        break # -> unterbrich die Schleife und beende die Schleife 

    print("Hallo")
    




