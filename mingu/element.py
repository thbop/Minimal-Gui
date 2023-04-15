import pygame

class Element:
    def __init__(self, master, rect):
        self.master = master
        self.rect = rect
        
        self.style = {}
