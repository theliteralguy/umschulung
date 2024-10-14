# Die Multiplikation der ganzen Zahlen x und y kann auch als x maliges addieren
# der Zahl y gelöst werden. Erstelle eine rekursive Funktion für diese Operation

def rekursive_multiplikation(x,y):

    if x == 0:
        return 0

    return y + rekursive_multiplikation(x-1, y)



print(rekursive_multiplikation(10, 4))