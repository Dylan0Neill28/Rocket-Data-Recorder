import statistics as stats
import numpy as np
import random

A0 = 101325 

def callibrate_init_pressure(samples=20):
    sensor_data = []
    for _ in range(samples):
        reading = random.randint(1, 100)
        sensor_data.append(reading)
    
    return stats.mean(sensor_data)

def get_pressure():
    return random.randint(1, 100)
    
def get_altitude(A0, pressure):
    return 44330 * (1 - ((pressure / A0) ** (1/5.255)))