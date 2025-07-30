class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Start at medium hunger
        self.energy = 5  # Start at medium energy
        self.happiness = 5  # Start at medium happiness
        self.tricks = []  # List to store learned tricks

    def eat(self):
        """Reduces hunger by 3 points and increases happiness by 1."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten and feels better!")

    def sleep(self):
        """Increases energy by 5 points."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} has slept well!")

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1."""
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} has played and is having fun!")

    def get_status(self):
        """Prints the current status of the pet."""
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print("\nKnown Tricks:")
            for trick in self.tricks:
                print(f"- {trick}")

    def train(self, trick):
        """Teaches the pet a new trick."""
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} has learned a new trick: {trick}")
        else:
            print(f"{self.name} already knows this trick!")

    def show_tricks(self):
        """Shows all tricks the pet knows."""
        if self.tricks:
            print(f"\n{self.name} knows these tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet!")
