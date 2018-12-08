from space.planet import Planet
from space.calc import planet_mass, planet_vol

hoth = Planet('Retard', 2000, 5.5, "Yolo system")

hoth_mass = planet_mass(hoth.gravity, hoth.radius)
hoth_vol = planet_vol(hoth.radius)

print(hoth_mass, hoth_vol)