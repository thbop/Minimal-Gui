import pygame
from math import pi

class Box:
    """
    Generic Box renderer.
    Requires 'background', 'border', and 'border-radius'
    If 'border' is not None, then 'border-thickness' is  required.
    """
    def render(self, surf):
        if self.style == {}:
            pygame.draw.rect(surf, (0, 0, 0), self.rect, 0)
        else:
            pygame.draw.rect(surf, self.style['background'], self.rect, 0, self.style['border-radius'])
            if self.style['border'] != None:
                pygame.draw.rect(surf, self.style['border'], self.rect, self.style['border-thickness'], self.style['border-radius'])


