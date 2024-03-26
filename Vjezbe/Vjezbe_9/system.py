import numpy as np
import matplotlib.pyplot as plt

class SolarSystem:
    def __init__(self, G):
        self.G = G
        self.bodies = []

    def add_body(self, mass, position, velocity, name, color, size):
        body = {
            'mass': mass,
            'position': np.array(position, dtype=float),
            'velocity': np.array(velocity, dtype=float),
            'name': name,
            'color': color,
            'size': size,
            'history': [np.array(position, dtype=float)]
        }
        self.bodies.append(body)

    def calculate_gravitational_acceleration(self, body1, body2):
        r = body2['position'] - body1['position']
        distance = np.linalg.norm(r)
        if distance == 0:
            return np.zeros_like(r)
        direction = r / distance
        acceleration_magnitude = self.G * body2['mass'] / distance**2
        acceleration = direction * acceleration_magnitude
        return acceleration

    def evolve(self, num_steps, dt):
        for _ in range(num_steps):
            for i, body in enumerate(self.bodies):
                acceleration = np.zeros_like(body['position'])
                for other_body in self.bodies[:i] + self.bodies[i+1:]:
                    acceleration += self.calculate_gravitational_acceleration(body, other_body)
                body['velocity'] += acceleration * dt
                body['position'] += body['velocity'] * dt
                body['history'].append(body['position'].copy())

    def plot(self):
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('black')  
        ax.set_facecolor('black') 
        for body in self.bodies:
            positions = np.array(body['history'])
            ax.plot(positions[:, 0], positions[:, 1], color=body['color'], label=body['name'])
            ax.scatter(positions[-1, 0], positions[-1, 1], color=body['color'], s=body['size'])
        ax.set_xlabel('X [m]', color='white') 
        ax.set_ylabel('Y [m]', color='white')  
        ax.tick_params(axis='x', colors='white') 
        ax.tick_params(axis='y', colors='white')  
        ax.set_aspect('equal', 'box')
        ax.legend()
        plt.show()

