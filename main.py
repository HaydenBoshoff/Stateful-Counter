from tkinter import *
import tkinter as tk
from os.path import exists
from string import ascii_letters, punctuation

# Create the file we need to work with if it does not already exist.
if not exists("value.txt"):
    with open("value.txt", "w") as file:
        file.write("0")
    print("Error: Missing Files - The files have automatically been created, please restart.")
    quit()

# Main Class
class App:
    """Manage the app resources, behaviour, and GUI"""
    def __init__(self):
        """Initializing the class attributes"""
        # Main Root
        self.root = Tk()
        self.root.title("Incremental App")
        self.root.geometry("400x220")
        self.root.resizable(False, False)

        # Canvas
        self.canvas = tk.Canvas(self.root, width=400, height=250)
        self.canvas.pack()

        # Defaults
        self.file = "value.txt"
        self.working_value = 1  # In which value to increment or decrement
        self.value = StringVar()
        self.denied_characters = ascii_letters + punctuation
 
        # Setting the value to display
        with open(self.file, "r") as file:
            self.read_file()

            # Checking if there is even a value in the file
            if len(self.current_value) == 0:
                self.current_value = "0"

            # Checking if ASCII characters and symbols were entered in the file
            for i in self.current_value:
                if i in self.denied_characters:
                    self.current_value = "0"
                    break

            self.value.set(self.current_value)

            with open(self.file, "w") as file:
                file.write(self.current_value)

        # Accounting for certain conditions
        if int(self.current_value) > 9999999:
            self.current_value = "9999999"
            self.write_file(self.current_value)
        elif int(self.current_value) < -9999999:
            self.current_value = "-9999999"
            self.write_file(self.current_value)
        elif len(self.current_value) > 8:
            self.current_value = "0"
            self.write_file(self.current_value)

        # Value Display
        self.label = tk.Label(self.canvas, textvariable=self.value)
        self.label.config(font=("Tahoma", 30))
        self.canvas.create_window(100, 110, window=self.label)

        # Increment Button
        self.increment = tk.Button(self.canvas, text="Increment", command=self.increment)
        self.increment.config(font=("Tahoma", 20), relief=GROOVE, width=11)
        self.canvas.create_window(300, 50, window=self.increment)

        # Decrement Button
        self.decrement = tk.Button(self.canvas, text="Decrement", command=self.decrement)
        self.decrement.config(font=("Tahoma", 20), relief=GROOVE, width=11)
        self.canvas.create_window(300, 110, window=self.decrement)
        
        # Reset Button
        self.reset = tk.Button(self.canvas, text="Reset", command=self.reset)
        self.reset.config(font=("Tahoma", 20), relief=GROOVE, width=11)
        self.canvas.create_window(300, 170, window=self.reset)

    def read_file(self):
        """Read the file"""
        with open(self.file, "r") as file:
            self.current_value = file.read()
        
    def write_file(self, value):
        """Write to the file"""
        with open(self.file, "w") as file:
            file.write(value)
        self.value.set(value)

    def increment(self):
        """Increase the value by 1"""
        self.read_file()
        if int(self.current_value) < 9999999:
            new_value = int(self.current_value) + self.working_value
            self.write_file(str(new_value))

    def decrement(self):
        """Decrease the value by 1"""
        self.read_file()
        if int(self.current_value) > -9999999:
            new_value = int(self.current_value) - self.working_value
            self.write_file(str(new_value))

    def reset(self):
        """Reset the value to 0"""
        self.write_file("0")
    

if __name__ == "__main__":
    app = App()
    app.root.mainloop()
