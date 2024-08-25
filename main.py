import ctypes
from PiicoDev_LIS3DH import PiicoDev_LIS3DH
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

def rotate_display(angle):
    # 0: Landscape
    # 1: Portrait (Flipped 90 degrees clockwise)
    # 2: Landscape (Flipped 180 degrees)
    # 3: Portrait (Flipped 270 degrees)
    angle_mapping = {
        0: 0,
        90: 1,
        180: 2,
        270: 3
    }
    ctypes.windll.user32.SetDisplayConfig(0, 0, 0, 0, 0x10 | 0x8)
    ctypes.windll.user32.SetDisplayConfig(1, ctypes.byref(ctypes.wintypes.DEVMODE(0, angle_mapping[angle], 0)), 0, 0, 0x10 | 0x8)

# Example usage:
# rotate_display(90)  # Rotate the display to 90 degrees (portrait mode)
