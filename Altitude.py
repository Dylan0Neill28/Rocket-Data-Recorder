def get_altitude(A0, pressure):
    return 44330 * (1 - ((pressure / A0) ** (1/5.255)))
