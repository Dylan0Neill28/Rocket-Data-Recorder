import math as m
import random

def get_accel():
    ax = random.randint(1, 100)
    ay = random.randint(1, 100)
    az = random.randint(1, 100)

    return ax, ay, az

def total_accel(ax, ay, az):

    return m.sqrt(m.pow(ax, 2) + m.pow(ay, 2) + m.pow(az, 2))