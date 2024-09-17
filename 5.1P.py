import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
red = 17
green = 27
blue = 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.LOW)
GPIO.output(blue, GPIO.LOW)

def select_led():
    selected_led = led_choice.get()
    if selected_led == 'red':
        GPIO.output(red, GPIO.HIGH)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)
    elif selected_led == 'green':
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.HIGH)
        GPIO.output(blue, GPIO.LOW)
    elif selected_led == 'blue':
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.HIGH)

def exit_gui():
    GPIO.cleanup()
    root.destroy()

root = tk.Tk()
root.title("LED Controller")
root.geometry("300x200")
root.configure(bg="#f0f0f0")  

led_choice = tk.StringVar(value="red")

radio_style = {"font": ("Arial", 12), "bg": "#f0f0f0", "fg": "#333", "pady": 10}

tk.Radiobutton(root, text="Red", variable=led_choice, value="red", command=select_led, **radio_style).pack(anchor=tk.W, padx=20)
tk.Radiobutton(root, text="Green", variable=led_choice, value="green", command=select_led, **radio_style).pack(anchor=tk.W, padx=20)
tk.Radiobutton(root, text="Blue", variable=led_choice, value="blue", command=select_led, **radio_style).pack(anchor=tk.W, padx=20)

exit_button = tk.Button(root, text="Exit", command=exit_gui, font=("Arial", 12), bg="#ff4d4d", fg="white", padx=10, pady=5)
exit_button.pack(pady=20)

root.mainloop()

