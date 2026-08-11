import logging
from Config import CSV_FILENAME_RAW 
from Config import CSV_FILENAME_CLEAN

def raw_log():
    logging.basicConfig(
        filename = CSV_FILENAME_RAW,
        filemode = "w",
        level = logging.INFO,
        format = "%(message)s"
    )

def clean_log():
    logging.basicConfig(
        filename = CSV_FILENAME_CLEAN,
        filemode = "w",
        level = logging.INFO,
        format = "%(message)s"
    )

def log_info(time, phase, altitude, height, ax, ay, az, gx, gy, gz, velx, vely, velz):
    logging.info(f'Time: {time}|Phase: {phase}| Altitude: {altitude}| Height: {height}m| Ax: {ax}m/s^2| Ay: {ay}m/s^2| Az: {az}m/s^2| Gx: {gx}°/s|Gy: {gy}°/s|Gz: {gz}°/s|Velocity x: {velx}m/s| Velocity y: {vely}m/s| Velocity z: {velz}m/s ')



#def log_error():
