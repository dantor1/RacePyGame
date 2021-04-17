import pygame, sys
from pygame.locals import *
import random

class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0): # aquí le decimos que el disfraz por defecto es turtle
        ixCustome = random.randint(0, 4) # Esto genera un valor al azar entre 0 y 4
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome])) # Voy a cargar la imagen (disfraz) al azar, porque ix va al azar
        self.position = [x, y] # Esto tiene que ser mutable
        self.name = ""
        
class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480)) # La pantalla lo creamos como un atributo privado
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de Bichos")
        
        self.runner = Runner(320, 240)
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Esto es el evento de tipo QUIT (acabar). Es una constante de PyGame.
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.runner.position[1] -= 5 # En Pygame la Y cuando subes, tienes que restar
                    elif event.key == K_DOWN:
                        self.runner.position[1] += 5 # En Pygame la Y cuando bajas, tienes que sumar
                    elif event.key == K_LEFT:
                        self.runner.position[0] -= 5
                    elif event.key == K_RIGHT:
                        self.runner.position[0] += 5
                    else:
                        pass
                    
            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(self.runner.custome, self.runner.position)
                    
            pygame.display.flip()
            
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.start()
