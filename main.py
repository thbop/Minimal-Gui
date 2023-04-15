import pygame
from pygame.locals import *

import mingu as mg
import definitions as df


class App(mg.App):
    def __init__(self):
        pygame.init()
        super().__init__()

        self.containers.add( df.Container( 'test', pygame.Rect(50, 50, 500, 500) ) )
        self.containers.add_element( df.Square( 'test', pygame.Rect(10, 10, 30, 30) ) )
    
    def run(self):
        while self.running:
            self.event_handler()
            
            self.renderer.clear('#1e1a28')

            self.renderer.render()


            self.renderer.update()


if __name__ == '__main__':
    app = App()
    app.run()
