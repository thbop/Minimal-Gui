import pygame
from pygame.locals import *

import mingu as mg


class App(mg.App):
    def __init__(self):
        pygame.init()
        super().__init__()
    
    def run(self):

        while self.running:
            self.event_handler()
            
            self.window.fill((0, 0, 0))

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
