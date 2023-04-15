import mingu as mg

class Container(mg.Container, mg.Box):
    def __init__(self, name, rect):
        super().__init__(name, rect)

        self.style['background'] = '#1d1a23'
        self.style['border'] = '#322f3d'
        self.style['border-radius'] = 18
        self.style['border-thickness'] = 2

class Square(mg.Element, mg.Box):
    def __init__(self, name, rect):
        super().__init__(name, rect)

        self.style['background'] = '#cccccc'
        self.style['border-radius'] = 0
        self.style['border'] = None