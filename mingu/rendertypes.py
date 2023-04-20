import pygame

class Box:
    """
    Generic Box renderer.

    Requires 'background', 'border', and 'border-radius'
    If 'border' is not None, then 'border-thickness' and 'hover' are  required.
    """
    def render(self, surf):
        if self.style == {}:
            pygame.draw.rect(surf, (0, 0, 0), self.rect, 0)
        else:
            pygame.draw.rect(surf, self.style['background'], self.rect, 0, self.style['border-radius'])
            
            if self.style['border'] != None:
                pygame.draw.rect(surf, self.style['border'], self.rect, self.style['border-thickness'], self.style['border-radius'])

                if self.style['hover'] != None and self.check_mouse_hover():
                    pygame.draw.rect(surf, self.style['hover'], self.rect, self.style['border-thickness'], self.style['border-radius'])

class TextRender:
    """
    Renders text with the specified color
    """

    def render(self, surf):
        if self.style == {}:
            self.font.render_to(surf, self.rect.topleft, self.text)
        else:
            self.font.render_to(surf, self.rect.topleft, self.text, self.style['color'])



