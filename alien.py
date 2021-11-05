import pygame
import pathlib
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' A class to represent a single alien of the fleet '''
    def __init__(self, ai_settings, screen):
        ''' Initialize alien and set starting position '''
        super(Alien, self).__init__()
        self.screen = screen 
        self.ai_settings = ai_settings

        # Load alien image and its rect attribute
        path = str(pathlib.Path(__file__).parent.resolve()) + '\images\_alien.bmp'
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

        # Star each new alien at top left corner 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien exact position
        self.x = float(self.rect.x)
    # end def

    def blitme(self):
        ''' Draw alien at its currente position '''
        self.screen.blit(self.image, self.rect)
    # end def
# end class