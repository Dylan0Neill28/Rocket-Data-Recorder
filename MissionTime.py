import time

def get_time():
    return time.time()
        
def get_total_time(long_time, start_time):
    return long_time - start_time

def delta_time(current_time, previous_time):
    return current_time - previous_time

def set_previous(current_height, current_time):
    global previous_height, previous_time

    previous_height = current_height
    previous_time = current_time