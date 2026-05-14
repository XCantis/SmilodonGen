import random

EVENTS = [
    "A hunt was successful.",
    "A rival pride was spotted nearby.",
    "A juvenile completed training.",
    "Heavy rains flooded hunting grounds.",
    "A kit was born healthy.",
    "A guard returned with injuries.",
]

class EventSystem:

    @staticmethod
    def generate_event():
        return random.choice(EVENTS)
