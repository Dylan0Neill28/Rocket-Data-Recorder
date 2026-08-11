import time

def get_vertical_velocity(i, current_time, ay, altitude):
    if i < 1 or current_time <= 0 :
        return current_time[i] * ay[i]
    
    return (altitude[i] - altitude[i-1])/(current_time[i]-current_time[i-1])

def get_a_velocity(i, current_time, acceloration):
    return current_time[i] * acceloration[i]
