from variablen import *


def kontrolliere_auswahl(auswahl):
    if auswahl == 1:
        gesamtpreis = preis_kleines_schraubenpaket + versandkosten
        preis_kleines_schraubenpaket_str = str(f"{preis_kleines_schraubenpaket:.2f}").replace(".",",")
        gesmatpreis_str = str(f"{gesamtpreis:.2f}").replace(".",",")
        print(f"""Sie haben sich für das kleine Schraubenpaket entschieden für {preis_kleines_schraubenpaket_str} €
                  Ihr gesamter Einkaufswert inkl. Versankosten beträgt: {gesmatpreis_str} €
              """)
    elif auswahl == 2:
        gesamtpreis = preis_mittleres_schraubenpaket +versandkosten
        gesmatpreis_str = str(f"{gesamtpreis:.2f}").replace(".",",")
        print(f"""Sie haben sich für das mittlere Schraubenpaket entschieden für {preis_mittleres_schraubenpaket:.2f} €
              Ihr gesamter Einkaufswert inkl. Versankosten beträgt: {gesmatpreis_str} €
              """)
    elif auswahl == 3:
        gesamtpreis = preis_grosses_schraubenpaket - rabatt
        gesamtpreis_str = str(f"{gesamtpreis:.2f}").replace(".", ",")
        rabatt_str = str(f"{rabatt:.2f}").replace(".",",")
        print(f"""Sie haben sich für das große Schraubenpaket entschieden für {preis_grosses_schraubenpaket:.2f} €
                Ihr gesamter Einkaufswert abzüglich {rabatt_str} € Rabatt beträgt {gesamtpreis_str} €
              """)
    else:
        print("Ihre Eingabe ist ungültig!!!")



