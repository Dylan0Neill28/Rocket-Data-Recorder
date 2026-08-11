import matplotlib.pyplot as plt

def plot_data(the_time, altitude, ax, ay, az, gx, gy, gz):
    altitude_chart = plt.figure(num="Altitude Chart", figsize=(6,4))
    plt.plot(the_time, altitude, marker='o', color='blue', linestyle='--')
    plt.ylabel('Altitude')
    plt.title('Altitude over time')

    ax_chart = plt.figure(num="Acceloration x Chart", figsize=(6,4))
    plt.plot(the_time, ax, marker='o', color='red', linestyle='--')
    plt.ylabel('Acceloration x')
    plt.title('Acceloration x over time')

    ay_chart = plt.figure(num="Acceloration y Chart", figsize=(6,4))
    plt.plot(the_time, ay, marker='o', color='green', linestyle='--')
    plt.ylabel('Acceloration y')
    plt.title('Acceloration y over time')
    
    az_chart = plt.figure(num="Acceloration z Chart", figsize=(6,4))
    plt.plot(the_time, az, marker='o', color='purple', linestyle='--')
    plt.ylabel('Acceloration z')
    plt.title('Acceloration z over time')
    
    gx_chart = plt.figure(num="Gyro x Chart", figsize=(6,4))
    plt.plot(the_time, gx, marker='o', color='pink', linestyle='--')
    plt.ylabel('Gyro x')
    plt.title('Gyro x over time')

    gy_chart = plt.figure(num="Gyro y Chart", figsize=(6,4))
    plt.plot(the_time, gy, marker='o', color='gold', linestyle='--')
    plt.ylabel('Gyro y')
    plt.title('Gyro y over time')

    gz_chart = plt.figure(num="Gyro z Chart", figsize=(6,4))
    plt.plot(the_time, gz, marker='o', color='black', linestyle='--')
    plt.ylabel('Gyro z')
    plt.title('Gyro z over time')

    plt.show()


#velocity_chart = plt.figure(num="Velocity Chart", figsize=(6,4))
    #plt.plot(the_time, altitude, marker='o', color='orange', linestyle='--')
    #plt.ylabel('Velocity')
    #plt.title('Velocity over time')