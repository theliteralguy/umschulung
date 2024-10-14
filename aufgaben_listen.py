# 1. Erstelle 5 Listen, wobei jeweils eine Liste nur strings, eine andere nur integer, eine weitere nur floats beinhaltet. Was in den anderen beiden steht ist egal
lst_str = ['a','b','c','d','e']
lst_int = [0,8,3,88,5]
lst_floats = [1.5,3.4,5.5,6.4,5.6]
lst_namens = ['Aryan','Jack','John','Jose','Athena']
lst_mix = [123, 22.33, 'Alex']


# 2. Hänge 3 Werte an deine 1. Liste an
# print (lst_str.append('F'))
# print (lst_str.append('G'))
# print (lst_str.append('H'))
# print (lst_str)


# 3. Nimm deine 2. Liste und hänge sie an deine erste Liste, lass sie dir danach ausgeben
# lst_str.extend(lst_int)
# print(lst_str)

# 4. Füge deinen Namen und 2 weitere Namen deiner Klassenkameraden deiner 1 Liste an Position 3, 4 und 6 hinzu
# lst_str.insert(3, 'Aryan')
# lst_str.insert(4, 'Oliver')
# lst_str.insert(6, 'Nils')
# print(lst_str)

# 5. Entferne einen Wert mit der Methode remove aus deiner 4. Liste. begründe warum der Wert trotzdem noch in der Liste vorhanden sein könnte.
# lst_namens.remove('Aryan')
# print(lst_namens)
# Erklärung: Der Wert trotzdem noch in der Liste vorhanden sein könnte, weil die remove Methode betrachtet nur das erste Instanz
# von dem eingegebnen Parameter


# 6. Werfe das letzte Element aus deiner 1. Liste raus.
# lst_str.pop()
# print(lst_str)



# 7. Lösche den Inhalt aus deiner 5. Liste und gib sie aus, um zu prüfen ob die Liste wirklich leer ist
# lst_mix.clear()
# print(lst_mix)



# 8. Sortiere deine 2 Liste absteigend und gib sie aus
# lst_int.sort()
# print(lst_int)


# 9. Kopiere deine 4. Liste und lasse sie dir ausgeben mit dem Satz: "Das ist die Kopie von Liste 4"
# kopierte_liste = lst_namens.copy()
# print(f"Das ist die Kopie von Liste 4: {kopierte_liste}")



# 10. Füge einen Eintrag in deiner Kopie hinzu, lasse dir danach die Kopie und die original Liste ausgeben und schau ob das ändern der Kopie die echte Liste verändert hat.
# kopierte_liste = lst_namens.copy()
# kopierte_liste.append('Joseph')
# print(f"Das ist die Orginal von Liste 4: {lst_namens}")
# print(f"Das ist die Kopie von Liste 4: {kopierte_liste}")


# Zähle wie oft der Name Alex in deiner 1. Liste vorhanden ist
# print(lst_str.count('a'))


# 12. Zähle wie oft dein Name in der 1. Liste vorhanden ist
# print(lst_str.count('Aryan'))

# 13. Prüfe wie oft die Zahl 3 in deiner 2. Liste ist
# print(lst_int.count(88))

# 14. Sortiere die 3 Liste aufsteigend, weil diese sich sonst ausgeschlossen fühlt >;)
# lst_floats.sort()
# print(lst_floats)