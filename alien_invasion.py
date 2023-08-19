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
            self._check_events()
            self.ship.update()
            self._update_screen()
            # Update framerate (60 Frames per second)
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        # Draw the ship
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ =='__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()