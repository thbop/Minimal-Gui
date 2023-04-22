import pygame
from pygame.locals import *

import mingu as mg
import definitions as df

from client import Client


class App(mg.App):
    def __init__(self):
        pygame.init()
        super().__init__()

        self.client = Client()
        self.client.login('Thbop', 'Beef64')
        self.client.req_chats()


        self.containers.add( df.Container( 'side-panel', pygame.Rect(5, 5, (self.width/4)-10, self.height-10) ) )


        self.main_panel = df.Container( 'main-panel', pygame.Rect((self.width/4), 5, (self.width/4)*3-5, self.height-10) )
        self.containers.add(self.main_panel)


        self.message_bar = df.TextBox( 'main-panel', pygame.Rect(10, self.height-65, self.main_panel.rect.w-20, 40), '', 16 )
        self.containers.add_element(self.message_bar)

        self.open_chat = self.client.get_known_chats()[0]
        self.messages_raw = []
        self.tick = 1


    def send_message(self):
        self.client.send_message()
    
    def check_messages(self):
        if self.tick < 300:
            self.tick += 1
        else:
            self.tick = 1
            res = self.client.req_messages(self.open_chat, 10)
            if res['error'] != None:
                print(res['error'])
            else:
                self.messages_raw = res['data']
    
    def run(self):
        while self.running:
            
            self.event_handler()
            
            self.renderer.clear('#1e1a28')


            self.renderer.update()

            self.check_messages()



if __name__ == '__main__':
    app = App()
    app.run()
