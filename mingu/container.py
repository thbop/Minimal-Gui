import pygame

class Container:
    def __init__(self, name, rect):
        """Initializes a new Container"""
        self.name = name
        self.rect = rect
        
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
    
    def find(self, name):
        out = None
        for container in self.containers:
            if container.name == name:
                out = container
        return out
    
    def add_element(self, element):
        container = self.find(element.master)
        if container != None:
            # Offset element to fit container local space
            element.rect.x += container.rect.x
            element.rect.y += container.rect.y

            container.add(element)
        else:
            raise Exception(f'Cannot add element to container!\nEither the master container "{element.master}" doesn\'t exist or it is defective.')