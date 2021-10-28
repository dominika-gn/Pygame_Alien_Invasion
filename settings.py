class Settings:
    """ Klasa przeznaczona do przechowywania wszystkich ustawień gry"""

    def __init__(self):

        #ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 150, 200)

        self.ship_speed = 1.5