import tkinter as tk

def selection():
    value = radio.get()
    if value == 1:
        gender = "Male"
    else:
        gender = "Female"
    print(gender)  # You can also use a label to display this in the GUI

# Create the main window
root = tk.Tk()
root.title("Gender Selection")

# Variable to hold the value of the selected radio button
radio = tk.IntVar()

# Create radio buttons for gender selection
male_radio = tk.Radiobutton(root, text="Male", variable=radio, value=1, command=selection)
female_radio = tk.Radiobutton(root, text="Female", variable=radio, value=2, command=selection)

# Place the radio buttons in the window
male_radio.pack(anchor=tk.W)
female_radio.pack(anchor=tk.W)

# Start the Tkinter main loop
root.mainloop()

