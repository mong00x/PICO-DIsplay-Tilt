from PiicoDev_LIS3DH import PiicoDev_LIS3DH
from PiicoDev_Unified import sleep_ms
import machine
import time

# Initialize the LIS3DH sensor and UART (serial) communication
motion = PiicoDev_LIS3DH()
uart = machine.UART(0, baudrate=115200)  # UART0 for serial communication

# Debounce interval in seconds
debounce_interval = 3
last_time = time.time()

# Transition zone of 20 degrees
detect_zone = 20

def get_angle(x,y,z):
    if abs(int(z)) in range(0, 20):  # Landscape 
        return "landscape"
    elif int(z) in range(90 - detect_zone, 90 + detect_zone):
        return "portrait"
    elif abs(int(z)) in range(180 - detect_zone, 180):
        return "landscape filpped"
    elif int(z) in range(-90 - detect_zone, -90 + detect_zone):
        return "portrait flipped"
    else:
        return "Angle in transition..." #No change within the transition zone

last_angle = None

while True:
    current_time = time.time()
    
    if current_time - last_time >= debounce_interval:
        x, y, z = motion.angle
        angle = get_angle(x,y,z)
        # print("Angle: {:.0f}°".format(z)) # #monitor value in plotter
        # print("Current angle:"+angle)
        if angle != last_angle:
            # print("Angle changed:")
            print(angle)
            uart.write(angle + "\n")  # Send orientation to PC
            if angle = "Angle in transition...":
                last_angle = angle
                
        
        # Update the last_time to the current time
        last_time = current_time
    
    sleep_ms(100)  # Small sleep to avoid excessive CPU usage

