import pygame
import json

class Renderer:
    def __init__(self, app):
        self.app = app

        self.style = {}
    
    def load_style(self, filename):
        """Loads the specified style file"""
        file = open(filename)
        self.style = json.load(file)
        file.close()
    
    def clear(self):
        self.app.window.fill(self.style['background'])
    
    def render(self):
        for container in self.app.containers.containers:
            pygame.draw.rect(self.app.window, (0, 255, 0), container.rect, 2)
            for element in container.elements:
                pygame.draw.rect(self.app.window, (255, 0, 0), element.rect)
    
    def update(self):
        pygame.display.flip()
        self.app.clock.tick(60)