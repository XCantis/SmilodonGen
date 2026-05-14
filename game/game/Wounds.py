import random

MINOR_SCARS = [
    "Ear Nick",
    "Face Scratch",
    "Shoulder Scar",
    "Leg Scar"
]

MAJOR_WOUNDS = [
    "Missing Eye",
    "Missing Ear",
    "Limp",
    "Missing Tail",
    "Missing Leg"
]


def give_random_wound(smilodon):
    roll = random.randint(1, 100)

    if roll <= 70:
        scar = random.choice(MINOR_SCARS)
        smilodon.scars.append(scar)

    else:
        wound = random.choice(MAJOR_WOUNDS)
        smilodon.scars.append(wound)

        if wound == "Missing Leg":
            smilodon.role = "Sitter"
