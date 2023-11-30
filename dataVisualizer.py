import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv

# Function to open the file
def open_csv_file():
    filePath = 'orderInformation.csv'
    if filePath:
        display_csv_data(filePath)

# Function to display csv data
def display_csv_data(filePath):

    with open(filePath, 'r', newline='') as file:
        csvReader = csv.reader(file)
        header = next(csvReader)  # Read the header row
        tree.delete(*tree.get_children())  # Clear the current data

        # Set the headers to the column headers of the csv
        tree["columns"] = header
        for col in header:
            tree.heading(col, text=col)
            tree.column(col, width=75)

        for row in csvReader:
            tree.insert("", "end", values=row)


# Set root of window
visualize = tk.Tk()
# Set title of window
visualize.title("Data Visualizer")

# Create a button to show the data and update the data if more has been entered while the window is open
open_button = tk.Button(visualize, text="Show Data", command=open_csv_file)
open_button.pack(padx=20, pady=10)

# Create the tree to show the .csv file
tree = ttk.Treeview(visualize, show="headings")
tree.pack(padx=20, pady=20, fill="both", expand=True)

visualize.mainloop()