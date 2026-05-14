import pygame

from game.clan.clan import Clan
from game.world.biome import RED_SAVANNA
from game.smilodon.smilodon import Smilodon
from game.event_system import EventSystem
from game.save_manager import SaveManager

class GameManager:
    def __init__(self):

        self.font = pygame.font.SysFont("times new roman", 22)

        self.clan = Clan("Sunfang Pride", RED_SAVANNA)

        starter_queen = Smilodon("Fawn'Saber", "Female", 24)
        starter_king = Smilodon("Quick'Mane", "Male", 25)

        starter_queen.role = "Queen"
        starter_king.role = "King"

        self.clan.queen = starter_queen
        self.clan.king = starter_king

        self.clan.add_member(starter_queen)
        self.clan.add_member(starter_king)

        self.turns = 0
        self.current_event = "The pride settles into camp."

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                self.next_dawn()

            if event.key == pygame.K_s:
                SaveManager.save_game(self.clan)

    def next_dawn(self):

        self.turns += 1

        self.clan.age_clan()

        self.current_event = EventSystem.generate_event()

        if self.turns % 5 == 0:
            SaveManager.save_game(self.clan)

    def update(self, dt):
