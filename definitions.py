import mingu as mg

class Container(mg.Container, mg.Box):
    def __init__(self, name, rect):
        super().__init__(name, rect)

        self.style = {
            'background': '#1d1a23',
            'border': '#322f3d',
            'border-radius': 18,
            'border-thickness': 2,
            'hover': None #'#4d42ad'
        }

class Button(mg.Element, mg.Box):
    def __init__(self, name, rect):
        super().__init__(name, rect)

        self.style = {
            'background': '#26293f',
            'border': '#26293f',
            'border-radius': 8,
            'border-thickness': 1,
            'hover': '#4d42ad'
        }

class Text(mg.Text, mg.TextRender):
    def __init__(self, name, rect, text):
        super().__init__(name, rect, text)
        self.style = {
            'color': '#FFFFFF'
        }