class Settings:
    """A class too store all settings for Alien Invasion game"""

    def __init__(self) :
        """Initialize the game's settings."""
        #Screen Settings
        self.screen_width = 1200
        self.scree_height = 800
        self.bg_color = (230,230,230)
        
        # URL for images
        self.imageSource = 'https://opengameart.org/'