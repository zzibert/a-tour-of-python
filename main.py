class Planet:
    def __init__(self):
        self.name = "Hoth"
        self.radius = 2000
        self.gravity = 5.5
        self.system = "Hoth System"
        
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

hoth = Planet()
print(hoth.radius)
print(hoth.orbit())