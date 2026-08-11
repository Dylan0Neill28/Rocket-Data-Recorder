import random

def get_gyro():
    gx = random.randint(1, 100)
    gy = random.randint(1, 100)
    gz = random.randint(1, 100)
    return gx, gy, gz