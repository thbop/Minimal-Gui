import pygame
from pygame.locals import *

import mingu as mg


class App(mg.App):
    def __init__(self):
        pygame.init()
        super().__init__()

        self.containers.add(
            mg.Container( 'test', pygame.Rect(50, 50, 500, 500) )
            )
        self.containers.add_element( mg.Element( 'test', pygame.Rect(10, 10, 30, 30) ) )
        
        self.renderer.load_style('style.json')
    
    def run(self):
        while self.running:
            self.event_handler()
            
            self.renderer.clear()

            self.renderer.render()

            self.renderer.update()


if __name__ == '__main__':
    app = App()
    app.run()
