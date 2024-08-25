from PiicoDev_LIS3DH import PiicoDev_LIS3DH
from PiicoDev_Unified import sleep_ms
import machine

# Initialize the LIS3DH sensor and UART (serial) communication
motion = PiicoDev_LIS3DH()
uart = machine.UART(0, baudrate=115200)  # UART0 for serial communication

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
        uart.write(orientation + "\n")  # Send orientation to PC
        last_orientation = orientation
    
    sleep_ms(50)
