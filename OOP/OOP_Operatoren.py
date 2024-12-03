class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __eq__(self, value: object) -> bool:
        return self.x == value.x and self.y == value.y
 
    def addittion_of_other_instance(self, other):
        return self.x + other.y
 
 
# Jeder Vector ist ein eigenes Objekt ^^
v1 = Vector(1,1)
v2 = Vector(2,2)
v3 = Vector(1,1)
 
 
print(v1 == v3) # kurz und knackig wie ne Wurst
print(v1.addittion_of_other_instance(v2)) # Umständlicher und weniger elegant wie ein Elefant
 