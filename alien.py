import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen: pygame.Surface = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230,230)
        self.ship = Ship(self.screen)

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()
            
            
    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()