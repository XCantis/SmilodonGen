class Biome:
    def __init__(self, name, description, wet_length, dry_length):
        self.name = name
        self.description = description
        self.wet_length = wet_length
        self.dry_length = dry_length


RED_SAVANNA = Biome(
    "Red Savanna",
    "Dry red grasslands with scarce trees.",
    14,
    48
)

BARELA_FOREST = Biome(
    "Barela Forest",
    "Dense forests with abundant resources.",
    20,
    20
)

YKUA_TUNDRA = Biome(
    "Ykua Tundra",
    "Frozen harsh tundra biome.",
    14,
    18
)
