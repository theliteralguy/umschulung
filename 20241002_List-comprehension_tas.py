# Aufgabe 1
# Erstelle eine Liste von Quadratzahlen der Zahlen von 1 bis 20

""" squared_nums = [x**2 for x in range(1,21)]
print(squared_nums) """







 
# Aufgabe 2
# Hier ist eine Liste von graden Zahlen. Verwende eine List Comprehension um nur die
# graden Zahlen herauszufiltern
 
""" zahlen = [10, 15, 23, 42, 55, 68, 73, 80, 87, 93, 96, 99, 110, 111, 120]
 
even_numbers = [x for x in zahlen if x % 2 == 0]
print(even_numbers) """
 









# Aufgabe 3
# Du findest eine Variable vom Datentyp String, Erstelle eine neue Liste die nur die Vokale a, e, i, o, u aus dem String enthält
 
""" satz = "Zehn zahme Ziegen zogen zehn Zentner Zucker zum Zoo"

new_list = [x for x in satz if x in ["a", "e", "i", "o", "u"]]
print(new_list) """
 









# Aufgabe 4
# Erstelle eine Liste mit den Zahlen 1 bis 100, aber nimm nur die Zahlen auf, welche durch 5 oder 7 teilbar sind

""" divisible_by_5and7 = [x for x in range (1,101) if x % 5 == 0 or x % 7 == 0]
print(divisible_by_5and7) """
 







 
# Aufgabe 5
# Du findest eine Liste mit Wörtern. Erstelle eine neue Liste die nur Wörter enthält die länger als 4 Zeichen lang sind
 
""" woerterliste = ['Apfel', 'Ei', 'Banane', 'Traube', 'Ananas', 'Kiwi', 'Uwe', 'Rettungswagen', 'Schlafmütze']
longer_than_four = [x for x in woerterliste if len(x) > 4]
print(longer_than_four) """







 
# Aufgabe 6
# Du findest einen Satz. Erstelle eine Liste, die die Länge jedes Wortes in diesem Satz erhält
 
""" satz = "Ihr werdet besser und besser. Hört nicht auf zu lernen, ihr seid richtig gut <3"

word_lengths = [len(word) for word in satz.split()]
print(word_lengths) """








# Aufgabe 7
# Erstelle eine Liste der Quadratzahlen von 1 bis 50, aber nur für ungrade Zahlen
""" squared_nums = [x**2 for x in range(1,51) if x % 2 != 0]
print(squared_nums) """
 







 
# Aufgabe 8
# Du findest eine Liste mit Wörtern. Erstelle eine Liste, in der jedes Wort in Großbuchstaben umgewandelt wird
 
""" wortliste = ["Das", "ist", "eine", "sehr", "einfache", "Übung", "um", "dir", "das", "Leben", "schwer", "zu", "machen"]
 
capitalized = [word.upper() for word in wortliste]
print(capitalized) """








 
# Aufgabe 9
# Du findest 2 Listen. Erstelle eine neue Liste von Tupeln, die alle Kombinationen von Zahl und Buchstaben enthalten
 
""" zahlen = [1, 2, 3]
buchstaben = ['A', 'B', 'C']
 
combined = [(x,y) for x in zahlen for y in buchstaben]
print(combined) """










# Aufgabe 10
# Du findest eine Liste mit 1000 Namen. Baue ein Programm, in dem ein Benutzer einen Namen eigeben muss. Benutze die List Comprehension dazu,
# die Namensliste nach dem Namen zu durchsuchen unabhängig davon, ob der Benutzer den Namen groß oder klein schreibt.
# Messe die Zeit wie lange deine List Comprehension dafür benötigt hat.
 
""" import random
 
vornamen = ["Anna", "Ben", "Clara", "David", "Eva", "Felix", "Greta", "Hannes", "Iris", "Jonas",
            "Klara", "Lukas", "Maria", "Nina", "Oskar", "Paula", "Quentin", "Rosa", "Sebastian", "Tina",
            "Uwe", "Vera", "Walter", "Xenia", "Yannik", "Zoe"]
 
nachnamen = ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker",
             "Schulz", "Hoffmann", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder",
             "Neumann", "Schwarz", "Zimmermann", "Krüger", "Hartmann", "Lange", "Werner", "Schmitz"]
 
namen_liste = [f"{random.choice(vornamen)} {random.choice(nachnamen)}" for _ in range(1000)]
print(namen_liste)
 

import time
user_inputed_name = input("Please enter a name: ").lower()
print(f"Starting time: {time.time()}")
name_matched = [name for name in namen_liste if user_inputed_name == name.lower()]
print(f"Finishing time: {time.time()}")
print(f"{name_matched} was found in the list")
 """