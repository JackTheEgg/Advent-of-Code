#!/usr/bin/env python3
import re

class Moon:
    def __init__(self, coords):
        self.pos = [int(x) for x in coords]
        self.vel = [0, 0, 0]

def energy(moons):
    return sum([sum(map(abs, m.pos)) * sum(map(abs, m.vel)) for m in moons])

def lcm(x, y):
    a, b = x, y
    while a:
        a, b = b % a, a
    return x // b * y

with open("12.txt") as f:
    moons_str = [m.strip("\n<>") for m in f.readlines()]
moons_coords = [re.findall(r"x=(-?\d+), y=(-?\d+), z=(-?\d+)", m)[0] for m in moons_str]
moons = [Moon(m) for m in moons_coords]

for t in range(1000):
    for moon in moons:
        for other_moon in moons:
            for i in range(3):
                if moon.pos[i] < other_moon.pos[i]:
                    moon.vel[i] += 1
                elif moon.pos[i] > other_moon.pos[i]:
                    moon.vel[i] += -1
    for moon in moons:
        for i in range(3):
            moon.pos[i] += moon.vel[i]
print(energy(moons))

moons = [Moon(m) for m in moons_coords]
x_states, y_states, z_states = set(), set(), set()
while True:
    for moon in moons:
        for other_moon in moons:
            for i in range(3):
                if moon.pos[i] < other_moon.pos[i]:
                    moon.vel[i] += 1
                elif moon.pos[i] > other_moon.pos[i]:
                    moon.vel[i] += -1
    for moon in moons:
        for i in range(3):
            moon.pos[i] += moon.vel[i]
    x_state = tuple((m.pos[0], m.vel[0]) for m in moons)
    y_state = tuple((m.pos[1], m.vel[1]) for m in moons)
    z_state = tuple((m.pos[2], m.vel[2]) for m in moons)
    if x_state in x_states and y_state in y_states and z_state in z_states:
        break
    x_states.add(x_state)
    y_states.add(y_state)
    z_states.add(z_state)
print(lcm(len(x_states), lcm(len(y_states), len(z_states))))