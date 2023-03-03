import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random
import numpy as np

class Intruder:
    def __init__(self, center, radius, velocity):
        self.center = center
        self.radius = radius
        self.velocity = velocity
        
    def move(self, dt):
            # update velocity randomly
            self.velocity = [random.uniform(0, 3), random.uniform(3, 46)]
            # normalize velocity to have constant speed
            self.velocity = np.array(self.velocity) / np.linalg.norm(self.velocity)
            # update position
            self.center = [c + v*dt for c, v in zip(self.center, self.velocity)]
            