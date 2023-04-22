import pygame

from .container import Containers
from .renderer import Renderer

class App:
    def __init__(self, title=None, width=1200, height=800):
        """Initialize the application and define a window."""
        self.title = title
        self.width = width
        self.height = height

        self.window = self.create_window(self.title, self.width, self.height)

        self.running = True
        self.clock = pygame.time.Clock()

        self.sel = None

        self.containers = Containers(self)
        self.renderer = Renderer(self)

    
    def create_window(self, title, width, height):
        """
        Creates a window with parameters: title, width, and height.
        Returns the Surface object.
        """
        window = pygame.display.set_mode((width, height))
        if title == None: title = 'Mingu Application'
        pygame.display.set_caption(title)
        return window

    def event_handler(self):
        """Simple event handler for those not interested in handling events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.sel != None and 'sel' in self.sel.tags:
                if event.type == pygame.TEXTINPUT:
                    if 'text' in self.sel.tags:
                        self.sel.text += event.text
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if 'text' in self.sel.tags:
                            self.sel.text = self.sel.text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if 'text' in self.sel.tags and 'on_enter' in self.sel.tags:
                            try:
                                self.sel.on_enter()
                            except: pass