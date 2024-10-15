# Aufgabe 1
# erstelle mit einer List Comprehension 3 Listen mit einem Leerzeichen in einer Liste mit dem Namen Spielfeld
# gib deine List Comprehension aus
# die Ausgabe sollte so aussehen: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
 
""" spielfeld = [[' ', ' ', ' '] for x in range(1,4)] """
""" print(spielfeld) """
 
# Aufgabe 2
# 2.1 Suche im Internet nach der Methode .join() und erkläre im Detail was diese macht
# ist ein concatentor, der die elemente von einem iterribareren objekt durch ein belibiges zeichen trennt oder zusmaggengefügt.
 
 
# 2.2 Schreibe eine Funktion mit dem Namen zeichne Spielfeld mit einer for Schleife, die jede Liste deiner List Comprehension untereinander ausgibt
# 2.3 Benutze die join Methode, um die Listen mit einem " | " Zeichen miteinander zu verbinden und gebe sie in der Console aus.
# 2.4 füge jeder Liste in einer Reihe einen Boden mit "-" hinzu und gebe dein Spielfeld in der Console aus. (Tipp: 9 Trennstriche sehen gut und symmetrisch aus)
# Dein Ergebnis sollte etwa wie folgt aussehen:
#
#  |   |
#---------
#  |   |
#---------
#  |   |
#---------
 
def zeichne_spielfeld(spielfeld):
        for reihe in spielfeld:
              print(" | ".join(reihe))
              print("---------")
 
 
""" print(zeichne_spielfeld(spielfeld)) """
 
 
# Aufgabe 3
# 3.1 Baue eine Hauptfunktion mit dem Namen starte_spiel(), kopiere deine List Comprehension mit deinem
#     Spielfeld in die Funktion, so das dein Spielfeld bei dem Aufruf der Funktion erstellt wird
# 3.2 Definiere eine Variable mit dem Namen aktueller_spieler => 'X' in deiner Funkion
# 3.3 Baue eine While Schleife, in deiner starte_spiel() Funktion, die bei dem Start der Schleife
#     deine Funktion zeichne_spielfeld aufruft. (TIPP: Vergiss nicht die Parameterübergabe)
# 3.4 Fordere innerhalb deiner While Schleife eine Eingabe an, welche die Zeile mit einer Zahl empfängt und speichere den Wert der
#     Eingabe in der Variable zeile. Dieser Wert wird später auf den Index deines Feldes zugreifen
# 3.5 Fordere innerhalb deiner While Schleife eine weitere Eingabe an, welche die Spalte mit einem Zahlenwert empfängt, die später dem Index der
#     Spalte zugewiesen wird und speichere den Wert der Eingabe in einer Variablen mit dem Namen spalte
#      (TIPP: Aus der Kombination deiner Eingabe ergeben sich später die Indizes und somit die Stelle an der deine Wahl platziert wird)
 
""" def starte_spiel():
    spielfeld = [[' ', ' ', ' '] for x in range(1,4)]
    print(spielfeld)
    aktueller_spieler = 'X'
    while True:
          zeichne_spielfeld(spielfeld)
          zeile = int(input("Wähle eine Zeile: 0, 1 oder 2:  "))
          spalte = int(input("Wähle eine Spalte: 0, 1 oder 2:  "))
          spielfeld[zeile][spalte] = aktueller_spieler
 
   
   
 
 
 
starte_spiel() """
 
 
 
# Aufgabe 4
# Du hast ein 2 Dimensionales Spielfeld gebaut, auf dessen Felder du zugreifen kannst.
# Finde heraus, wie du das Zeichen deines aktuellen Spielers...
# ... auf die Felder der getätigten Eingabe setzen kannst und erweitere deine Funktion...
# ... starte_spiel() mit der Zuweisung X auf die Eingabe des Spielers
 
""" def starte_spiel():
    spielfeld = [[' ', ' ', ' '] for x in range(1,4)]
    print(spielfeld)
    aktueller_spieler = 'X'
    while True:
          zeichne_spielfeld(spielfeld)
          zeile = int(input("Wähle eine Zeile: 0, 1 oder 2:  "))
          spalte = int(input("Wähle eine Spalte: 0, 1 oder 2:  "))
          spielfeld[zeile][spalte] = aktueller_spieler
 
   
   
 
 
 
starte_spiel() """
 
 
 
 
 
 
 
 
# Aufgabe 5
# Wechsle den aktuellen Spieler in deiner While Schleife von "X" auf "O" und falls dieser Spieler schon auf "O" stehen sollte, wechsle ihn wieder zu "X"
# Teste mal aus, ob es schon funktioniert
""" def starte_spiel():
    spielfeld = [[' ', ' ', ' '] for x in range(1,4)]
    print(spielfeld)
    aktueller_spieler = 'X'
    while True:
        zeichne_spielfeld(spielfeld)
        zeile = int(input("Wähle eine Zeile: 0, 1 oder 2:  "))
        spalte = int(input("Wähle eine Spalte: 0, 1 oder 2:  "))
        spielfeld[zeile][spalte] = aktueller_spieler
        if aktueller_spieler == 'X':
             aktueller_spieler = 'O'
        else:
             aktueller_spieler = 'X'
           
starte_spiel() """







# Aufgabe 6
# Atme mal tief durch, trink nen Schluck und wenn du fertig bist, zeige mit einem print Befehl an, welcher Spieler grade bei dem neuen Schleifendurchlauf an
# der Reihe ist.
"""  
def starte_spiel():
    spielfeld = [[' ', ' ', ' '] for x in range(1,4)]
    print(spielfeld)
    aktueller_spieler = 'X'
    while True:
        zeichne_spielfeld(spielfeld)
        print(f'Spiler {aktueller_spieler} ist dran')
        zeile = int(input("Wähle eine Zeile: 1, 2 oder 3:  ")) -1
        spalte = int(input("Wähle eine Spalte: 1, 2 oder 3:  ")) -1
        spielfeld[zeile][spalte] = aktueller_spieler
        if aktueller_spieler == 'X':
             aktueller_spieler = 'O'
        else:
             aktueller_spieler = 'X'
           
starte_spiel() """




# Aufgbe 7
# Begründe warum du die Zahlen 0 - 2 eingeben musst.
 
 
# Aufgabe 8
# Was wäre eine Lösung, wenn du die Zahlen 1 - 3 eingeben möchtest, weil sich diese Eingabe intuitiver anfühlt?
# Welche Problematik tritt auf und wie können wir diese beheben und umsetzen ?
 
 
# Aufgabe 9
# Wenn du es bis hierhin schon geschafft hast, herzlichen Glückwunsch. Jetzt folgen noch mehr Aufgaben. Vielleicht machst du ein kurzes Brainstorming darüber,
# welche Aufgaben das sein könnten.
 

 ####################################################################################################



# Teil 2
 
 
# Aufgabe 1
# Baue eine Funktion, die prüft, ob das Spielfeld voll ist. Falls ja, beende das Spiel.

""" def ist_spielfeld_voll(spielfeld):
    for zeile in spielfeld:
        if ' ' in zeile:
            return False
    return True


def starte_spiel():
    spielfeld = [[' ', ' ', ' '] for x in range(1,4)]
    print(spielfeld)
    aktueller_spieler = 'X'
    while True:
        zeichne_spielfeld(spielfeld)
        print(f'Spiler {aktueller_spieler} ist dran')
        zeile = int(input("Wähle eine Zeile: 1, 2 oder 3:  ")) -1
        spalte = int(input("Wähle eine Spalte: 1, 2 oder 3:  ")) -1
        spielfeld[zeile][spalte] = aktueller_spieler  
        if ist_spielfeld_voll(spielfeld) ==True:
            
            print("Das Spielfeld ist voll. Das Spiel ist vorbei!")
            
            break
        else:
            pass
        # if spielfeld[zeile][spalte] != ' ':
        #     print("Das Feld ist schon belegt. Wähle ein anderes Feld.")
        #     continue
        if aktueller_spieler == 'X':
             aktueller_spieler = 'O'
        else:
             aktueller_spieler = 'X'
    
           
starte_spiel() """




# Aufgabe 1.2
# Überlege wie du das Problem beheben kannst, das dein Spielfeld auch den letzten Spielzug anzeigt.
 
 
""" 
def ist_spielfeld_voll(spielfeld):
    for zeile in spielfeld:
        if ' ' in zeile:
            return False
    return True


def starte_spiel():
    spielfeld = [[' ', ' ', ' '] for x in range(1,4)]
    print(spielfeld)
    aktueller_spieler = 'X'
    while True:
        zeichne_spielfeld(spielfeld)
        print(f'Spiler {aktueller_spieler} ist dran')
        zeile = int(input("Wähle eine Zeile: 1, 2 oder 3:  ")) -1
        spalte = int(input("Wähle eine Spalte: 1, 2 oder 3:  ")) -1
        spielfeld[zeile][spalte] = aktueller_spieler  
        if ist_spielfeld_voll(spielfeld) ==True:
            zeichne_spielfeld(spielfeld)
            print("Das Spielfeld ist voll. Das Spiel ist vorbei!")
            
            break
        else:
            pass
        # if spielfeld[zeile][spalte] != ' ':
        #     print("Das Feld ist schon belegt. Wähle ein anderes Feld.")
        #     continue
        if aktueller_spieler == 'X':
             aktueller_spieler = 'O'
        else:
             aktueller_spieler = 'X'
    
           
starte_spiel()
 """

# Aufgabe 2
# Fast geschafft!!!! Engegner!!! XD
# Aufgabe 2.1
# Baue eine Funktion mit dem Namen ueberpruefe_gewinner(), die bei jedem Spielzug überprüft, ob alle Reihen das jeweilige Zeichen 3 mal enthalten.
# (Tipp: Denke an die Parameter)
# Aufgabe 2.2
# erweitere deine Funktion ueberpruefe_gewinner() mit der gleichen Kontrolle über jede Spalte
# Aufgabe 2.3
# Überprüfe jetzt noch die Diagonalen Felder


""" def ueberpruefe_gewinner(spielfeld, aktueller_spieler):
    # Check Reihe
    for reihe in spielfeld:
        if reihe.count(aktueller_spieler) == 3:
            return True
            
    # Check Spalte
    for spalte in range(3):
        if (spielfeld[0][spalte] == aktueller_spieler and
            spielfeld[1][spalte] == aktueller_spieler and
            spielfeld[2][spalte] == aktueller_spieler):
            return True
            
    # Check diagonals
    if (spielfeld[0][0] == aktueller_spieler and
        spielfeld[1][1] == aktueller_spieler and
        spielfeld[2][2] == aktueller_spieler):
        return True
    if (spielfeld[0][2] == aktueller_spieler and
        spielfeld[1][1] == aktueller_spieler and
        spielfeld[2][0] == aktueller_spieler):
        return True
    
    return False




def ist_spielfeld_voll(spielfeld):
    for zeile in spielfeld:
        if ' ' in zeile:
            return False
    return True




def starte_spiel():
    spielfeld = [[' ', ' ', ' '] for x in range(1,4)]
    aktueller_spieler = 'X'
    while True:
        zeichne_spielfeld(spielfeld)
        print(f'Spiler {aktueller_spieler} ist dran')
        zeile = int(input("Wähle eine Zeile: 1, 2 oder 3:  ")) -1
        spalte = int(input("Wähle eine Spalte: 1, 2 oder 3:  ")) -1
        if zeile not in [0,1,2] or spalte not in [0,1,2]:
            print("Sorry, but you haven't picked a number bw. 1-3. Try again: ")
            continue
        spielfeld[zeile][spalte] = aktueller_spieler  
        if ueberpruefe_gewinner(spielfeld, aktueller_spieler) == True:
            zeichne_spielfeld(spielfeld)
            print("Herzlichen Glückwunsch")
            print(f"Spieler {aktueller_spieler} hat das Spiel gewonnen!!! ")
            break

        if ist_spielfeld_voll(spielfeld) ==True:
            zeichne_spielfeld(spielfeld)
            print("Das Spielfeld ist voll. Das Spiel ist vorbei!")
            
            break
        else:
            pass

        if aktueller_spieler == 'X':
             aktueller_spieler = 'O'
        else:
             aktueller_spieler = 'X'
    
           
starte_spiel()
 """



# Aufgabe 3
# Fange einen Fehler ab, falls ein Spieler etwas anderes als eine Zahl als Eingabe tätigt. Der Spieler soll darauf hin seinen Spielzug wiederholen
# Aufgabe 3.2
# Überprüfe ob die Eingabe in einem Gültigen Feldbereich liegt. Falls ein Feld besetzt sein sollte, gib aus, das der Zug ungültig ist und der Spieler
# soll seinen Spielzug wiederholen.




""" spielfeld = [[' ', ' ', ' '] for x in range(1, 4)]


def zeichne_spielfeld(spielfeld):
    for reihe in spielfeld:
        print(" | ".join(reihe))
        print("---------")


def ueberpruefe_gewinner(spielfeld, aktueller_spieler):
    # Check Reihe
    for reihe in spielfeld:
        if reihe.count(aktueller_spieler) == 3:
            return True

    # Check Spalte
    for spalte in range(3):
        if (spielfeld[0][spalte] == aktueller_spieler and
            spielfeld[1][spalte] == aktueller_spieler and
            spielfeld[2][spalte] == aktueller_spieler):
            return True

    # Check diagonals
    if (spielfeld[0][0] == aktueller_spieler and
        spielfeld[1][1] == aktueller_spieler and
        spielfeld[2][2] == aktueller_spieler):
        return True
    if (spielfeld[0][2] == aktueller_spieler and
        spielfeld[1][1] == aktueller_spieler and
        spielfeld[2][0] == aktueller_spieler):
        return True

    return False


def ist_spielfeld_voll(spielfeld):
    for zeile in spielfeld:
        if ' ' in zeile:
            return False
    return True


def starte_spiel():
    spielfeld = [[' ', ' ', ' '] for x in range(1, 4)]
    aktueller_spieler = 'X'
    while True:
        zeichne_spielfeld(spielfeld)
        print(f'Spieler {aktueller_spieler} ist dran')
        
        # Eingabe und Überprüfung der Zeile
        while True:
            try:
                zeile = int(input("Wähle eine Zeile: 1, 2 oder 3: ")) - 1
                if zeile not in [0, 1, 2]:
                    print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 3 eingeben.")
                    continue
                break
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
        
        # Eingabe und Überprüfung der Spalte
        while True:
            try:
                spalte = int(input("Wähle eine Spalte: 1, 2 oder 3: ")) - 1
                if spalte not in [0, 1, 2]:
                    print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 3 eingeben.")
                    continue
                break
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
        
        # Überprüfen, ob das Feld bereits besetzt ist
        if spielfeld[zeile][spalte] != ' ':
            print("Dieses Feld ist bereits besetzt. Bitte wähle ein anderes Feld.")
            continue
        
        # Zug durchführen
        spielfeld[zeile][spalte] = aktueller_spieler
        
        # Überprüfen, ob der aktuelle Spieler gewonnen hat
        if ueberpruefe_gewinner(spielfeld, aktueller_spieler):
            zeichne_spielfeld(spielfeld)
            print("Herzlichen Glückwunsch")
            print(f"Spieler {aktueller_spieler} hat das Spiel gewonnen!!! ")
            break

        # Überprüfen, ob das Spielfeld voll ist
        if ist_spielfeld_voll(spielfeld):
            zeichne_spielfeld(spielfeld)
            print("Das Spielfeld ist voll. Das Spiel ist vorbei!")
            break

        # Spieler wechseln
        aktueller_spieler = 'O' if aktueller_spieler == 'X' else 'X'


starte_spiel()
 """
