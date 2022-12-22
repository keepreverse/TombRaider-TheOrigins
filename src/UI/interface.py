"""
Control the components.
Decide what will be display on the screen.
"""


class Interface:
    def __init__(self, *components):
        self.components = []
        self.add(components)

    def update(self):
        for component in self.components:
            component.update()

    def draw(self, surface):
        for component in self.components:
            component.draw(surface)

    def add(self, components):
        for component in components:
            self.components.append(component)
            component.interface = self

    def remove(self, *components):
        for component in components:
            self.components.remove(component)
            component.interface = None
