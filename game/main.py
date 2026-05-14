import pygame
from game.game_manager import GameManager

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SmilodenGen")

clock = pygame.time.Clock()

manager = GameManager()

running = True

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.handle_event(event)

    manager.update(dt)
    manager.draw(screen)

    pygame.display.flip()

pygame.quit()
