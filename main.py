"""
PiicoDev Accelerometer LIS3DH
Simple example to infer tilt-angle from acceleration data
"""

from PiicoDev_LIS3DH import PiicoDev_LIS3DH
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

motion = PiicoDev_LIS3DH()

# Example function to send a command to Windows
def rotate_display_on_windows(orientation):
    # Here you would send a command to rotate the display based on `orientation`
    # This could be through a serial port or using keyboard emulation
    pass

def get_orientation(x, y, z):
    if abs(x) > 45:  # Landscape mode
        if x > 0:
            return "landscape"
        else:
            return "landscape_flipped"
    elif abs(y) > 45:  # Portrait mode
        if y > 0:
            return "portrait"
        else:
            return "portrait_flipped"
    else:
        return "flat"

last_orientation = None

while True:
    x, y, z = motion.angle
    orientation = get_orientation(x, y, z)
    
    if orientation != last_orientation:
        print("Orientation changed:", orientation)
        rotate_display_on_windows(orientation)  # Call your function here
        last_orientation = orientation
    
    sleep_ms(50)

