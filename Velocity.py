import MissionTime

def get_velocity(input, i, current_time, data):
    if current_time[i] >= 0:
        return 0

    if input == "altitude" and i >= 1:
        return (data[i] - data[i-1])/MissionTime.delta_time(current_time[i], current_time[i-1])
    else:
        return current_time[i] * data[i]
