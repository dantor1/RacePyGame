import pygame, sys
import random


class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0): # aquí le decimos que el disfraz por defecto es turtle
        ixCustome = random.randint(0, 4) # Esto genera un valor al azar entre 0 y 4
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome])) # Voy a cargar la imagen (disfraz) al azar, porque ix va al azar
        self.position = [x, y] # Esto tiene que ser mutable
        self.name = ""
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
        #pygame.time.delay(5)
        

class Game():
    runners = [] # Esto es un array
    __posY = (160, 200, 240, 280)
    __names = ("Speedy", "Lucera", "Alonso", "Torcuata")
    __startLine = -5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480)) # La pantalla lo creamos como un atributo privado
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de Bichos")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i]) # Esto me creará un runner, una instancia de Runner y hará las 3 cosas de def__init__ . El corredor lo creamos en cada ciclo
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)

    def close(self):
        pygame.quit()
        sys.exit()
                
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Esto es el evento de tipo QUIT (acabar). Es una constante de PyGame.
                    gameOver = True
            
            for activeRunner in self.runners: # solo voy a usar esta variable en el contexto del bucle # Comprobamos eventos
                activeRunner.avanzar() # comprobamos eventos
                if activeRunner.position[0] >= self.__finishLine: # comprobamos eventos
                    print("{} ha ganado".format(activeRunner.name)) # comprobamos eventos
                    gameOver = True # comprobamos eventos
            
            fpsClock = pygame.time.Clock()
            FPS = 80
            fpsClock.tick(FPS)
         

            self.__screen.blit(self.__background, (0, 0)) # Método optimizado para videojuegos. Nos pinta a toda velocidad el fondo
              
            for runner in self.runners: # Pintamos la pantalla
                self.__screen.blit(runner.custome, runner.position) # Pintamos la pantalla
            
            pygame.display.flip() # Pintamos la pantalla
            
        while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                
            

if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()
    
