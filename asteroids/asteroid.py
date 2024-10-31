import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        degree = random.uniform(20,50)
        angle1 = self.velocity.rotate(degree)
        angle2 = self.velocity.rotate(-degree)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_rock1 = Asteroid(self.position.x,self.position.y,new_radius)
        new_rock1.velocity = angle1 * 1.2
        new_rock2 = Asteroid(self.position.x,self.position.y,new_radius)
        new_rock2.velocity = angle2 * 1.2