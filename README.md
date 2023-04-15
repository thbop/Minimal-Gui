# Minimal Gui
Minimal Gui, or Mingu is an attempt at a Pygame Gui library. The goal is to allow simple, powerful, and flexible tools for developing Gui applications.

## Basic ideas:
The app is the base manager for everything. It is properly implemented by inheriting it into your own app's class and also calling the superclass constructor.

Mingu works in a hierarchical manner, with "elements" being the basic building blocks for everything. 
Containers obviously contain elements (yet the container class itself is inherited from the element class) and elements generally function as the buttons, textboxes, etc. for the app.

The renderer class (called in the base app class) handles the basic function of clearing the screen with a certain color, rendering the containers/elements, and updating the window. In order for the renderer to properly render the app containers/elements, you must either define your own render method per container/element (by creating your own class of either and inheriting from the base element/container class) or use one of the provided methods who's classes must be inherited (check rendertypes.py).