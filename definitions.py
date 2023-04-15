import mingu as mg

class Container(mg.Container, mg.Box):
    def __init__(self, name, rect):
        super().__init__(name, rect)

        self.style = {
            'background': '#1d1a23',
            'border': '#322f3d',
            'border-radius': 18,
            'border-thickness': 2
        }

class Square(mg.Element, mg.Box):
    def __init__(self, name, rect):
        super().__init__(name, rect)

        self.style = {
            'background': '#cccccc',
            'border': None,
            'border-radius': 0
        }