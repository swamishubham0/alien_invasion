class Settings:
    """A class too store all settings for Alien Invasion game"""

    def __init__(self) :
        """Initialize the game's settings."""
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 70

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


        # URL for images
        self.imageSource = 'https://opengameart.org/'
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 5
        self.bullet_speed = 5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale