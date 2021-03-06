# libraries
import sys
import pygame

# modules
from settings import Settings
from ship import Ship


# Overall class to manage game assets and behaviour
class AlienInvasion:
    # initialise game and resources
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_width)
        )
        pygame.display.set_caption("Alien Invasion by github.com/adolfolh")

        self.ship = Ship(self)

        # set bg color
        self.bg_color = (230, 230, 230)

    # start main loop for the game
    def run_game(self):
        # watch mouse and keys events
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make the most recently drawn screen visible
            pygame.display.flip()


# make a game instance and run the game
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
