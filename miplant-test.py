
from miplant import MiPlant

for plant in MiPlant.discover():
        print(plant.temperature)
