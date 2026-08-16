from operator import __not__
import FlightEvents
import MissionTime
import Extra
import Altitude
import Acceleration
import Gyro
import Config
import Plot
import Logger
import Phases

import Velocity

import time
import statistics as stats
import numpy as np

from scipy.signal import savgol_filter

def check_landing(window, rep, altitude, acceloration):
    alt_window = altitude[rep-window:rep]
    accel_window = acceloration[rep-window:rep]
    
    if max(alt_window) - min(alt_window) < 0.2 and max(accel_window) - min(accel_window) < 0.1:
        return True
    else:
        return False

def rolling_window(i, n, window, k):
    if i < k:
        start = 0
        end = window
    elif i + k >= n:
        start = n - window
        end = n
    else: 
        start = i - k
        end = i + k + 1
    return start, end

class Data:
    def __init__(self):
        self.fd = []

    def hampel_filter(self, window , nsigma):  
        k = window//2
        n = len(self.fd)
        for i in range(n):
            point = self.fd[i]
            start, end = rolling_window(i, n, window, k)
            set = np.array(self.fd[start:end])
            median = stats.median(set)
            mad = stats.median(abs(set - median))
            sigma = 1.4826 * mad

            if sigma == 0:
                continue
            elif abs(point - median) > nsigma * sigma:
                self.fd[i] = median
the_time = Data()

altitude = Data()

vx = Data()
vy = Data()
vz = Data()

height = Data()

ax = Data()
ay = Data()
az = Data()

gx = Data()
gy = Data()
gz = Data()

phase = Data()

check = Data()

rep = -1
program_start = FlightEvents.program_start()

if program_start:

    start_time = MissionTime.get_time()
    initial_altitude = Altitude.get_altitude()

    print('program started')
    print('ready for launch')

    while True:
        if len(check.fd) > 19:
            check.fd.pop(0)

        the_time.fd.append(Extra.round_down_thousandths(MissionTime.get_time() - start_time))
        altitude.fd.append(Altitude.get_altitude(Altitude.A0, Altitude.get_pressure()))
        ax_sample, ay_sample, az_sample = Acceleration.get_accel()
        gx_sample, gy_sample, gz_sample = Gyro.get_gyro()

        ax.fd.append(ax_sample)
        ay.fd.append(ay_sample)
        az.fd.append(az_sample)

        gx.fd.append(gx_sample)
        gy.fd.append(gy_sample)
        gz.fd.append(gz_sample)

        rep += 1

        if rep > 5 and the_time.fd[rep] > 10:
            check.fd.append(check_landing(5, rep, altitude.fd, ay.fd))
            check.fd = [True, True, True, True, True, True]
            if all(check.fd):
                print('ROCKET LANDED')
                break
        
        time.sleep(Config.LOG_INTERVAL)
    
    
    altitude.hampel_filter(window=7 , nsigma=3)
    savgol_filter(altitude.fd, window_length=31, polyorder=2)

    savgol_filter(ax.fd, window_length=7, polyorder=2)
    savgol_filter(ay.fd, window_length=7, polyorder=2)
    savgol_filter(az.fd, window_length=7, polyorder=2)

    savgol_filter(gx.fd, window_length=5, polyorder=2)
    savgol_filter(gy.fd, window_length=5, polyorder=2)
    savgol_filter(gz.fd, window_length=5, polyorder=2)

    for i in range(len(the_time.fd)):
        vx.fd.append(Velocity.get_a_velocity(i, the_time.fd, ax.fd))
        vy.fd.append(Velocity.get_vertical_velocity(i, the_time.fd, ay.fd, altitude.fd))
        vz.fd.append(Velocity.get_a_velocity(i, the_time.fd, az.fd))
        height.fd.append(altitude.fd[i] - initial_altitude)

    Phases.state_machine_outline(ax.fd, ay.fd, az.fd, vx.fd, vy.fd, altitude.fd)
    for x in range(len(the_time.fd)):
        phase.fd.append(Phases.Node.run_state_machine(x))


    for n in range(len(the_time.fd)):
        Logger.log_info(the_time.fd[n], phase.fd[n], altitude.fd[n], height.fd[n], ax.fd[n], ay.fd[n], az.fd[n], gx.fd[n], gy.fd[n], gz.fd[n], vx.fd[n], vy.fd[n], vz.fd[n])

    Plot.plot_data(the_time.fd, altitude.fd, ax.fd, ay.fd, az.fd, gx.fd, gy.fd, gz.fd)
