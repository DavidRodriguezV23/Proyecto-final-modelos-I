# Descripción: Objetos del entorno
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import pygame
import random
import Project.Main
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class Obstacle:

    def __init__(self, hollows):
        self.posx = 0
        self.posy = 0
        self.type = None
        self.image = None
        self.imageWidth = 20
        self.imageHeight = 20
        self.generate_obs(hollows)

    def generate_obs(self, hollows):
        self.posx = random.randint(0, Project.Main.displayWidth - self.imageWidth)
        self.posy = random.randint(0, Project.Main.displayHeight - self.imageHeight)
        pos = Point(self.posx, self.posy)
        validated = True
        for h in hollows:
            polygon = Polygon(h.corners)
            if polygon.contains(pos):
                validated = False
        self.type = random.choice(['stone', 'spike'])
        # self.image = pygame.image.load('Project/resources/' + self.type + '.png') Falta imagen
        print('Obstaculo:', self.type)
        if not validated:
            self.generate_obs(hollows)