import sys
import pygame

# Overall class to manage game assets and behaviour
class AlienInvasion:
    # initialise game and resources
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion by adolfolh")

    # start main loop for the game
    def run_game(self):
        # watch mouse and keys events
        while True:
            for event in pygame.event.get():
                if event.type() == pygame.QUIT:
                    sys.exit()

        # make the most recently drawn screen visible
        pygame.display.flip()