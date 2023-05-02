import pygame, sys
from settings import *
from nivel import Level

class Game:
    def __init__(self):
        
        pygame.init()
        self.pantalla = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption("Link's souls")
        self.reloj = pygame.time.Clock()
        
        self.level = Level ()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.pantalla.fill('black')
            self.level.run()
            pygame.display.update()
            self.reloj.tick(FPS)
           
if __name__ == '__main__':
    game = Game()
    game.run()                    