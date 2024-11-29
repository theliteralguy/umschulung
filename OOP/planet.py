import random

class Planet:
    def __init__(self, name):
        self.name = name  # Name of the planet
        self.population = 0  # Initial population
        self.food = random.randint(300, 2000)  # Random food supply
        self.wood = random.randint(1500, 2000)  # Random wood resource
        self.stone = random.randint(1500, 2000)  # Random stone resource
        self.gold = 200  # Fixed gold value
        self.humans = []  # List to store humans on the planet
        self.buildings = []  # List of constructed buildings
        self.has_town_hall = False  # Tracks if the town hall is built

    def can_afford(self, building):
        """Check if the planet has enough resources to build a structure."""
        return (self.food >= building["food_costs"] and
                self.wood >= building["wood_costs"] and
                self.stone >= building["stone_costs"] and
                self.gold >= building["gold_costs"])

    def build(self, building):
        """Deduct resources and build the structure."""
        if self.can_afford(building):
            self.food -= building["food_costs"]
            self.wood -= building["wood_costs"]
            self.stone -= building["stone_costs"]
            self.gold -= building["gold_costs"]
            self.buildings.append(building["name"])
            if building["name"] == "Rathaus":
                self.has_town_hall = True
            print(f"{building['name']} has been built on {self.name}.")
        else:
            print(f"Not enough resources to build {building['name']}.")

    def add_human(self, human):
        """Add a human if the town hall is built and resources allow."""
        if not self.has_town_hall:
            print(f"Cannot add {human.name}. Build a town hall first!")
            return
        if self.food >= 100:
            self.humans.append(human)
            self.population += 1
            self.food -= 100  # Consume 100 food for adding a human
            print(f"{human.name} has been added to {self.name}.")
        else:
            print(f"Not enough food to add {human.name}.")

    def __str__(self):
        return (f"Planet Name: {self.name}, Population: {self.population}, Food: {self.food}\n"
                f"Wood: {self.wood}, Stone: {self.stone}, Gold: {self.gold}\n"
                f"Buildings: {', '.join(self.buildings)}, Humans: {len(self.humans)}")
