import pygame

class Renderer:
    def __init__(self, app):
        self.app = app

    def clear(self, color):
        self.app.window.fill(color)
    
    def update(self):
        for container in self.app.containers.containers:
            container.render(self.app.window)
            for element in container.elements:
                element.render(self.app.window)

                if element.check_mouse_hover():
                    element.sel = True

                    if pygame.mouse.get_pressed()[0]:
                        if 'sel' in element.tags:
                            self.app.sel = element
                        if 'button' in element.tags and 'button:pause' not in element.tags:
                            try:
                                element.onclick()
                                
                            except: pass
                            element.tags.append('button:pause')
                    else:
                        if 'button:pause' in element.tags:
                            element.tags.remove('button:pause')
                else:
                    element.sel = False

    
        pygame.display.flip()
        self.app.clock.tick(60)