import numpy as np
import functions
import random

class Intruder:
    def __init__(self, center, radius, velocity):
        self.center = center
        self.radius = radius
        self.velocity = velocity
        
    def move(self, dt, xlim, ylim, obstacles):
        # update velocity randomly
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
        # normalize velocity to have constant speed
        self.velocity = np.array(self.velocity) / np.linalg.norm(self.velocity)
        
        # check for obstacle collision and avoid them
        for obs in obstacles:
            p = functions.closest_point_on_line_segment(obs.ld, obs.ru, self.center)
            p_np=np.array(p)
            d = np.linalg.norm(p_np - self.center)
            if d < self.radius + 0.5:
                v_in = self.velocity
                v_norm = functions.unitary_vector(obs.ld, obs.ru)
                self.velocity = functions.reflection(v_in, v_norm)
                break
                
        # update position
        self.center = [c + v*dt for c, v in zip(self.center, self.velocity)]
        
        # check for boundary collision and avoid them
        if self.center[0] < xlim[0]:
            self.center[0] = xlim[0]
            self.velocity[0] *= -1
        elif self.center[0] > xlim[1]:
            self.center[0] = xlim[1]
            self.velocity[0] *= -1
        if self.center[1] < ylim[0]:
            self.center[1] = ylim[0]
            self.velocity[1] *= -1
        elif self.center[1] > ylim[1]:
            self.center[1] = ylim[1]
            self.velocity[1] *= -1
