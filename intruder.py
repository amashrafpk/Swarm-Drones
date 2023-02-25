import random
import numpy as np

class Intruder:
    def __init__(self, position, world_size, speed=10):
        self.position = np.array(position)
        self.world_size = world_size
        self.speed = speed
        self.direction = self._random_direction()

    def _random_direction(self):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        direction = np.array([x, y])
        return direction / np.linalg.norm(direction)

    def update(self, dt):
        self.position += self.direction * self.speed * dt
        self._check_boundaries()

    def _check_boundaries(self):
        if self.position[0] < 0:
            self.position[0] = 0
            self.direction[0] = abs(self.direction[0])
        elif self.position[0] > self.world_size[0]:
            self.position[0] = self.world_size[0]
            self.direction[0] = -abs(self.direction[0])
        if self.position[1] < 0:
            self.position[1] = 0
            self.direction[1] = abs(self.direction[1])
        elif self.position[1] > self.world_size[1]:
            self.position[1] = self.world_size[1]
            self.direction[1] = -abs(self.direction[1])
