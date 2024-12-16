# einfache Vererbung
 
class Tier:
    def __init__(self, name):
        self.name = name
 
    def macht_geräusch(self):
        return "Blubbiblub"
   
 
class Hund(Tier):
    def __init__(self, name, alter):
        super().__init__(name)
        self.alter = alter
 
    def geräusch_machen(self):
        print(super().macht_geräusch())
        return f"Der Hund {self.name} macht Wuff wuff!"
   
 
""" hund1 = Hund("Sparki", 7)
print(hund1.geräusch_machen()) """
 
# Mehrfachvererbung
 
class Fliege:
    def fliegen(self):
        print("Ich kann fliegen")
 
 
class Fisch(Tier):
    def schwimmen(self):
        print("Ich kann schwimmen")
 
 
class Flugfisch(Fliege, Fisch):
    pass
 
 
flugfisch = Flugfisch("Flippy")
flugfisch.fliegen()
flugfisch.schwimmen()
print(flugfisch.name)
 