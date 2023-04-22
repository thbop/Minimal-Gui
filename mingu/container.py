import pygame
from .element import Element

class Container(Element):
    def __init__(self, name, rect):
        """Initializes a new Container"""
        super().__init__('WINDOW', rect)
        self.name = name
        
        self.elements = []
    
    def add(self, element):
        self.elements.append(element)

    def remove(self, element):
        self.elements.remove(element)
    
    

class Containers:
    def __init__(self, app):
        """Initializes the Container Manager"""
        self.app = app

        self.containers = []

    def add(self, container):
        self.containers.append(container)
    
    def remove(self, container):
        self.containers.remove(container)
    
    def get(self, name):
        out = None
        for container in self.containers:
            if container.name == name:
                out = container
        return out
    
    def get_index(self, name):
        out = None
        for i, container in enumerate(self.containers, 0):
            if container.name == name:
                out = i
        return out
    
    def add_element(self, element):
        container = self.get(element.master)
        if container != None:
            # Offset element to fit container local space
            element.rect.x += container.rect.x
            element.rect.y += container.rect.y

            container.add(element)
        else:
            raise Exception(f'Cannot add element to container!\nEither the master container "{element.master}" doesn\'t exist or it is defective.')