product = {
    "id": "12345",
    "name": "Holzschrauben",
    "amount": 1000,
    "price": 19.99,
}
 
product_name = product["name"]
 
product["name"] = "Metallschrauben" # Ändert den Value von einem Key und fügt ihn hinzu wenn dieser nicht existiert
 
""" del product["price"] """ # Löscht ein Paar aus dem Dicitonary
""" test = product.pop("price") """ # Löscht das Paar aus dem Dictionary und gibt es zurück
 
product.get("name") # gibt den Wert eines Schlüssels zurück, wenn der Schlüssel nicht existiert wirft es None zurück anstatt einen Key Error
 
product.keys() # gibt eine Liste aller Schlüssel im Dictionary zurück
 
product.values() # Gibt alle Werte eines Dicitonaries zurück
 
product.items() # gibt eine Liste mit Tupeln von Schlüssel Wert Paaren zurück
 
product.update({"prices":3.99}) # fügt neue Paare hinzu oder aktualisiert vorhandene Einträge
product.update({"size":"38x18"}) # fügt neue Paare hinzu oder aktualisiert vorhandene Einträge
 
""" product.clear()  """ # löscht alle Key Value Paare in einem Dictionary
 
kopie = product.copy() # Kopiert ein Dictionary
 
test = product.popitem() # Wirft den letzten Eintrag wieder aus dem Dictionary
 
print(test)