import pygame

class Renderer:
    def __init__(self, app):
        self.app = app

    def clear(self, color):
        self.app.window.fill(color)
    
    def render(self):
        for container in self.app.containers.containers:
            container.render(self.app.window)
            for element in container.elements:
                element.render(self.app.window)
    
    def update(self):
        pygame.display.flip()
        self.app.clock.tick(60)