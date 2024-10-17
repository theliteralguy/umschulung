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
# Artikel suchst und gib ihn mit seinem Preis aus. Wenn der Artikel nicht gefunden wurde, soll der Artikel gespeichert
# werden und einen Standardpreis von 0 zurückgegeben
 
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


#####jacques solution:


""" products = {
    "apple": 3.99,
    "pineapple": 4.99,
    "eggs": 3.95,
    "chickenwings": 5.99,
    "pizza": 2.99
}
 
 
 
def save_products():
 
    choice = int(input("Möchtest du ein neues Produkt speichern oder ein Produkt suchen? 1 : Produkt speichern, 2 : Produkt suchen"))
 
    if choice == 1:
        new_product = input("Bitte gib ein neues Produkt ein: ")
        price = float(input("Bitte gib einen Preis für das neue Produkt ein: "))
        products.update({new_product : price})
        print(f"Das neue Produkt {new_product} wurde mit einem Preis von {price} gespeichert")
    elif choice == 2:
        search = input("Bitte gib das Produkt ein, welches du suchst: ")
        if search in products:
            result = products.get(search)
            print(f"Das Produkt {search} wurde gefunden. Es kostet {result}")
        elif search not in products:
            products.setdefault(search,0)
            print(f"Es wurde ein neues Produkt {search} hinzugefügt welches standardmäßig {products.get(search)} kostet")
    print(products)
   
save_products() """










 
# Aufgabe 4
# Erstelle ein Dicitonary mit dem Namen und dem Alter von 3 Personen. Schreibe ein Programm,
# das durch die Schlüssel des Dictionaries iteriert und nur die Namen der Personen ausgibt

""" my_dict = {"John": 30,"Alex": 20, "Athena": 35}
for key in my_dict.keys():
    print(key) """
 
 ###Jacques:

""" persons = {
    "German": 25,
    "Patrick": 28,
    "Roland": 22
}
 
for names in persons.keys():
    print(names) """









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


##jacques

""" articles = {
    "Screws": 10000,
    "Wood": 0,
    "Nails": 100,
    "toolkit": 10,
    "scanner": 2,
    "paper": 0,
}
 
for key, value in articles.items():
    if value > 0:
        print(key, value) """









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
    for land in sorted(countries.keys()):
        print(land)

# Funktion aufrufen, um die Länder auszugeben
laender_sortiert_ausgeben() """













 
# Aufgabe 7
# Erstelle ein Dictionary mit fünf Tieren und deren Anzahl im Lager aus einem Tierhandel. Schreibe ein
# Programm, das die Summe aller Werte im Dicitonary berechnet und ausgibt.

# Dictionary mit Tieren und deren Anzahl im Lager
""" tiere = {
    "Hunde": 15,
    "Katzen": 10,
    "Vögel": 25,
    "Fische": 100,
    "Hamster": 8
}

def gesamtanzahl_tiere():
    gesamtanzahl = sum(tiere.values())
    print(f"Die Gesamtanzahl der Tiere im Lager beträgt: {gesamtanzahl}")

# Funktion aufrufen, um die Summe auszugeben
gesamtanzahl_tiere() """

 
 
# Aufgabe 8
# Du findest ein Dictionary mit den Namen von Schülern als Schlüssel und deren Noten als Werte.
# Schreibe ein Programm, das den Notendurchschnitt aller Noten berechnet (benutze values() und keys())
 
""" students = {
    "Alan": 1,
    "Jacques": 6,
    "Gerhard": 4,
    "Willi": 4,
    "Susanne":2
}
 
 # Dictionary mit Namen der Schüler und deren Noten
schueler_noten = {
    "Anna": 2,
    "Ben": 3,
    "Clara": 1,
    "David": 4,
    "Eva": 2
}

def notendurchschnitt_berechnen():
    summe = sum(schueler_noten.values()) 
    anzahl = len(schueler_noten.keys()) 
    durchschnitt = summe / anzahl
    print(f"Der Notendurchschnitt beträgt: {durchschnitt:.2f}")

notendurchschnitt_berechnen() """







# Aufgabe 9
# Erstelle ein Dictionary, das den Umsatz verschiedener Filialen eines Unternehmens speichert.
# Nutze den Filialnamen als Schlüssel und den Umsatz als Wert.
# Schreibe ein Programm, das die Filiale mit dem höchsten Umsatz identifiziert und den Namen
# der Filiale sowie den Umsatz ausgibt
 
# Dictionary mit den Umsätzen der Filialen



# Dictionary mit den Umsätzen der Filialen
""" umsatz = {
    'Filiale A': 15000,
    'Filiale B': 22000,
    'Filiale C': 18000,
    'Filiale D': 25000,
    'Filiale E': 21000
}

hoechste_filiale = ''
hoechster_umsatz = 0

# Über das Dictionary iterieren, um die Filiale mit dem höchsten Umsatz zu finden
for filiale, betrag in umsatz.items():
    if betrag > hoechster_umsatz:
        hoechster_umsatz = betrag
        hoechste_filiale = filiale

# Ergebnis ausgeben
print("Die Filiale mit dem höchsten Umsatz ist:", hoechste_filiale)
print("Umsatz:", hoechster_umsatz, "Euro") """








# Aufgabe 10
# Erstelle ein Wörterbuch, welches die Preise von 5 Artikeln speichert. Verwende items() um durch die Schlüssel
# Wert Paare zu iterieren und alle Artikel, deren Preis über 10 € liegt, auszugeben

# Wörterbuch mit den Preisen der Artikel
""" preise = {
    'Apfel': 2.50,
    'Brot': 1.80,
    'Käse': 12.00,
    'Schokolade': 8.50,
    'Wein': 15.00
}

for artikel, preis in preise.items():
    if preis > 10:
        print(f"Artikel: {artikel}, Preis: {preis} €") """















 # Aufgabe 11
# Erstelle ein Dictionary, das die Punktzahl von Spielern in einem Videospiel speichert.
# Der Spielername ist der Schlüssel und die Punktzahl der Wert. Schreibe ein Programmm, welches den Spieler ausgibt,
# der die höchste Punktzahl hat. (Benutze items())
 
# Dictionary mit den Punktzahlen der Spieler
""" punkte = {
    'Spieler1': 1500,
    'Spieler2': 2300,
    'Spieler3': 1800,
    'Spieler4': 2700,
    'Spieler5': 2200
}

# Variablen für den Spieler mit der höchsten Punktzahl
bester_spieler = ''
hoechste_punktzahl = 0

# Durch das Dictionary iterieren und den Spieler mit der höchsten Punktzahl finden
for spieler, punktzahl in punkte.items():
    if punktzahl > hoechste_punktzahl:
        hoechste_punktzahl = punktzahl
        bester_spieler = spieler

print("Der Spieler mit der höchsten Punktzahl ist:", bester_spieler)
print("Punktzahl:", hoechste_punktzahl) """



#jacques
""" players = {
    "Horsti": 1200,
    "Toddy": 890,
    "Mucki": 3200,
    "Schneidi": 430,
    "Hechti": 788,
}
 
max_points = max(players.values())
print(max_points)
 
for player, points in players.items():
    if points == max_points:
        print(f"Spieler {player} hat die meisten Punkte mit {points}") """








# AUfgabe 12
# Erstelle ein Dictionary mit Informationen über einen Film (z.B.: Titel, Jahr, Genre). Schreibe ein Programm dass
# das Dictionary mithilfe von update um die Bewertung des Films erweitert.

# Dictionary mit Informationen über einen Film

""" film = {
    'Titel': 'The Fountain',
    'Jahr': 2006,
    'Genre': 'Sci-fi'
}

# Das Dictionary mit einer Bewertung erweitern
film.update({'IMDb Bewertung': 7.2})

print(film) """

#jacques

""" movies = {
    "title": "Ghostbusters",
    "year": "1998",
    "Genre": "Science Fiction",
}
 
movies.update({"reviews": 5})
print(movies) """


# Aufgabe 13
# Erstelle 2 Dictionaries die jeweils den Lagerbestand in zwei verschiedenen Filialen eines Geschäfts darstellen.
# Schreibe ein Programm das den Lagerbestand der beiden Filialen zusammenführt (benutze Update) und gib das
# kombinierte Dicitonary aus


# Dictionaries representing the stock of two different store branches
""" filiale1 = {
    'Apples': 50,
    'Bananas': 30,
    'Oranges': 20
}

filiale2 = {
    'Bananas': 20,
    'Oranges': 15,
    'Pineapples': 10
}

combined_stock = filiale1.copy()  # Make a copy of the first dictionary to avoid modifying the original

# Loop through the items in the second dictionary and add them to the combined stock
for item, quantity in filiale2.items():
    if item in combined_stock:
        combined_stock[item] += quantity 
    else:
        combined_stock[item] = quantity

print(combined_stock) """






# Aufgabe 14
# Du findest ein Dictionary mit Produkten und ihren Preisen Schreibe ein Programm, das den Benutzer auffordert, 
# den Preis eines Produkts zu aktualisieren. Verwende update() um das Produkt mit dem neuen Preis im Dicitonary
# zu aktualisieren.
 
""" products = {
    "Apple": 2.99,
    "Pineapple": 1.99,
    "Beans": 1.49,
    "Tomato": 1.79
}
product_name = input("Enter the name of the product you want to update: ")
if product_name in products:
    new_price = float(input(f"Enter the new price for {product_name}: "))
    products.update({product_name: new_price})
    print(products)
else:
    print("Product not found.") """





#jacques:

""" products = {
    "Apple": 2.99,
    "Pineapple": 1.99,
    "Beans": 1.49,
    "Tomato": 1.79
}
 
def update_price():
    article = input("Bei welchem Artikel möchtest du den Preis anpassen ?")
    new_price = float(input(f"Bitte gib einen neuen Preis für {article} ein"))
    new_price = f"{new_price:.2f}"
    if article in products.keys():
        print(f"{article} wurde gefunden")
        products.update({article : new_price})
        print(f"Der Artikel {article} wurde angepasst. {products}")
    else:
        print(f"Artikel {article} konnte nicht gefunden werden")
 
update_price() """
 


 # Aufgabe 15
# Erstelle ein Dictionary mit dem Namen von drei Klassenkameraden und deren Handynummern. Schreibe ein Programm,
# dass das Dicitonary mit clear() leert und überprüft, ob es nun leer ist.

# Dictionary with names of classmates and their phone numbers

""" classmates = {
    "Lars": "01521211548787",
    "Abd": "001675487545",
    "Oliver": "01687545797"
}

classmates.clear()

if not classmates:
    print("The dictionary is now empty.")
else:
    print("The dictionary is not empty.") """

    #jacques

""" contacts = {
    "German": "0123456789",
    "Alex": "987654321",
    "Lukas": "135797531",
}
 
#contacts.clear()
if len(contacts.keys()) < 1:
    print(f"Einträge: {len(contacts.keys())}")
    print(f"Die Kontaktliste ist Leer: {contacts}")
else:
    print(f"Einträge: {len(contacts.keys())}")
    print(f"Hier sind deine Kontakte: {contacts}") """




# Aufgabe 16
# Baue 2 Funktionen. Eine der beiden Funktionen soll einen Studenten und seine Note nach der Eingabe eines Benutzers in dem Dictionary speichern, allerdings nur, wenn
# weniger als 5 Studenten in dem Dictionary gespeichert sind.
# Falls schon 5 Studenten in dem Dictionary gespeichert sind, gib den Notendurschnitt aller Studenten aus und stelle den Benutzer vor eine Wahl, ob er das
# aktuelle Dictionary löschen möchte um den neuen Studenten dort abspeichern zu können. Fällt die Antwort auf Nein, beende das Programm.
# Falls die Wahl auf das löschen des Dicitonaries fällt, benutze die 2. Funktion und übergib die Eingabe des Benutzers als Dicitonary in den Parametern
# Erweitere deine 2. Funktion indem du das Dictionary löscht, und die neuen Werte aus den Funktionsparametern speicherst.
# Gib deine Eingabe des neuen Studenten aus und auch, das dieser Student erfolgreich gespeichert wurde.
 
student_graduations = {
    "Micky": 1,
    "Daisy": 3,
    "Donald": 6,
    "Dagobert": 1,
    "Goofy": 3,
}


# Initialize the student dictionary
student_graduations = {
    "Micky": 1,
    "Daisy": 3,
    "Donald": 6,
    "Dagobert": 1,
    "Goofy": 3,
}

def add_student(student_dict):
    # Check the number of students in the dictionary
    if len(student_dict) < 5:
        # Get user input for the new student
        name = input("Gib den Namen des Studenten ein: ")
        grade = int(input("Gib die Note des Studenten ein: "))
        # Store the student in the dictionary
        student_dict[name] = grade
        print(f"{name} wurde erfolgreich gespeichert mit der Note {grade}.")
    else:
        # Calculate the average grade
        average_grade = sum(student_dict.values()) / len(student_dict)
        print(f"Der Notendurchschnitt aller Studenten ist: {average_grade:.2f}")
        
        # Ask the user if they want to reset the dictionary
        choice = input("Möchten Sie das Dictionary löschen? (ja/nein): ").strip().lower()
        if choice == 'ja':
            reset_dictionary(student_dict)
        else:
            print("Programm beendet.")
            return

def reset_dictionary(student_dict):
    # Clear the dictionary
    student_dict.clear()
    # Get user input for the new student
    name = input("Gib den Namen des neuen Studenten ein: ")
    grade = int(input("Gib die Note des neuen Studenten ein: "))
    # Store the new student in the dictionary
    student_dict[name] = grade
    print(f"{name} wurde erfolgreich gespeichert mit der Note {grade}.")

# Main execution
add_student(student_graduations)

