class Planet:
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system} system'

hoth = Planet("retard", 2000, 5.5, "yolo")
print(hoth.orbit())
