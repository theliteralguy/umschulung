namens_liste = [
    "Matthias",
    "Anas",
    "Fatjon",
    "Oliver",
    "Ina"
]
 
""" # print(len(namens_liste))
 
name = "Ina"
 
for names in namens_liste:
    if names == "Ina":
        print("Wir haben " + name + " gefunden")
    else:
        print("Wir konnten " + name + " nicht finden") """
 
 
 
 
 
 
 
 
 
namens_liste = [
    "Matthias",
    "Anas",
    "Fatjon",
    "Oliver",
    "Ina"
]
 
""" # print(len(namens_liste))
 
name = "Pascal"
for index in range(len(namens_liste)):
    if namens_liste[index] == "Pascal":
        print("Wir haben " + name + " gefunden")
    else:
        print("Wir konnten " + name + " nicht finden") """
 
""" anzahl = 0
while True:
    anzahl += 1
    if anzahl == 5:
        print("5 wird übersprungen", anzahl)
 
    if anzahl > 10:
        print("Schritte beendet")
        break
    print("Hallo")
 """
 
 
 
 
 
 
 
 
 
 
# Aufgabe 1
# Schreibe eine for Schleife, die die Summe aller Zahlen von 1 bis 100 berechnet und das Ergebnis ausgibt
""" sum = 0
for num in range(0, 101):
    sum += num
print(sum) """
 
 
 
 
 
 
 
 
 
 
#Aufgabe 2
# Schreibe ein Programm, das eine Liste von Benutzernamen durchläuft und überprüft ob sie gültig sind
# Ein Benutzername ist nur gültig, wenn er länger als 3 Zeichen ist und keine Leerzeichen enthält
""" user_list = ["Max Mustermann", "admin123", "abc"]
def user_validation(user_list):
    for name in user_list:
        if len(name) > 3 and " " not in name:
            print(f"The username {name}is valid ")
        else:
            print(f"The username {name} is invalid ")
 
 
print(user_validation(user_list)) """











# Aufgabe 3
# Erstelle ein Programm, das eine Einkaufsliste verwaltet. Es sollte Artikel von einer Liste entfernen,
# wenn sie bereits gekauft wurden. Verwende dazu eine Schleife, um den Benutzer zu fragen,
# welchen Artikel er gekauft hat, und entferne diesen dann aus der Liste.
 
""" items_list = ["Milk", "Bread", "Egg", "Apple"]
while len(items_list) > 0:
    purchased = input("What have you already purchased? ")
    if purchased in items_list:
        items_list.remove(purchased)
        print(f"Your remainig list is: {items_list}")
    else:
        print(f"{purchased} is not in the items list")
print("You have purchased all items. ")
 """
 
 
 
 
 
 
 
 
 
# Aufgabe 4
# Schreibe ein Programm, das so lange Noten (Zahlen zwischen 1 und 6) vom Benutzer entgegennimmt, bis der Benutzer "0" eingibt.
# Anschließend soll das Programm die Durchschnittsnote berechnen und ausgeben.
 
 
""" grade_sum = 0
while True:
    grade = int(input("Please enter your grade here: "))
    if grade not in range(0,7):
        print("Sorry, but you have entered an invalid grade. It should be bw. 1 - 6")
        continue
    if grade != 0:
        grade_sum += grade
   
    else:
        break
print(grade_sum) """
 
 
 
 
 
 
 
 
# Aufgabe 5
# Schreibe ein Programm, das eine zufällige Zahl zwischen 1 und 20 generiert.
# Der Benutzer soll die Zahl erraten. Wenn der Benutzer richtig rät, beende die Schleife.
# Ansonsten gib Hinweise aus, ob die Zahl zu hoch oder zu niedrig ist.
 

import random
random_number = random.randint(1,20)
print(random_number)
while True:
    user_input = int(input("Please a guess and enter a number bw. 1 - 20: "))
    if user_input > random_number:
        print("Nope, the number is bigger than the desired number. Try agin! ")  
    if user_input < random_number:
        print("Nope, the number is smaller than the desired number. Try agin! ")  
    if user_input == random_number:
        print("Congrats! You won the game! ")
        break
 
 
 
 
 
 
# Aufgabe 6
# Schreibe ein Programm, das vom Benutzer eine Reihe von Zahlen entgegennimmt.
# Verwende eine Schleife, um diese Eingaben zu verarbeiten und negative Zahlen herauszufiltern.
# Gib nur die positiven Zahlen in einer Liste aus.
 
""" positive_numbers = []
negative_numbers = []
while True:
 
    user_input = float(input("Please enter a number or write 0 to end the program: "))
    if user_input != 0 and user_input < 0:
        negative_numbers.append(user_input)
    if user_input != 0 and user_input > 0:
        positive_numbers.append(user_input)
    if user_input == 0:
        break
print(positive_numbers) """
 
 
 
 
 
 
 
 
 
 
# Aufgabe 7
# Baue eine Liste mit 8 Namen
# Schreibe ein Programm mit einer Funktion, welche einen Namen in einer Namensliste scuht, benutze hierfür eine Schleife die durch die Liste iteriert.
# Der Benutzer soll einen Namen in einem Input angeben können.
# Wenn du den Namen gefunden hast, füge dem Namen den Satz : " ist 25 Jahre alt" durch einen weiteren Input hinzu und speichere den Namen mit dem Alter in der Liste
# verwende die time.sleep() Methode um eine Bearbeitungszeit zu simulieren
# nach der simulation der Bearbeitungszeit, gib deine aktualisierung aus.
# Wenn der Name nicht in der Liste ist, gib aus, das der Name in er Liste nicht vorhanden ist
""" names_list2 = ["Ahmad","Mahmood","John","Athena","Alexander","Thor","Aster","Jupiter"]
import time
def name_looker(names_list2):
    user_choice = input("Please enter a name to look for: ")
    for name in names_list2:
        if name == user_choice:
           persons_age = input("How old is he? ")
           print(f"{user_choice} is {persons_age} years old. ")
           time.sleep(3)
           print("The list has been updated. ")
           break
    else:
        print("Sorry, but the name isn't in the list. ")
        
print(name_looker(names_list2)) """












""" import time
namen_liste = ["Anna", "Bernd", "Clara", "David", "Eva", "Frank", "Gina", "Hannah"]
def suche_und_aktualisiere_name(liste):
    gesuchter_name = input("Gib einen Namen ein, den du in der Liste suchen möchtest: ")
    for i in range(len(liste)):
        if liste[i] == gesuchter_name:
            alter = input(f"Wie alt ist {gesuchter_name}? ")
            liste[i] = f"{gesuchter_name} ist {alter} Jahre alt"
            print("Aktualisiere Namen...")
            time.sleep(3)
            print("Der Name wurde aktualisiert!")
            print("Aktualisierte Namensliste:", liste)
            return
    print(f"Der Name {gesuchter_name} ist nicht in der Liste.")
suche_und_aktualisiere_name(namen_liste) """
