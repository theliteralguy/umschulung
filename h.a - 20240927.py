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
""" def nums_comparision():
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    if num1 == num2:
        print("Both numbers are equal. ")
    if num1 < num2:
        print("The first numbers is smaller than the second number. ")
    if num1 > num2:
        print("The first numbers is larger than the second number. ") """







# Aufgabe 7
# Schreibe ein Programm welches prüft, ob eine Person Zugang zu einem System erhält.
# Die Person hat entweder die Rolle Admin oder Superuser oder das Passwort "secret" um auf das System zugreifen zu können
# Ansonsten wird der Zugriff verweigert
# benutze or
""" def system_access():
    user = input('Please enter your username: ')
    password = input('Please enter your password: ')
    if user in ['Admin','Superuser'] or password == "secret":
        print('Access Granted! ')
    else:
        print('Access Denied! ')

print(system_access()) """



# Aufgabe 8
# Schreibe eine Funktion, die überprüft, ob eine gegebene Zahl sowohl größer als 10 als auch kleiner als 20 ist.
#  Verwende dafür bitte den and Operator und einen Input der eine Eingabe entgegen nimmt.
 
""" def range_checker():
    num = int(input('Please enter the number to be checked: '))
    if num > 10 and num < 20:
        print(f'{num} is smaller than 20 and larger than 10')
    else:
        print(f'{num} is either smaller than 10 or larger than 20')
range_checker() """

 
# Aufgabe 9
# Schreibe eine Funktion, die überprüft, ob eine Zahl entweder kleiner als 0 oder
# größer als 100 ist. Verwende dabei den or Operator und einen Input für eine Eingabe
""" def range_checker2():
    num = int(input('Please enter the number to be checked: '))
    if num < 0 or num > 0:
        return True
    else:
        return False

range_checker2() """

""" def range_checker2():
    num = int(input('Please enter the number to be checked: '))
    if num < 0 or num > 100:
        return True
    else:
        return False

print(range_checker2())
  """





# Aufgabe 10 Sonderaufgabe
# Schreibe ein Programm, das ein Passwort von einem Nutzer entgegen nimmt und überprüft
# ob es mindestens 8 Zeichen lang ist und es muss entweder eine Zahl oder ein Sonderzeichen (@, #, $, %) enthalten

""" def password_checker():
    password = input('Pleae enter your password here: ')
    if len(password) < 8:
        print("Password must contain at least 8 charachters. ")
        return False
    has_special_characters = False
    for char in password:
        if char in ["@", "#", "$", "%"] or char.isdigit():
            has_special_characters = True
            
    if has_special_characters == False:
        print('Passowrd must contain at least one special character. ')
        return False
    print ('Password is valid. ')

print(password_checker()) """

#Jacques Lösung

""" def check_password(password):
    if (len(password) > 8 and (
        '@' in password or
        '#' in password or
        '$' in password or
        '%' in password or
        any(char.isdigit() for char in password))):
        print("Das Passwort ist sicher")
    else:
        print("Das Passwort ist nicht lang genug oder es enthält keine Sonderzeichen")
 
 
eingabe = input("Bitte gib dein Passwort ein: ")
check_password(eingabe) """

#Jacques Lösung editiert:
""" def check_password(password):
    if len(password) > 8 and (
        "@" in password or
        "#" in password or
        "$" in password or
        "x" in password or
        '1' in password or
        '2' in password or
        '3' in password or
        '4' in password or
        '5' in password or
        '6' in password or
        '7' in password or
        '8' in password or
        '9' in password or
        '0' in password    
    ):
        print("Das Passwort ist sicher")
    else:
        print("Das Passwort ist nicht lang genug oder es enthält keine Sonderzeichen")

eingabe = input("Bitte gib dein Passwort ein: ")
check_password(eingabe) """