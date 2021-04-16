import pygame, sys


class Game():
    runners = []
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480)) # La pantalla lo creamos como un atributo privado
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de Bichos")
        
        
    def competir(self):    
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Esto es el evento de tipo QUIT (acabar). Es una constante de PyGame.
                    gameOver = True
    

            self.__screen.blit(self.__background, (0, 0)) # metodo optimizado para videojuegos. Nos pinta a toda velocidad el fondo)
            
            pygame.display.flip()
            
        pygame.quit() # Nos cierra PyGame
        sys.exit() # Nos cierra Python
            
            
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()
    
