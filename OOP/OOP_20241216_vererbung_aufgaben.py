# Aufgabe 1
# Erstelle eine Klasse Fahrzeug die folgende Instanzattribute und Methoden hat:
# - Instanzattribute: marke, farbe
# - Methode: beschreiben()
# Aufgabe 1.2
# Erstelle eine Subklasse Auto, die von Fahrzeug erbt
# füge das Attribut anzahl_tueren hinzu
# überschreibe die Methode beschreiben() um die Anzahl der Türen anzugeben
# Teste deine Instanzen von Fahrzeug und Instanzen
 









""" # Basisklasse Fahrzeug
class Fahrzeug:
    def __init__(self, marke, farbe):
        # Attribute der Klasse Fahrzeug
        self.marke = marke
        self.farbe = farbe

    def beschreiben(self):
        # Methode, die die Fahrzeugdetails beschreibt
        print(f"Das Fahrzeug ist ein {self.farbe} {self.marke}.")

# Subklasse Auto
class Auto(Fahrzeug):
    def __init__(self, marke, farbe, anzahl_tueren):
        # Aufruf des Konstruktors der Basisklasse
        super().__init__(marke, farbe)
        # Neues Attribut für Auto
        self.anzahl_tueren = anzahl_tueren

    def beschreiben(self):
        # Methode überschreiben, um die Türen anzugeben
        print(f"Das Auto ist ein {self.farbe} {self.marke} mit {self.anzahl_tueren} Türen.")

# Test
fahrzeug = Fahrzeug("Toyota", "rot")
fahrzeug.beschreiben()

auto = Auto("BMW", "blau", 4)
auto.beschreiben()

 """









 
# Aufgabe 2
# Erstelle eine Basisklasse Tier mit den Instanzattributen name und art und einer Methode geraeusch_machen(), die "Das Tier macht ein Geräusch" ausgibt
# Erstelle die Subklassen Hund, Katze, Maus, und Chinchilla
# Der Hund soll die Methode geraeusch_machen() überschreiben und WuffiWuff ausgeben.
# Die Katze soll "Ich bin Tom" ausgeben  mit der Methode geraeusch_machen()
# Die Maus soll "Ich bin Jerry und ärgere Tom" ausgeben mit der Methode geraeusch_machen()
# Das Chinchilla soll ausgeben, was in der Klasse Tier in der Methode geraeusch_machen steht Musst du die Methode geraeusch_machen dafür überschreiben ?
 
# Aufgabe 2.2
# Erstelle eine weitere Methode info() in der Klasse Tier, die als zusätzliche Informationen ide Rasse über das jeweilige Tier ausgibt. Benutze super(), um die Info()
# Methode in den Subklassen zu erweitern
 









 
"""  # Basisklasse Tier
class Tier:
    def __init__(self, name, art):
        # Attribute der Klasse Tier
        self.name = name
        self.art = art

    def geraeusch_machen(self):
        # Standardgeräusch
        print("Das Tier macht ein Geräusch.")

    def info(self):
        # Info über das Tier
        print(f"Name: {self.name}, Art: {self.art}")

# Subklassen
class Hund(Tier):
    def geraeusch_machen(self):
        print("WuffiWuff!")

class Katze(Tier):
    def geraeusch_machen(self):
        print("Ich bin Tom!")

class Maus(Tier):
    def geraeusch_machen(self):
        print("Ich bin Jerry und ärgere Tom!")

class Chinchilla(Tier):
    # Verwendt die Methode aus der Basisklasse, kein Überschreiben nötig
    pass

# Teest
hund = Hund("Rex", "Hund")
hund.geraeusch_machen()
hund.info()

katze = Katze("Tom", "Katze")
katze.geraeusch_machen()
katze.info()

maus = Maus("Jerry", "Maus")
maus.geraeusch_machen()
maus.info()

chinchilla = Chinchilla("Flauschi", "Chinchilla")
chinchilla.geraeusch_machen()
chinchilla.info() """











# Aufgabe 3
# Erstelle eine Klasse mit dem Namen Mitarbeiter und den Instanzattributen name und gehalt.
# Füge eine Methode arbeiten() hinzu die "Mitarbeiter arbeitet ausgibt"
# 3.2
# Erstelle eine Subklasse Manager die zusätzlich ein Attribut teamgroesse hat.
# Überschreibe die Methode arbeiten() in der Subklasse, sodass sie zusätzlich angibt, dass der Manager das Team leitet
# Verwende dabei super()
 
 








"""  # Basisklasse Mitarbeiter
class Mitarbeiter:
    def __init__(self, name, gehalt):
        # Attribute für Mitarbeiter
        self.name = name
        self.gehalt = gehalt

    def arbeiten(self):
        # Standardarbeitsmethode
        print(f"{self.name} arbeitet.")

# Subklasse Manager
class Manager(Mitarbeiter):
    def __init__(self, name, gehalt, teamgroesse):
        # Attribute erben und erweitern
        super().__init__(name, gehalt)
        self.teamgroesse = teamgroesse

    def arbeiten(self):
        # Methode überschreiben, super() nutzen
        super().arbeiten()
        print(f"{self.name} leitet ein Team von {self.teamgroesse} Personen.")

# Test
mitarbeiter = Mitarbeiter("Alice", 3000)
mitarbeiter.arbeiten()

manager = Manager("Bob", 5000, 5)
manager.arbeiten() """











# Aufgabe 4
# Erstelle die Klasse Läufer und Schwimmer, jede mit einer Methode, die ihre Fähigkeit beschreibt (laufen und schwimmen)
# Erstelle eine Klasse Triathlet, die von beiden Klassen erbt und alle Fähigkeiten vereint.
# Teste den Zugriff auf die geerbeten Methoden
 
 







"""  # Klassen Läufer und Schwimmer
class Läufer:
    def laufen(self):
        print("Ich kann laufen.")

class Schwimmer:
    def schwimmen(self):
        print("Ich kann schwimmen.")
# Klasse Triathlet, die von beiden erbt
class Triathlet(Läufer, Schwimmer):
    pass

# Test
triathlet = Triathlet()
triathlet.laufen()
triathlet.schwimmen() """









# Aufgabe 5
# importiere ABC (Abstract Base Class) und abstractmethod aus dem Modul abc
# Erstelle eine abstrakte Klasse Figur mit einer abstrakten Methode flaeche() und einer normalen Methode beschreibung(),
# die "Das ist eine geometrische Figur" ausgibt
# 5.2
# Erstelle die Subklassen Kreis und Rechteck, die flaeche() implementieren und die jeweilige Fläche des Objekts berechnen.
# Gib die berechnete Fläche und die Beschreibung aus
 
 








""" 
from abc import ABC, abstractmethod

# Abstrakte Klasse Figur
class Figur(ABC):
    @abstractmethod
    def flaeche(self):
        # Abstrakte Methode
        pass

    def beschreibung(self):
        print("Das ist eine geometrische Figur.")

# Subklasse Kreis
class Kreis(Figur):
    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        return 3.14 * self.radius**2

# Subklasse Rechteck
class Rechteck(Figur):
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

    def flaeche(self):
        return self.breite * self.hoehe

# Test
kreis = Kreis(5)
kreis.beschreibung()
print("Fläche des Kreises:", kreis.flaeche())

rechteck = Rechteck(4, 6)
rechteck.beschreibung()
print("Fläche des Rechtecks:", rechteck.flaeche()) """











# Aufgabe 6
# Erstelle eine Basisklasse Bankkonto mit Kontonummer und kontostand als Attribute
# Erstelle darin die Methoden einzahlen(betrag) und auszahlen(betrag)
# 6.2
# Erstelle die Subklasse Sparkonto mit einem Attribut zins_satz und einer Methode zinsen_hinzufügen
# Erstelle die Subklasse Girokono, welches einen Dispo-Kreditrahmen besitzt und auszahlen(betrag) entsprechend anpasst
# Simuliere mit diesen Klassen eine Bank, indem du mehrere Konten erstellst und Transaktionen durchführst.









""" # Basisklasse Bankkonto
class Bankkonto:
    def __init__(self, kontonummer, kontostand):
        self.kontonummer = kontonummer
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        self.kontostand += betrag
        print(f"{betrag} eingezahlt. Neuer Kontostand: {self.kontostand}")

    def auszahlen(self, betrag):
        if self.kontostand >= betrag:
            self.kontostand -= betrag
            print(f"{betrag} ausgezahlt. Neuer Kontostand: {self.kontostand}")
        else:
            print("Nicht genug Guthaben.")

# Subklasse Sparkonto
class Sparkonto(Bankkonto):
    def __init__(self, kontonummer, kontostand, zins_satz):
        super().__init__(kontonummer, kontostand)
        self.zins_satz = zins_satz

    def zinsen_hinzufügen(self):
        zinsen = self.kontostand * self.zins_satz / 100
        self.kontostand += zinsen
        print(f"Zinsen von {zinsen} hinzugefügt. Neuer Kontostand: {self.kontostand}")

# Subklasse Girokonto
class Girokonto(Bankkonto):
    def __init__(self, kontonummer, kontostand, dispo):
        super().__init__(kontonummer, kontostand)
        self.dispo = dispo

    def auszahlen(self, betrag):
        if self.kontostand + self.dispo >= betrag:
            self.kontostand -= betrag
            print(f"{betrag} ausgezahlt. Neuer Kontostand: {self.kontostand}")
        else:
            print("Dispo-Kreditrahmen überschritten.")

# Test
sparkonto = Sparkonto("12345", 1000, 2)
sparkonto.einzahlen(200)
sparkonto.zinsen_hinzufügen()

girokonto = Girokonto("54321", 500, 300)
girokonto.auszahlen(600)
girokonto.auszahlen(300) """
