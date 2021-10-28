import pygame


class Ship:

    def __init__(self, ai_game):
        """Inicjalizacja statku i jego położenie początkowe"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #wczytanie obrazu statku i pobranie jego prostokąta
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom
        #położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #uaktualnienie obiektu rect na podstawie wartości self.x
        self.rect.x = self.x

    def blitme(self):
        """Wyświetlenie statku w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)