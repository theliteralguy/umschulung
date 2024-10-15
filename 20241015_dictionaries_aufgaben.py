# Aufgabe 1
# Erstelle ein Dictionary, da die Noten eines Schülers in verschiedenen Fächern speichert.
# Schreibe ein Programm, das die Note für ein Fach abfragt und ausgibt. Verwende get() und
# fange mit if und else einen Fehler ab, falls das Fach nicht existiert.
 
""" noten = {
    "Mathematik": 2,
    "Deutsch": 3,
    "Englisch": 1,
    "Biologie": 2,
    "Physik": 4
}

fach = input("Gib ein Fach ein: ")

note = noten.get(fach)

if note is not None:
    print(f"Die Note in {fach} ist: {note}")
else:
    print("Dieses Fach existiert nicht im Notenbuch.") """


# AUfgabe 2
# Erstelle ein Dictionary mit den Namen von 5 Mitarbeitern und ihren Positionen in einem Betrieb.
# Schreibe ein Programm, das einen Benutzer nach dem Namen fragt und entweder die Position des
# Mitarbeiters ausgibt oder "Mitarbeiter konnte nicht gefunden werden" anzeigt, wenn der Name
# nicht im Dicitonary vorhanden ist (benutze get() )
 # Dictionary mit den Namen und Positionen der Mitarbeiter

""" mitarbeiter = {
    "Anna": "Vertriebsleiterin",
    "Max": "Softwareentwickler",
    "Lisa": "Buchhalterin",
    "Tom": "Marketing Manager",
    "Julia": "Personal"
}

# Name des Mitarbeiters abfragen
name = input("Gib den Namen eines Mitarbeiters ein: ")

# Überprüfen, ob der Name existiert und die Position ausgeben, falls sie existiert
position = mitarbeiter.get(name)

if position is not None:
    print(f"{name} ist {position}.")
else:
    print("Mitarbeiter konnte nicht gefunden werden.") """

# Aufgabe 3
# Erstelle ein Dictionary, das 5 Lebensmittel und ihre Preise enthält. Baue eine Funktion, die neue Produkte und
# deren Preise speichert. Erweitere deine Funktion, indem du nach einem
# Artikel suchst und gib ihn mit seinem Preis aus. Wenn der Artikel nicht gefunden wurde, soll der Artikel gespeichert werden und einen
# Standardpreis von 0 zurückgegeben
 
 # Dictionary mit Lebensmitteln und ihren Preisen
""" lebensmittel = {
    "Apfel": 1.20,
    "Brot": 2.50,
    "Milch": 1.00,
    "Käse": 3.50,
    "Eier": 2.00
}

# Funktion zum Hinzufügen neuer Produkte und Preise
def produkt_hinzufuegen(name, preis):
    lebensmittel[name] = preis
    print(f"{name} wurde mit dem Preis {preis} hinzugefügt.")

# Funktion, um nach einem Artikel zu suchen und den Preis auszugeben
def artikel_suchen(artikel):
    preis = lebensmittel.get(artikel)
    if preis is not None:
        print(f"Der Preis für {artikel} beträgt: {preis} €")
    else:
        print(f"{artikel} wurde nicht gefunden und wird nun hinzugefügt.")
        # Artikel mit Standardpreis von 0 speichern
        lebensmittel[artikel] = 0
        print(f"{artikel} wurde mit einem Standardpreis von 0 € hinzugefügt.")

# Test des Programms
artikel = input("Gib den Namen eines Lebensmittels ein: ")
artikel_suchen(artikel)

# Beispiel zum Hinzufügen eines neuen Produkts
produkt_hinzufuegen("Butter", 1.80)
 """













 
# Aufgabe 4
# Erstelle ein Dicitonary mit dem Namen und dem Alter von 3 Personen. Schreibe ein Programm,
# das durch die Schlüssel des Dictionaries iteriert und nur die Namen der Personen ausgibt

""" my_dict = {"John": 30,"Alex": 20, "Athena": 35}
for key,value in my_dict.items():
    print(key) """
 
 









# Aufgabe 5
# Gegeben ist ein Dictionary, das die Lagerbestände eines Geschäfts speichert.
# Schreibe ein Programm, das alle Artilkel ausgibt, die aktuell im Lager sind
# (Tipp: Schlüssel mit Wert > 0)
 
 
# Dictionary, das die Lagerbestände eines Geschäfts speichert

""" articles = {
    "Screws": 10000,
    "Wood": 0,
    "Nails": 100,
    "Toolkit": 10,
    "Scanner": 2,
    "Paper": 0
}

# Funktion, um alle Artikel mit Lagerbestand > 0 auszugeben
def verfuegbare_artikel_anzeigen():
    print("Verfügbare Artikel im Lager:")
    for artikel, bestand in articles.items():
        if bestand > 0:
            print(f"- {artikel}: {bestand} Stück")

# Funktion aufrufen, um die verfügbaren Artikel anzuzeigen
verfuegbare_artikel_anzeigen() """









# Aufgabe 6
# Du findest ein Dictionary mit Ländern als Schlüssel und deren Bevölkerungszahlen als Wert.
# Schreibe ein Programm, das die Länder nach Namen sortiert und in alphabetischer Reihenfolge
# die Namen ausgibt
 
""" countries = {
    "Deutschland": 85000000,
    "Frankreich": 68000000,
    "Spanien": 47000000,
    "Polen": 36000000,
}
 

# Funktion, um die Länder alphabetisch zu sortieren und auszugeben
def laender_sortiert_ausgeben():
    print("Länder in alphabetischer Reihenfolge:")
    for land in sorted(countries.keys()):
        print(land)

# Funktion aufrufen, um die Länder auszugeben
laender_sortiert_ausgeben() """













 
# Aufgabe 7
# Erstelle ein Dictionary mit fünf Tieren und deren Anzahl im Lager aus einem Tierhandel. Schreibe ein
# Programm, das die Summe aller Werte im Dicitonary berechnet und ausgibt.
 
# Aufgabe 8
# Du findest ein Dictionary mit den Namen von Schülern als Schlüssel und deren Noten als Werte.
# Schreibe ein Programm, das den Notendurchschnitt aller Noten berechnet (benutze values() und keys())
 
students = {
    "Alan": 1,
    "Jacques": 6,
    "Gerhard": 1,
    "Willi": 4,
    "Susanne":2
}
 