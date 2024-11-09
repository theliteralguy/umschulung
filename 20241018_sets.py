#Aufgaben Sets
 
# Aufgabe 1
# Füge mit der `add()` Methode ein weiteres Tier, z.B. "Elefant", hinzu
tiere = {"Hund", "Katze", "Vogel"}
tiere.add('Elefant')
#print(tiere)
 
 
# Aufgabe 2
# Entferne die Zahl 3 mit der `remove()` Methode
zahlen = {1, 2, 3, 4, 5}
zahlen.remove(3)
# print(zahlen)
 
 
# Aufgabe 3
# Verwende `discard()` für die Farbe "blau" und gib dein set aus
farben = {"rot", "gelb", "grün", "schwarz", "weiß"}
farben.discard("blau")
#print(farben)
 
 
# Aufgabe 4
# Verwende `union()`, um ein Set mit allen Früchten und Gemüsen zu erstellen und gib es aus
obst = {"Apfel", "Banane", "Kirsche", "Pflaume", "Mango"}
gemüse = {"Karotte", "Tomate", "Salat", "Brokkoli", "Kartoffel"}
# gemischter_set = obst.union(gemüse)
# gemischter_set = obst | gemüse
# print(gemischter_set)
 
 
# Aufgabe 5
# Verwende `intersection()` für die gemeinsamen Städte heruaszufiltern und gib sie aus
staedte = {"Berlin", "Hamburg", "München", "Köln", "Stuttgart"}
staedte2 = {"München", "Düsseldorf", "Berlin", "Leipzig"}

# gemeinsamen_städte = staedte.intersection(staedte2)
# gemeinsamen_städte = staedte & staedte2 
# print(gemeinsamen_städte)



 
# Aufgabe 6
# Verwende `difference()`, um die Sportarten zu finden, die nur in deinem Lieblings-Set sind
sportarten_studio1 = {"Fußball", "Basketball", "Tennis"}
sportarten_studio2 = {"Tennis", "Golf", "Schwimmen"}

lieblings_set = sportarten_studio1.difference(sportarten_studio2)
print(lieblings_set)
 


# Aufgabe 7
# Finde die Tiere, die nur in einem der beiden Gehege vorkommen (nicht in beiden). Finde heraus welche Funktion du verwenden könntest und gib dein Ergebnis aus
gehege_1 = {"Löwe", "Tiger", "Elefant", "Zebra"}
gehege_2 = {"Tiger", "Elefant", "Giraffe", "Nashorn"}

# einzigartige_tiere = gehege_1.symmetric_difference(gehege_2)
# einzigartige_tiere = gehege_1 ^ gehege_2
# print(einzigartige_tiere)

 