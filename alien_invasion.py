import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        # Setting clock for framerate
        self.clock = pygame.time.Clock()
        
        # Settings
        self.settings = Settings()

        # Create a display window on whcih we will draw all the games graphical elements
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.scree_height))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color
        self.bg_color = self.settings.bg_color

        # Create ship
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # Draw the ship
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            # Update framerate (60 Frames per second)
            self.clock.tick(60)


if __name__ =='__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()