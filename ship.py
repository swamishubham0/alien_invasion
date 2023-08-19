import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.geet_rect()

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new chip at the botton center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        #  Use the Pygame blit() method to draw the image.
        self.screen.blit(self.image, self.rect)