import pygame
import pygame.freetype


class Element:
    def __init__(self, master, rect):
        self.master = master
        self.rect = rect
        self.sel = False
        
        self.style = {}
    
    def check_mouse_hover(self):
        mouse = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse)

class Text(Element):
    def __init__(self, master, rect, text):
        super().__init__(master, rect)
        self.font = pygame.freetype.Font('agave/agave-r.ttf', self.rect.width)
        self.text = text