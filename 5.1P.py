import tkinter as tk  # Import the Tkinter library for GUI functionality
import RPi.GPIO as GPIO  # Import RPi.GPIO to control the GPIO pins on the Raspberry Pi

# Set the pin numbering system to BCM mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the red, green, and blue LEDs
red = 17
green = 27
blue = 22

# Set the pins as output pins to control the LEDs
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Turn off all LEDs initially by setting their output to LOW
GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.LOW)
GPIO.output(blue, GPIO.LOW)

# Function to handle LED selection
def select_led():
    # Get the selected LED choice (red, green, or blue)
    selected_led = led_choice.get()
    
    # Turn on the selected LED and turn off the others
    if selected_led == 'red':
        GPIO.output(red, GPIO.HIGH)   # Turn on the red LED
        GPIO.output(green, GPIO.LOW)  # Turn off the green LED
        GPIO.output(blue, GPIO.LOW)   # Turn off the blue LED
    elif selected_led == 'green':
        GPIO.output(red, GPIO.LOW)    # Turn off the red LED
        GPIO.output(green, GPIO.HIGH) # Turn on the green LED
        GPIO.output(blue, GPIO.LOW)   # Turn off the blue LED
    elif selected_led == 'blue':
        GPIO.output(red, GPIO.LOW)    # Turn off the red LED
        GPIO.output(green, GPIO.LOW)  # Turn off the green LED
        GPIO.output(blue, GPIO.HIGH)  # Turn on the blue LED

# Function to handle GUI exit and GPIO cleanup
def exit_gui():
    GPIO.cleanup()  # Reset the GPIO pins to their default state
    root.destroy()  # Close the Tkinter window

# Create the main Tkinter window
root = tk.Tk()
root.title("LED Controller")  # Set the title of the window
root.geometry("300x200")  # Set the size of the window (300px by 200px)
root.configure(bg="#f0f0f0")  # Set the background color of the window

# Create a Tkinter StringVar to store the selected radio button value
led_choice = tk.StringVar(value="red")  # Default value is set to "red"

# Define styles for the radio buttons (color, font, etc.)
radio_style1 = {"font": ("Arial", 12), "bg": "#ff4d4d", "fg": "#333", "pady": 10}  # Style for the red radio button
radio_style2 = {"font": ("Arial", 12), "bg": "#4dff4d", "fg": "#333", "pady": 10}  # Style for the green radio button
radio_style3 = {"font": ("Arial", 12), "bg": "#4d4dff", "fg": "#333", "pady": 10}  # Style for the blue radio button

# Create radio buttons for selecting the LED color
tk.Radiobutton(root, text="Red", variable=led_choice, value="red", command=select_led, **radio_style1).pack(anchor=tk.W, padx=20)
tk.Radiobutton(root, text="Green", variable=led_choice, value="green", command=select_led, **radio_style2).pack(anchor=tk.W, padx=20)
tk.Radiobutton(root, text="Blue", variable=led_choice, value="blue", command=select_led, **radio_style3).pack(anchor=tk.W, padx=20)
# Create the exit button to close the GUI and perform GPIO cleanup
exit_button = tk.Button(root, text="Exit", command=exit_gui, font=("Arial", 12), bg="#ff4d4d", fg="white", padx=10, pady=5)
exit_button.pack(pady=20)  # Add some padding around the button and pack it in the window
# Start the Tkinter event loop
root.mainloop()
