import pygame

class Ship():
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        

        self.image = pygame.transform.scale(pygame.image.load('images/ship.bmp'), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        