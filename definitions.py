import mingu as mg

class Container(mg.Container, mg.BoxRender):
    def __init__(self, name, rect):
        super().__init__(name, rect)

        self.style = {
            'background': '#1d1a23',
            'border': '#322f3d',
            'border-radius': 18,
            'border-thickness': 2,
            'hover': None #'#4d42ad'
        }

class Button(mg.Element, mg.BoxRender):
    def __init__(self, name, rect, onclick=None):
        super().__init__(name, rect)

        self.tags.append('button')
        self.onclick = onclick

        self.style = {
            'background': '#26293f',
            'border': '#26293f',
            'border-radius': 8,
            'border-thickness': 1,
            'hover': '#4d42ad'
        }

class Text(mg.Text, mg.TextRender):
    def __init__(self, name, rect, text, size):
        super().__init__(name, rect, text, size)
        self.style = {
            'color': '#FFFFFF'
        }

class Message(mg.Text, mg.TextBoxRender):
    def __init__(self, name, rect, text, size):
        super().__init__(name, rect, text, size)
        
        self.style = {
            'background': '#26293f',
            'border': '#26293f',
            'border-radius': 8,
            'border-thickness': 1,
            'hover': '#4d42ad',
            'color': '#ffffff',
        }

class TextBox(mg.Text, mg.TextBoxRender):
    def __init__(self, name, rect, text, size, on_enter=None):
        super().__init__(name, rect, text, size)

        self.tags = ['sel', 'text', 'on_enter']
        self.on_enter = on_enter

        self.style = {
            'background': '#26293f',
            'border': '#26293f',
            'border-radius': 8,
            'border-thickness': 1,
            'hover': '#4d42ad',
            'color': '#ffffff',
        }