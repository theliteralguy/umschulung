#testchange
import os
import time
import sys
from planet import Planet
from human import Human

class MainMenu:
    BUILDINGS = [
        {"name": "Rathaus", "food_costs": 50, "stone_costs": 1200, "wood_costs": 1200, "gold_costs": 80},
        {"name": "Jägerhütte", "food_costs": 10, "stone_costs": 10, "wood_costs": 200, "gold_costs": 30},
        {"name": "Bauernhof", "food_costs": 20, "stone_costs": 400, "wood_costs": 1200, "gold_costs": 50},
        {"name": "Holzfällerhütte", "food_costs": 10, "stone_costs": 100, "wood_costs": 300, "gold_costs": 25},
        {"name": "Steinbruch", "food_costs": 15, "stone_costs": 100, "wood_costs": 1200, "gold_costs": 25},
        {"name": "Goldmine", "food_costs": 40, "stone_costs": 1500, "wood_costs": 1500, "gold_costs": 30},
    ]

    def __init__(self):
        self.planets = []  # List to store created planets

    def select_planet(self):
        """Allow the user to select a planet."""
        if not self.planets:
            print("No planets available. Please create a planet first.")
            time.sleep(2)
            return None

        print("Available planets:")
        for idx, planet in enumerate(self.planets):
            print(f"{idx + 1}: {planet.name}")
        choice = int(input("Choose a planet: ")) - 1
        if 0 <= choice < len(self.planets):
            return self.planets[choice]
        else:
            print("Invalid choice.")
            time.sleep(2)
            return None

    def create_planet(self):
        """Create a new planet."""
        planet_name = input("Enter the name of the new planet: ")
        new_planet = Planet(planet_name)
        self.planets.append(new_planet)
        print(f"The new planet {planet_name} has been created.")
        time.sleep(2)

    def build_structure(self):
        """Build a structure on a planet."""
        planet = self.select_planet()
        if not planet:
            return

        print("Available structures to build:")
        for idx, building in enumerate(self.BUILDINGS):
            print(f"{idx + 1}: {building['name']} (Costs: Food={building['food_costs']}, "
                  f"Stone={building['stone_costs']}, Wood={building['wood_costs']}, Gold={building['gold_costs']})")
        choice = int(input("Choose a structure to build: ")) - 1
        if 0 <= choice < len(self.BUILDINGS):
            building = self.BUILDINGS[choice]
            planet.build(building)
        else:
            print("Invalid choice.")
            time.sleep(2)

    def create_human(self):
        """Create a human and add them to a planet."""
        planet = self.select_planet()
        if not planet:
            return

        if not planet.has_town_hall:
            print(f"Cannot add a human. Build a Town Hall (Rathaus) on {planet.name} first!")
            time.sleep(2)
            return

        if planet.food < 100:
            print(f"Not enough food on {planet.name} to create a human (requires 100 food).")
            time.sleep(2)
            return

        name = input("Enter the human's name: ")
        age = int(input("Enter the human's age: "))
        profession = input("Enter the human's profession: ")
        new_human = Human(name, age, profession)
        planet.add_human(new_human)
        time.sleep(2)

    def start(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\n1: Create a new planet")
            print("2: Build a structure")
            print("3: Create a human")
            print("4: Exit program")
            print("\nCurrent Planets:")
            for planet in self.planets:
                print(planet)
            print("\n")

            choice = input("Choose an option: ")
            if choice == "1":
                self.create_planet()
            elif choice == "2":
                self.build_structure()
            elif choice == "3":
                self.create_human()
            elif choice == "4":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Try again.")
                time.sleep(2)



if __name__ == "__main__":
    menu = MainMenu()
    menu.start()
