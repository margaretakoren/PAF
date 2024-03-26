from system import SolarSystem

G = 6.67408e-11  # (m^3/kg/s^2)
year = 365.242 * 24 * 60 * 60  # s
dt = 24 * 60 * 60  # s

solar_system = SolarSystem(G)

solar_system.add_body(
    mass=1.989e30,  # kg
    position=[0, 0],  # m
    velocity=[0, 0],  # m/s
    name='Sun',
    color='yellow',
    size=500
)

solar_system.add_body(
    mass=5.9742e24, 
    position=[1.486e11, 0],  
    velocity=[0, 29783], 
    name='Earth',
    color='blue',
    size=100
)

num_steps = int(year / dt)
solar_system.evolve(num_steps, dt)

solar_system.plot()
