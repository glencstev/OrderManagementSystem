# Import tkinter to create GUI
import tkinter as tk
# Import csv for manipulating the csv file
import csv
# Import Path for file checking
from pathlib import Path
# Import PANDAS for dataframes
import pandas as pd
# Import datetime for dates
from datetime import date
# Import Canvas from reportlab for pdf generation
from reportlab.pdfgen.canvas import Canvas
# Import pagesize from reportlab
from reportlab.lib.pagesizes import letter
# Import webbrowser to open pdf file
import webbrowser



# Set root of window
data = tk.Tk()

# Set window dimensions and title
data.geometry("800x100")
data.title("Data Entry")

# Creates and defines variables for tkinter inputs
orderNumberVar = tk.StringVar()
firstNameVar = tk.StringVar()
lastNameVar = tk.StringVar()
unitsVar = tk.StringVar()
costsPerUnitVar = tk.StringVar()
phoneNumberVar = tk.StringVar()
totalCostVar = tk.StringVar()

# Creates variable for file checking
fileCheck = Path("orderInformation.csv")

# Check if the file already exists
if fileCheck.exists():
    pass
else:
    # Create file if it doesn't and open it for writing
    with open('orderInformation.csv', 'w', newline='') as file:
        # Create the CSV Writer
        writer = csv.writer(file)
        # Create Headers in the csv file
        writer.writerow(['Order Number', 'First Name', 'Last Name', 'Phone Number', 'Units', 'Cost Per Unit', 'Total Cost', 'Date'])

# Read the CSV file into a dataframe
orderInformationDF = pd.read_csv("orderInformation.csv")
print(orderInformationDF)

# function to submit the information
def submit():
    # Assign the user input to variables
    orderNumber = orderNumberVar.get()
    firstName = firstNameVar.get()
    lastName = lastNameVar.get()
    phoneNumber = phoneNumberVar.get()
    units = unitsVar.get()
    costPerUnit = costsPerUnitVar.get()
    orderDate = date.today()
    # Try to calculate the total cost
    try:
        totalCost = (float(units) * float(costPerUnit))
    except ValueError:
        # If the number of units or cost per unit is not a number, print a warning it total cost text box
        totalCostVar.set('Please Input Numbers')
    # Open the csv file for appending
    # Check if order number is in the list of orders
    if int(orderNumber) in orderInformationDF['Order Number'].values:
        orderNumberVar.set('Order Number already in use')
    else:
        if len(phoneNumber) != 10:
            phoneNumberVar.set('Enter Valid Phone Number')
        else:
            with open('orderInformation.csv', 'a', newline='') as file:
                # Create CSV writer
                writer = csv.writer(file)
                # Write order data as a row
                writer.writerow([orderNumber, firstName, lastName, phoneNumber, units, costPerUnit, totalCost, orderDate])

    # Reset the text inputs to blank for new inputs
    totalCostVar.set(totalCost)


# function to search through the information
def search():
    # Reads any new information added to the CSV file
    orderInformationDF = pd.read_csv("orderInformation.csv")

    # Gets the order number from the entry
    orderNumber = orderNumberVar.get()

    # find the order information from the dataframe
    check = orderInformationDF[orderInformationDF['Order Number'].astype(str).str.contains(orderNumber)]

    # fill in the other information into the text boxes
    orderNumberVar.set(check['Order Number'].iloc[0])
    firstNameVar.set(check['First Name'].iloc[0])
    lastNameVar.set(check['Last Name'].iloc[0])
    phoneNumberVar.set(check['Phone Number'].iloc[0])
    unitsVar.set(check['Units'].iloc[0])
    costsPerUnitVar.set(check['Cost Per Unit'].iloc[0])
    totalCost = (check['Units'].iloc[0] * check['Cost Per Unit'].iloc[0])
    totalCostVar.set(totalCost)


# function to clear the entry boxes
def clear():
    orderNumberVar.set("")
    firstNameVar.set("")
    lastNameVar.set("")
    unitsVar.set("")
    costsPerUnitVar.set("")
    phoneNumberVar.set("")
    totalCostVar.set("")
    print(orderInformationDF)

# Function to create a pdf order form
def createPDF():
    # Update the Dataframe
    orderInformationDF = pd.read_csv("orderInformation.csv")

    # Get the information either inputted or searched
    orderNumber = orderNumberVar.get()
    firstName = firstNameVar.get()
    lastName = lastNameVar.get()
    phoneNumber = phoneNumberVar.get()
    units = unitsVar.get()
    costPerUnit = costsPerUnitVar.get()

    totalCost = (float(units) * float(costPerUnit))

    # Used to look for the information in the dataframe
    check = orderInformationDF[orderInformationDF['Order Number'].astype(str).str.contains(orderNumber)]
    orderDate = check['Date'].iloc[0]
    c = Canvas('OrderFile.pdf')
    w, h = letter
    text = c.beginText(30, h-30)
    c.setFont("Times-Roman", 10)
    text.textLine(f'Date Ordered: {orderDate}')
    text.textLine(' ')
    text.textLine(f'Order Number: {orderNumber}    First Name: {firstName}    Last Name: {lastName}    Phone Number: {phoneNumber}')
    text.textLine(' ')
    text.textLine(f'Units Bought: {units}    Cost Per Unit: ${costPerUnit}    Total Cost: ${totalCost}')
    c.drawText(text)
    c.showPage()
    c.save()
    webbrowser.open_new(r'OrderFile.pdf')

def goBack():
    data.destroy()


# creating a label and entry box for order number
orderNumberLabel = tk.Label(data, text='Order Number', font=('calibre', 10, 'bold'))
orderNumberEntry = tk.Entry(data, textvariable=orderNumberVar, font=('calibre', 10, 'normal'))

# creating a label and entry box for first name
firstNameLabel = tk.Label(data, text='First Name', font=('calibre', 10, 'bold'))
firstNameEntry = tk.Entry(data, textvariable=firstNameVar, font=('calibre', 10, 'normal'))

# creating a label and entry box for last name
lastNameLabel = tk.Label(data, text='Last Name', font=('calibre', 10, 'bold'))
lastNameEntry = tk.Entry(data, textvariable=lastNameVar, font=('calibre', 10, 'normal'))

# creating a label and entry box for the phone number
phoneLabel = tk.Label(data, text='Phone Number', font=('calibre', 10, 'bold'))
phoneEntry = tk.Entry(data, textvariable=phoneNumberVar, font=('calibre', 10, 'normal'))

# creating a label and entry box for units
unitsLabel = tk.Label(data, text='Units', font=('calibre', 10, 'bold'))
unitsEntry = tk.Entry(data, textvariable=unitsVar, font=('calibre', 10, 'normal'))

# creating a label and entry box for costPerUnit
costPerUnitLabel = tk.Label(data, text='Cost Per Unit', font=('calibre', 10, 'bold'))
costPerUnitEntry = tk.Entry(data, textvariable=costsPerUnitVar, font=('calibre', 10, 'normal'))

# creating a label for total costs
totalCostLabel = tk.Label(data, text='Total Cost', font=('calibre', 10, 'bold'))
totalCostEntry = tk.Entry(data, textvariable=totalCostVar, font=('calibre', 10, 'normal'))

# creating a button that will call the submit function
sub_btn = tk.Button(data, text='Submit', command=submit)
search_btn = tk.Button(data,text='Search by Order Number', command=search)
clear_btn = tk.Button(data,text='Clear', command=clear)
return_btn = tk.Button(data,text='Return', command=goBack)
createPDF_btn = tk.Button(data,text='Create Order Report', command=createPDF)

# Placing the labels and entry boxes on a grid
orderNumberLabel.grid(row=0, column=0)
orderNumberEntry.grid(row=0, column=1)
firstNameLabel.grid(row=1, column=0)
firstNameEntry.grid(row=1, column=1)
lastNameLabel.grid(row=1, column=2)
lastNameEntry.grid(row=1, column=3)
phoneLabel.grid(row=1, column=4)
phoneEntry.grid(row=1, column=5)
unitsLabel.grid(row=2, column=0)
unitsEntry.grid(row=2, column=1)
costPerUnitLabel.grid(row=2, column=2)
costPerUnitEntry.grid(row=2, column=3)
totalCostLabel.grid(row=2, column=4)
totalCostEntry.grid(row=2, column=5)
sub_btn.grid(row=3, column=1)
search_btn.grid(row=3, column=2)
clear_btn.grid(row=3, column=3)
return_btn.grid(row=3, column=4)
createPDF_btn.grid(row=3, column=5)

# loop to display window
data.mainloop()
