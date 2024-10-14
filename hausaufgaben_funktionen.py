

#Aufgabe 1
def funktion1(name):
    print(f"Hallo, hier ist {name}")

#Rufe funktion1 auf und übergebe ihr einen Namen

#print(funktion1("Aryan"))

#######################################################


#Aufgabe 2
# Rufe funktion2 auf und ergänze sie mit einem sinnvollen parameter der übergeben wird, der berechnet werden kann
def funktion2(a):
    c = a + 10
    print(c)

# funktion2(100)

########################################################

#Aufgabe 3
# schreibe eine Funktion mit dem Namen funktion3, welche die Parameter aus dem Funktionsaufruf empfängt, addiert und ausgibt 
def funktion3(a,b):
    print(a+b)

# funktion3(100, 200)

########################################################


# Aufgabe 4
# schreibe eine Funktion mit dem Namen funktion4, welche einen Rückgabewert ausgibt welcher durch die Variablen a + b berechnet wird

def funktion4(a,b):
    return a + b

lösung = funktion4(90, 44)
# print(lösung)

########################################################

# Aufgabe 5
# 
# 
# schreibe eine Funktion mit dem namen funktion5, welche 2 parameter empfängt. 
# Diese werden wie folgt in der Funktion berechnet: (parameter1 + parameter2) / 2
# Gib dein Ergebnis als Rückgabewert aus

def funktion5(a,b):
    mittelwert = (a+b)/2
    return mittelwert

# funktion5(30,40)

########################################################


#Aufgabe 6 
# 
# Warum funktioniert folgende Funktion nicht ? Begründe es und finde eine Lösung

def ups_das_klappt_nicht(a, b):
    c = a * b
    return c

# ergebnis = ups_das_klappt_nicht()
# print(ergebnis)

# Loesung: Beim aufrufe der Funktion wurden die fehlenden argumente hingefuegt.
def ups_das_klappt_nicht(a, b):
    c = a * b
    return c

ergebnis = ups_das_klappt_nicht(100, 300)
# print(ergebnis)

########################################################


#Aufgabe 7
# Was gibt folgende Funktion aus? Beschreibe was passiert 

def funktion7():
    return 10

x = 100 + funktion7()
print(x)

# loesung:
    # Die Funktion gibt 110 als integer aus.
    # Prozess: Zuerst wird eine Funktion beschrieben. Die Funktion lediglig
    # gibt 10 aus. Dann ausserhalb der Funktion wird x beschrieben. Diese Variable
    # besteht aus ein wert von 100 und die Ergebnisse von der Funktion.




# HIHIHIIHIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII HAAAHAHAHAHAHAAAAAA WUAAAAAHAHAHAHAAHAHAHAHAHAHAH  ;) 