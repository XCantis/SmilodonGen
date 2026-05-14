class Clan:
    def __init__(self, name, biome):
        self.name = name
        self.biome = biome

        self.members = []
        self.age = 0
        self.health = 100

        self.king = None
        self.queen = None

        self.dynasty = []

    def add_member(self, smilodon):
        self.members.append(smilodon)

    def remove_dead(self):
        self.members = [m for m in self.members if m.alive]

    def age_clan(self):
        self.age += 1

        for member in self.members:
            member.age_up()

        self.remove_dead()
        self.update_health()

    def update_health(self):
        total = 0

        for member in self.members:
            total += member.health

        if self.members:
            self.health = total / len(self.members)
