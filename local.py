import tkinter as tk
from tkinter import font
import time

class InfoClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock Display")

        # Create the clock label
        self.clock_label = tk.Label(root, font=('Helvetica', 48), fg='white', bg='black')
        self.clock_label.pack(pady=20)

        # Create the info slide label (hidden by default)
        self.info_label = tk.Label(root, font=('Helvetica', 24), fg='black', bg='yellow')
        
        # Start updating the clock
        self.update_clock()

    def update_clock(self):
        # Get the current time and update the clock label
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        # Call this method again after 1000ms (1 second)
        self.root.after(1000, self.update_clock)

    def show_slide(self, slide):
        # Show the selected info slide
        self.info_label.config(text=slide)
        self.info_label.pack(pady=20, fill='x')

    def clear_slide(self):
        # Hide the info slide and show only the clock
        self.info_label.pack_forget()

class ControlPanelApp:
    def __init__(self, control_window, display_app):
        self.control_window = control_window
        self.display_app = display_app
        self.control_window.title("Control Panel")

        # Button labels stored in a dictionary
        self.default_button_labels = {
            1: "Show Info 1",
            2: "Show Info 2",
            3: "Show Info 3",
            4: "Show Info 4",
            5: "Show Info 5"
        }

        # List of slides
        self.slides = [
            "Please turn on your microphone.",
            "Please Speak into the microphone.",
            "Please Speak louder.",
            "Please adjust your setup.",
            "Check your internet connection."
        ]

        # Create buttons for each slide in the control panel
        self.buttons = {}
        for i in range(1, 6):
            button = tk.Button(control_window, text=self.default_button_labels[i], command=lambda i=i: self.show_slide(i), font=('Helvetica', 18))
            button.pack(pady=10)
            self.buttons[i] = button  # Store button references

        # Add a Clear button to reset the display to only show the clock
        clear_button = tk.Button(control_window, text="Clear", command=self.clear_slide, font=('Helvetica', 18))
        clear_button.pack(pady=10)

    def show_slide(self, slide_id):
        # Show the selected slide in the main display window
        self.display_app.show_slide(self.slides[slide_id - 1])

        # Update the button text to indicate which slide is being shown
        self.buttons[slide_id].config(text=f"Showing Slide {slide_id}")

    def clear_slide(self):
        # Clear the slide and show only the clock
        self.display_app.clear_slide()

        # Reset all button texts back to their original labels
        for i in range(1, 6):
            self.buttons[i].config(text=self.default_button_labels[i])

# Create the main display window
root = tk.Tk()
display_app = InfoClockApp(root)

# Create a separate control panel window
control_window = tk.Toplevel(root)
control_panel = ControlPanelApp(control_window, display_app)

# Run the main loop
root.mainloop()
import tkinter as tk
from tkinter import font
import time

class InfoClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock Display")

        # Create the clock label
        self.clock_label = tk.Label(root, font=('Helvetica', 48), fg='white', bg='black')
        self.clock_label.pack(pady=20)

        # Create the info slide label (hidden by default)
        self.info_label = tk.Label(root, font=('Helvetica', 24), fg='black', bg='yellow')
        
        # Start updating the clock
        self.update_clock()

    def update_clock(self):
        # Get the current time and update the clock label
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        # Call this method again after 1000ms (1 second)
        self.root.after(1000, self.update_clock)

    def show_slide(self, slide):
        # Show the selected info slide
        self.info_label.config(text=slide)
        self.info_label.pack(pady=20, fill='x')

    def clear_slide(self):
        # Hide the info slide and show only the clock
        self.info_label.pack_forget()

class ControlPanelApp:
    def __init__(self, control_window, display_app):
        self.control_window = control_window
        self.display_app = display_app
        self.control_window.title("Control Panel")

        # Button labels stored in a dictionary
        self.button_labels = {
            1: "Show Info 1",
            2: "Show Info 2",
            3: "Show Info 3",
            4: "Show Info 4",
            5: "Show Info 5"
        }

        # List of slides
        self.slides = [
            "Please turn on your microphone.",
            "Please Speak into the microphone.",
            "Please Speak louder.",
            "Please adjust your setup.",
            "Check your internet connection."
        ]

        # Create buttons for each slide in the control panel
        self.buttons = {}
        for i in range(1, 6):
            button = tk.Button(control_window, text=self.button_labels[i], command=lambda i=i: self.show_slide(i), font=('Helvetica', 18))
            button.pack(pady=10)
            self.buttons[i] = button  # Store button references

        # Add a Clear button to reset the display to only show the clock
        clear_button = tk.Button(control_window, text="Clear", command=self.clear_slide, font=('Helvetica', 18))
        clear_button.pack(pady=10)

    def show_slide(self, slide_id):
        # Show the selected slide in the main display window
        self.display_app.show_slide(self.slides[slide_id - 1])

        # Update the button text to indicate which slide is being shown
        self.button_labels[slide_id] = f"Showing Slide {slide_id}"
        self.buttons[slide_id].config(text=self.button_labels[slide_id])

    def clear_slide(self):
        # Clear the slide and show only the clock
        self.display_app.clear_slide()

# Create the main display window
root = tk.Tk()
display_app = InfoClockApp(root)

# Create a separate control panel window
control_window = tk.Toplevel(root)
control_panel = ControlPanelApp(control_window, display_app)

# Run the main loop
root.mainloop()
import tkinter as tk
from tkinter import font
import time

class InfoClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock Display")

        # Create the clock label
        self.clock_label = tk.Label(root, font=('Helvetica', 48), fg='white', bg='black')
        self.clock_label.pack(pady=20)

        # Create the info slide label (hidden by default)
        self.info_label = tk.Label(root, font=('Helvetica', 24), fg='black', bg='yellow')
        
        # Start updating the clock
        self.update_clock()

    def update_clock(self):
        # Get the current time and update the clock label
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        # Call this method again after 1000ms (1 second)
        self.root.after(1000, self.update_clock)

    def show_slide(self, slide):
        # Show the selected info slide
        self.info_label.config(text=slide)
        self.info_label.pack(pady=20, fill='x')

class ControlPanelApp:
    def __init__(self, control_window, display_app):
        self.control_window = control_window
        self.display_app = display_app
        self.control_window.title("Control Panel")

        # List of slides
        self.slides = [
            "Please turn on your microphone.",
            "Please Speak into the microphone.",
            "Please Speak louder.",
            "Please ",
            "Check your internet connection."
        ]

        # Create buttons for each slide in the control panel
        for i, slide in enumerate(self.slides):
            button = tk.Button(control_window, text=f"Show Info {i+1}", command=lambda s=slide: self.display_app.show_slide(s), font=('Helvetica', 18))
            button.pack(pady=10)

# Create the main display window
root = tk.Tk()
display_app = InfoClockApp(root)

# Create a separate control panel window
control_window = tk.Toplevel(root)
control_panel = ControlPanelApp(control_window, display_app)

# Run the main loop
root.mainloop()
