# SCheribe sie eine prozdur in pseducode die alle elmenete in einer liste nach rechts verschiebt.
# das letzte ellment soll das ersel element ewerden.
#note: Pseudocode ist eine für den Menschen verständlich sprache, wleche unbhnig von der Syntax Programmiersprache ist
# und dient der verständlicheren Erkläarung von Abläufen eines Programms.
zahlen = [
    10,
    20,
    30,
    40,
    50,
]

liste = [
    "Oliver",
    "Patrick",
    "Anas",
    "Fatjon",
    "Nico",
]

def rechts_verschieben(liste):
    letzter_wert = liste[-1]
    rest_werte = liste[0:-1]
    neue_liste = [letzter_wert]
    neue_liste.extend(rest_werte)
    print(neue_liste)

rechts_verschieben(liste)