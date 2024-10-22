# Aufgabe 1
# Schreibe ein Programm, das den Benutzer auffordert, eine ganze Zahl einzugeben und diese Zahl verdoppelt.
# Verwende deine Kenntnisse im Error Handling um eine ValueError exception abzufangen, falls der Benutzer
# etwas anderes als eine Zahl eingibt.
 

# while True:
#     try:
#         zahl = int(input("Bitte eine ganze Zahl eingeben: "))
#         print("Das Doppelte der Zahl ist:", zahl * 2)
#         break
#     except ValueError:
#         print("Fehler: Bitte eine gültige ganze Zahl eingeben.")
#         continue


#jacques solution:

def double_number(x):
    return x * 2
 
 
def pick_number():
    while True:
        try:
            number = int(input("Bitte gib eine ganze Zahl ein, die verdoppelt werden soll: "))
        except ValueError:
            print("Eingabe ungültig, bitte gib eine ganze Zahl ein!")
            continue
        else:
            print(f"Das doppelte der Zahl {number} ist {double_number(number)}")
            break
 
#pick_number()
 
# Aufgabe 2
# Schreibe eine Funktion mit dem Namen addieren(a, b), die zwei Zahlen als Parameter empfängt.
# Verwende deine Error Handling Skills um einen TypeError abzufangen, falls einer der Parameter
# kein Zahlentyp ist
 
 
def addieren():
    while True:
        try:
            a = float(input("Bitte die erste Zahl eingeben: "))
            b = float(input("Bitte die zweite Zahl eingeben: "))
            result = a + b
            print("Das Ergebnis der Addition ist:", result)
            break
        except ValueError:
            print("Fehler: Bitte gültige Zahlen eingeben.")
            continue

#addieren()

#jacques solution:

def addieren(a,b):
    try:
        ergebnis = a + b
    except TypeError:
        print("Einer beiden Werte sind keine Zahlen.")
    else:
        print(ergebnis)
 
#addieren(2,"3")

 
# Aufgabe 3
# Schreibe eine Funktion mit dem Namen teilen, die 2 Zahlen als Parameter erhält und das Ergebnis einer
# Division zurück gibt. Verwende try und except um eine Division durch Null zu verhindern und eine
# entsprechende Fehlermeldung auszugeben

def teilen(a, b):
    try:
        result = a / b
        print("Das Ergebnis der Division ist:", result)
    except ZeroDivisionError:
        print("Fehler: Division durch Null ist nicht erlaubt.")


# Beispielaufruf
#teilen(10, 2)  # Korrekt
#teilen(10, 0)  # Fehler wegen Division durch Null

