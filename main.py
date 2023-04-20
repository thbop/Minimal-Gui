import pygame
from pygame.locals import *

import mingu as mg
import definitions as df


class App(mg.App):
    def __init__(self):
        pygame.init()
        super().__init__()

        self.containers.add( df.Container( 'side-panel', pygame.Rect(5, 5, (self.width/4)-10, self.height-10) ) )
        self.containers.add_element( df.Button( 'side-panel', pygame.Rect(10, 10, 250, 20) ) )
        self.containers.add_element( df.Text( 'side-panel', pygame.Rect(16, 14, 18, 0), 'Hello World' ) )

        self.containers.add( df.Container( 'main-panel', pygame.Rect((self.width/4), 5, (self.width/4)*3-5, self.height-10) ) )
    
    def run(self):
        while self.running:
            self.event_handler()
            
            self.renderer.clear('#1e1a28')

            self.renderer.render()


            self.renderer.update()


if __name__ == '__main__':
    app = App()
    app.run()
