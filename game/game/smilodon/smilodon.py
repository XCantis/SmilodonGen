import random
from game.constants import *

class Smilodon:
    def __init__(self, name, sex, age=0):
        self.name = name
        self.sex = sex
        self.age = age

        self.role = "Kit"

        self.coat_color = random.choice(COAT_COLORS)
        self.marking = random.choice(MARKINGS)
        self.coat_type = random.choice(COAT_TYPES)
        self.mane = random.choice(MANES)

        self.mutation = random.choice(MUTATIONS) if random.randint(1, 100) <= 10 else None

        self.health = 100
        self.alive = True

        self.scars = []
        self.mate = None
        self.children = []
        self.parents = []

        self.mentor = None
        self.apprentices = []

    def age_up(self):
        self.age += 1

        self.update_role_by_age()
        self.check_elder_death()

    def update_role_by_age(self):
        if self.age <= 7:
            self.role = "Kit"

        elif 8 <= self.age <= 16:
            self.role = "Juvenile"

        elif self.role in ["Kit", "Juvenile"]:
            self.role = random.choice([
                "Guard",
                "Hunter",
                "Sitter",
                "Mentor"
            ])

    def check_elder_death(self):
        death_chance = 0

        if self.age >= 30:
            death_chance += 10

        if self.mutation in ["Blind", "Deaf"]:
            death_chance += 5

        if random.randint(1, 100) <= death_chance:
            self.alive = False
