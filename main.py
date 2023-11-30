# Import tkinter to create GUI
import tkinter as tk
from tkinter import filedialog
# Import csv for manipulating the csv file
import os

main = tk.Tk()

# Set window dimensions and window title
main.geometry("400x100")
main.title("OMS")

# Title for inside the window
title = tk.Label(main, text='Order Management System')

# Functions for running the other files
def dataEntry():
    # Run the data entry file
    os.system('python dataEntry.py')

def dataVisualizer():
    # Run the data visualizer file
    os.system('python dataVisualizer.py')


# Creating the buttons for the window
dataEntrybtn = tk.Button(main, text="Data Entry", command=dataEntry, height = 1, width=10)
dataVisualizerbtn = tk.Button(main, text='Data Visualizer', command=dataVisualizer, height=1, width=10)

# Placing the title and buttons
title.place(relx=0.5, rely=0, anchor=tk.N)
dataEntrybtn.place(x=20, y=20)
dataVisualizerbtn.place(x=300, y=20)

# loop to display window
main.mainloop()
exit(0)