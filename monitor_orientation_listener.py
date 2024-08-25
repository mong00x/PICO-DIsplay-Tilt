import tkinter as tk
import serial

# Set up serial connection to the Pico (adjust the port name as necessary)
ser = serial.Serial('COM7', 115200)  # Replace 'COM3' with your port (e.g., '/dev/ttyUSB0' on Linux)

def show_popup(orientation):
    popup = tk.Tk()
    popup.overrideredirect(True)  # Remove window decorations
    
    # Get the screen width and height
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    
    # Set desired window dimensions
    window_width = 400  # Adjust this to make the window wider
    window_height = 100  # Keep this as is or adjust as needed
    
    # Calculate positions to center the window horizontally and place it at the bottom
    x_offset = (screen_width - window_width) // 2
    y_offset = screen_height - window_height - 100  # 10 pixels from the bottom edge
    
    # Set window size and position
    popup.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
    
    label = tk.Label(popup, text=f"Orientation: {orientation}", font=("Helvetica", 12))
    label.pack(expand=True)
    
    # Set a timer to destroy the popup after 2-3 seconds
    popup.after(2500, popup.destroy)
    popup.mainloop()

while True:
    # Read orientation data from the Pico
    if ser.in_waiting > 0:
        orientation = ser.readline().decode().strip()
        print("Orientation received:", orientation)
        show_popup(orientation)  # Display popup with current orientation
