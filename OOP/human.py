class Human:
    def __init__(self, name, age, profession):
        self.name = name  # Name of the human
        self.age = age  # Age of the human
        self.profession = profession  # Profession of the human

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Profession: {self.profession}"
