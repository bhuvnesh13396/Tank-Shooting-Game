class Settings():
    """ Class to store all settings for game."""

    def __init__(self):
        """ Initialize game's settings."""
        # Screen settings.
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)

        # Ship speed
        self.ship_speed_factor=1.5
        self.ship_limit=3

        # Bullet settings
        self.bullet_speed_factor=3
        self.bullet_width=400
        self.bullet_height=15        
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3

        # Alien settings
        self.alien_speed_factor=1
        self.fleet_drop_speed=10

        # fleet direction of 1 represents right and -1 maens left.
        self.fleet_direction=1