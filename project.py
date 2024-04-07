import tkinter as tk
from tkinter import ttk
import subprocess

class GestureControlApp:
    def __init__(self, master):
        self.master = master
        master.title("Gesture Control")

        # Calculate screen DPI (dots per inch) to adjust window size
        dpi = master.winfo_fpixels('1i')
        pixels_per_cm = dpi / 2.54

        # Calculate pixels for 3cm width and 1cm height for buttons
        button_width = int(3 * pixels_per_cm)
        button_height = int(1 * pixels_per_cm)

        # Calculate pixels for 10cm width and height for window
        width_pixels = int(10 * pixels_per_cm)
        height_pixels = int(10 * pixels_per_cm)

        # Set window size
        master.geometry(f"{width_pixels}x{height_pixels}")

        # Style configuration
        self.style = ttk.Style()

        # Green color for Start button
        self.style.configure('Start.TButton', font=('Arial', 12), foreground='#4caf50', background='#4caf50')
        self.style.map('Start.TButton', background=[('active', '#45a049')])

        # Red color for Stop button
        self.style.configure('Stop.TButton', font=('Arial', 12), foreground='#f44336', background='#f44336')
        self.style.map('Stop.TButton', background=[('active', '#d32f2f')])

        # Create frame
        self.frame = tk.Frame(master, bg='#f0f0f0')
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Calculate button width with padding
        button_width_with_padding = button_width + 10  # Adjust padding as needed

        # Create welcome label with each letter having different color
        welcome_text = "Welcome to Future AI Operating Computers "
        self.welcome_label = tk.Label(self.frame, text=welcome_text, font=("Arial", 15))
        self.welcome_label.pack(pady=5)
        self.welcome_label.config(fg='red', font=("Arial", 15))

        # Create start button
        self.start_button = ttk.Button(self.frame, text="Start Gesture Control", style='Start.TButton', command=self.start_gesture_control, width=button_width_with_padding)
        self.start_button.pack(pady=5)

        # Create stop button
        self.stop_button = ttk.Button(self.frame, text="Stop Gesture Control", style='Stop.TButton', command=self.stop_gesture_control, width=button_width_with_padding)
        self.stop_button.pack(pady=5)

    def start_gesture_control(self):
        self.start_button.configure(state='disabled')  # Disable start button
        subprocess.Popen(["python", "Gesture_Controller.py"])

    def stop_gesture_control(self):
        subprocess.run(["taskkill", "/f", "/im", "python.exe", "/t"])
        self.start_button.configure(state='normal')  # Enable start button when stopping
        self.master.deiconify()  # Show the window back

root = tk.Tk()
app = GestureControlApp(root)
root.mainloop()
