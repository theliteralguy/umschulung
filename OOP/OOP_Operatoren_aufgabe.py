# Aufgabe 1
# Erstelle eine Klasse Rectangle, die ein Rechteck durch die Attribute width und height repräsentiert.
# Überlade den == Operator __eq__, sodass zwei Rechtecke als gleich betrachtet werden, wenn ihre Fläche gleich ist.
# Benutze den __eq__() Operator
 

# Aufgabe 1: Rectangle Class with overloaded equality operator (__eq__)
""" class Rectangle:
    def __init__(self, width, height):
        # Initialize width and height
        self.width = width
        self.height = height

    def area(self):
        # Calculate and return the area of the rectangle
        return self.width * self.height

    def __eq__(self, other):
        # Check if the other object is a Rectangle and compare areas
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return False

# Example for Aufgabe 1
rect1 = Rectangle(4, 5)
rect2 = Rectangle(10, 2)
rect3 = Rectangle(3, 6)

print(rect1 == rect2)  # True, areas are both 20
print(rect1 == rect3)  # False, areas are 20 and 18 """












# AUfgabe 2
# Erstelle eine Klasse Point3D, die einen Punkt im dreidimensionalen Raum repräsentiert mit den Koordinaten x,y,z
# 2.1
# Implementiere die Operatoren + und -, sodass zwei Punkte addiert oder subtrahiert werden können
# 2.2
# implementiere == um zu prüfen ob zwei Punbkte identisch sind
# 2.3
# Implementiere __abs__, sodass die Distanz eines Punktes vom ursprung (0,0,0) mit abs(point) berechnet werden kann
# TIPP: der ABstand ergibt sich aus der Wurzel von x**2 + y**2 + z**2 und verwende das math module von Python
# 2.4
# Überprüfe ob die Übergebenen Objekte der gleichen Klasse Point3D entspricht und führe die Operatoren nur aus, wenn dies zutrifft.
 

# Aufgabe 2: Point3D Class with arithmetic and comparison operators
""" import math

class Point3D:
    def __init__(self, x, y, z):
        # Initialize the coordinates
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # Add two points' coordinates
        if isinstance(other, Point3D):
            return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        # Subtract two points' coordinates
        if isinstance(other, Point3D):
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __eq__(self, other):
        # Compare coordinates for equality
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __abs__(self):
        # Calculate distance from the origin
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __str__(self):
        # Return a readable string representation of the Point3D instance
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

# Example for Aufgabe 2
p1 = Point3D(1, 2, 3)
p2 = Point3D(4, 5, 6)
p3 = Point3D(1, 2, 3)

print(p1 + p2)        # Point3D(5, 7, 9)
print(p2 - p1)        # Point3D(3, 3, 3)
print(p1 == p3)       # True, identical points
print(abs(p1))        # 3.7416573867739413 (distance from origin) """





















 
# Aufgabe 3
# Erstelle eine Klasse mit dem Namen BankAccount
# 3.1
# implementiere ==, < und > für den Vergleich von Kontoständen
# 3.2
# implementiere den += Operator um Einzahlungen zu tätigen
# 3.3
# implementiere den + Operator um zwei Konten zu einem Konto zu fusionieren (mit kombinierten Kontostand)
 
 
""" class BankAccount:
    def __init__(self, balance):
        # Initialize the account balance
        self.balance = balance

    def __eq__(self, other):
        # Compare balances for equality
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return False

    def __lt__(self, other):
        # Compare if this balance is less than another balance
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        return NotImplemented

    def __gt__(self, other):
        # Compare if this balance is greater than another balance
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        return NotImplemented

    def __iadd__(self, amount):
        # Add to balance in-place
        self.balance += amount
        return self

    def __add__(self, other):
        # Combine balances of two accounts
        if isinstance(other, BankAccount):
            return BankAccount(self.balance + other.balance)
        return NotImplemented

# Example for Aufgabe 3
acc1 = BankAccount(300)
acc2 = BankAccount(200)
acc3 = BankAccount(300)

print(acc1 == acc3)  # True
print(acc1 > acc2)   # True
print(acc1 < acc2)   # False

acc1 += 50           # Add 50 to acc1
print(acc1.balance)  # 350

acc4 = acc1 + acc2   # Combine acc1 and acc2
print(acc4.balance)  # 550
 """



















# Aufgabe 4
# Erzeuge eine Klasse mit dem Namen Fläche
# 4.1
# Überlade den * Operator um die angegebene Breite und Höhe mit einer beliebigen Zahl zu multiplizieren
# 4.2
# Implementiere __repr__, um die Fläche in einer lesbaren Form darzustellen



# Aufgabe 4: Fläche Class with multiplication and string representation
""" class Fläche:
    def __init__(self, width, height):
        # Initialize width and height
        self.width = width
        self.height = height

    def __mul__(self, factor):
        # Multiply width and height by a factor
        if isinstance(factor, (int, float)):
            return Fläche(self.width * factor, self.height * factor)
        return NotImplemented

    def __repr__(self):
        # Return a readable representation
        return f"Fläche(width={self.width}, height={self.height})"

# Example for Aufgabe 4
area = Fläche(4, 5)
scaled_area = area * 3

print(area)          # Fläche(width=4, height=5)
print(scaled_area)   # Fläche(width=12, height=15)
 """
