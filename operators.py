# Aufgabe 1
# Deklariere Variablen der folgenden primitiven Datentypen und weise passende Werte zu und gib sie aus:
# int, float, str, bool
integer1 = 500
float1 = 2.5
str1 = 'This is a text'
bool1 = True





# Aufgabe 2
# Schreibe ein Programm, das zwei Ganzzahlen als Eingabe annimmt und folgende Berechnungen durchführt:
# Addition, Subtraktion, Multiplikation, division, modulo


""" def math(a,b):
    print (a+b)
    print (a-b)
    print (a*b)
    print (a/b)
    print (a%b)
print(math(7,2)) """





# Aufgabe 3
# Schreibe ein Programm, welches einen Fließkommazahl als Input annimmt und diesen Wert in einen Integer umwandelt.
# Danach soll das Programm prüfen ob der Integer Wert grade oder ungrade ist.
""" def float_convertor(a):
    print(int(a))
    if int(a)%2 == 0:
        print("Gerade Zahl")
    else:
        print("Ungerade Zahl")
 
print(float_convertor(39.34345)) """
 




# Aufgabe 4
# Schreibe ein Programm, welches das Alter einer Person abfragt und prüft, ob die Person volljährig ist oder nicht.
# Gib eine entsprechende Nachricht aus, ob Lina, die grade 14 geworden ist in die Discothek darf (Eintritt ab 18)

""" def age_checker():
    age = int(input("Please enter your age: "))
    if age >= 18:
        print("The person is an adult and may enter the club. ")
    else:
        print("Attention! The person is NOT an adult and is NOT allowed to enter the club. ")
print(age_checker()) """





# Aufgabe 5
# Schreibe ein Programm, das drei Zahlen als Input entgegen nimmt und prüft, welche davon die größte ist.
# Gib die größte Zahl aus
""" def lareget_number_finder():
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    num3 = float(input("Please enter the third number: "))
    if num1 > num2 and num3:
        largest = num1
        return largest
    if num2 > num1 and num3:
        largest = num2
    if num3 > num1 and num2:
        largest = num3
    return largest

print(lareget_number_finder()) """





# Aufgabe 6
# Schreibe ein Programm, das zwei Ganzzahlen vergleicht und ausgibt, ob sie gleich sind, oder ob eine Zahl größer
# oder kleiner als die andere ist.
def nums_comparision():
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    if num1 == num2:
        print("Both numbers are equal. ")
    if num1 < num2:
        print("The first numbers is smaller than the second number. ")
    if num1 > num2:
        print("The first numbers is larger than the second number. ")

# Aufgabe 7
# Schreibe ein Programm welches prüft, ob eine Person Zugang zu einem System erhält.
# Die Person hat entweder die Rolle Admin oder Superuser oder das Passwort "secret" um auf das System zugreifen zu können
# Ansonsten wird der Zugriff verweigert
# benutze or
 
 
# Aufgabe 8
# Schreibe eine Funktion, die überprüft, ob eine gegebene Zahl sowohl größer als 10 als auch kleiner als 20 ist.
#  Verwende dafür bitte den and Operator und einen Input der eine Eingabe entgegen nimmt.
 
 
 
# Aufgabe 9
# Schreibe eine Funktion, die überprüft, ob eine Zahl entweder kleiner als 0 oder
# größer als 100 ist. Verwende dabei den or Operator und einen Input für eine Eingabe
 
 
# Aufgabe 10 Sonderaufgabe
# Schreibe ein Programm, das ein Passwort von einem Nutzer entgegen nimmt und überprüft
# ob es mindestens 8 Zeichen lang ist und es muss entweder eine Zahl oder ein Sonderzeichen (@, #, $, %) enthalten