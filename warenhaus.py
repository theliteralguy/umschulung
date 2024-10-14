# Wir haben ein Warenhaus das Schraubenpakete verkauft, wir wollen das der Nutzer zwischen 3 Paketen auswählen darf

from auswahl_kontrolle import kontrolliere_auswahl
from variablen import *



print(begruessung)

try:
    auswahl = int(input(f"""Bitte wählen Sie aus unseren 3 möglichen Schraubenpaketen aus: 
                1 für das kleine Schraubenpaket {preis_kleines_schraubenpaket:.2f} €
                2 für das mittlere Schraubenpaket {preis_mittleres_schraubenpaket:.2f} €    
                3 für das große Schraubenpaket {preis_grosses_schraubenpaket:.2f} €    
            """))
except ValueError:
    print("Bitte geben Sie nur Zahlen ein!", ValueError)
    exit()


kontrolliere_auswahl(auswahl)
