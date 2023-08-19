class Settings:
    """A class too store all settings for Alien Invasion game"""

    def __init__(self) :
        """Initialize the game's settings."""
        #Screen Settings
        self.screen_width = 1200
        self.scree_height = 800
        self.bg_color = (230,230,230)
        
        #Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # URL for images
        self.imageSource = 'https://opengameart.org/'