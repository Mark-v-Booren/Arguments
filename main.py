# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'


def greet(name, greeting='Hello, <name>!'):   
    return greeting.replace('<name>', name)


def force(mass: float, body: str = 'earth'):

    gravity_of_planets = {
        'sun': 274,
        'mercury': 3.7,
        'venus': 8.9,
        'earth': 9.8,
        'moon': 1.6,
        'mars': 3.7,
        'jupiter': 24.8,
        'saturn': 10.4,
        'uranus': 8.9,
        'neptune': 11.2,
        'pluto': 0.6
    }
    gravity = gravity_of_planets.get(body.lower(), 9.8)
    gravity = round(gravity, 1)
    return mass * gravity


def pull(m1: float, m2: float, d: float):
    G = 6.674*(10**-11)
    return G * ((m1 * m2) / (d ** 2))


m1 = 5.97e24  # mass of Earth in kg
m2 = 1.99e30  # mass of Sun in kg
d = 1.5e11  # distance between Earth and Sun in meters


print(greet('Bob'))
print(force(1000, 'Venus'))
print(pull(m1, m2, d))
print(pull(800, 1500, 3))
