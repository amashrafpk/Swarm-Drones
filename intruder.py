import matplotlib.pyplot as plt
import random

import numpy as np

class Intruder:
    def __init__(self, center, radius, velocity, xlim, ylim):
        self.center = center
        self.radius = radius
        self.velocity = velocity
        self.xlim = xlim
        self.ylim = ylim
        
    def move(self, dt):
        # update velocity randomly
        noise = np.random.normal(0, 0.1, 2)
        self.velocity += noise
        # normalize velocity to have constant speed
        self.velocity = np.array(self.velocity) / np.linalg.norm(self.velocity)
        # update position
        center_new = [c + v*dt for c, v in zip(self.center, self.velocity)]
        # check if new position is within the limits of the plot
        if (self.xlim[0] + self.radius <= center_new[0] <= self.xlim[1] - self.radius and 
            self.ylim[0] + self.radius <= center_new[1] <= self.ylim[1] - self.radius):
            self.center = center_new
        else:
            # if the new position is outside the plot, reflect the velocity
            if center_new[0] < self.xlim[0] + self.radius or center_new[0] > self.xlim[1] - self.radius:
                self.velocity[0] = -self.velocity[0]
            if center_new[1] < self.ylim[0] + self.radius or center_new[1] > self.ylim[1] - self.radius:
                self.velocity[1] = -self.velocity[1]
            # update position with new velocity
            self.center = [c + v*dt for c, v in zip(self.center, self.velocity)]
