# Marleyna Goodrich
# 5.3 Project: Graphing Dynamically Generated Data

import csv
import openpyxl
from datetime import datetime
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.series import SeriesLabel

# Assign CSV file path
path = "C:\\PythonFiles\\ZooData.csv"

# Append data to the CSV file
def insertData(path, data):
    try:
        with open(path, 'a') as csvfile:
            csvfile.write(data + "\n")
        return True
    except OSError as error:
        print("Error saving data:", error)
        return False

# Opens and displays the data in the CSV file
def viewData(path):
    try:
        with open(path, 'r') as csvfile:
            print("The file", path)
            print(csvfile.read())
    except OSError as error:
        print("Error reading data:", error)

# Convert numerical values based on the selected data type
def convertedData(value):
    if conversionType == "1":
        return (value - 32) * 5 / 9
    elif conversionType == "2":
        return value / 2.205
    elif conversionType == "3":
        return value * 2.54

# Collect dates and numerical values based on the selected data type
def getInput():
    global conversionType

    # Display data type options for the user
    print("What type of data would you like to enter?")
    print("1. Temperature (Fahrenheit)")
    print("2. Weight (Pounds)")
    print("3. Rain Amount (Inches)")

    conversionType = input()

    while conversionType not in ("1", "2", "3"):
        print("Invalid selection. Please enter 1, 2, or 3.")
        conversionType = input()

    # Request the number of entries
    try:
        numberOfEntries = int(input("How many entries are you inputting?\n"))

        if numberOfEntries <= 0:
            print("Please enter a number greater than zero.")
            return

    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    # Repeat data entry based on the number of entries selected
    for entry in range(numberOfEntries):
        entryDate = input("Enter a date\n")

        try:

        # Request a numerical value based on selected data type
            if conversionType == "1":
                value = float(input("Enter the highest temp for the inputted date:\n"))
            elif conversionType == "2":
                value = float(input("Enter the weight in pounds for the inputted date:\n"))
            else:
                value = float(input("Enter the rain amount in inches for the inputted date:\n"))

            # Call convertData with a float argument and expect a float return value
            convertedValue = convertedData(value)

            # Organize data into a comma-separated string
            data = f"{entryDate},{value},{convertedValue}"

            # Save the data into the CSV file
            if insertData(path, data):
                print("The following data was saved at", datetime.now(), ":", data)
                print(f"{data}\n")

        except ValueError:
            print("Invalid numerical input. Entry was not saved.")

# createChart(path, ChartType)
# path (str): location of the csv file
# chartType (str): specifies "bar" or "line"
# Returns: None; creates and saves Excel workbook
def createChart(path, chartType):
    print("Which data would you like to chart?")
    print("1. Original values in Fahrenheit")
    print("2. Converted values in Celsius")

    dataChoice = input("Enter your selection:\n")

    if dataChoice == "1":
        selectedCol = 2
        yLabel = "Temperature (Fahrenheit)"
    elif dataChoice == "2":
        selectedCol = 3
        yLabel = "Temperature (Celsius)"
    else:
        print("Invalid selection. Please select 1 or 2.")
        return

    # Create new Excel workbook
    wb = openpyxl.Workbook()
    ws = wb.active

    # Read the csv file and add conents to worksheet
    with open(path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            entryDate = row[0]
            originalValue = float(row[1])
            convertedValue = float(row[2])
            ws.append([entryDate, originalValue, convertedValue])

    # Select type of chart based on argument
    if chartType == "bar":
        myChart = BarChart()
    elif chartType == "line":
        myChart = LineChart()
    else:
        print("Invalid chart type.")
        return

    # Select the values from the selected column
    myData = Reference(ws, min_col=selectedCol, min_row=1, max_row=ws.max_row)

    # Select dates from column A
    myDataLabels = Reference(ws, min_col=1, min_row=1, max_row=ws.max_row)

    # Add selected values to the chart
    myChart.add_data(myData)

    # Name data series
    myChart.series[0].title = SeriesLabel(v=yLabel)

    # Assign dates as labels along the horizontal axis
    myChart.set_categories(myDataLabels)

    # Use my student ID and today's date as the chart title
    myChart.title = "margoo6728 " + datetime.now().strftime("%B %d, %Y")

    # Label chart axis
    myChart.x_axis.title = "Date"
    myChart.y_axis.title = yLabel

    # Set chart dimensions
    myChart.height = 15
    myChart.width = 20

    # Add chart to the worksheet
    ws.add_chart(myChart, "A6")

    # Save Excel workbook
    wb.save("C:\\FinalExam\\final2.xlsx")

    print("Chart successfully saved to C:\\FinalExam\\final2.xlsx")

# generateReport(path)
# path (str): location of csv file
# Returns: None; asks for a chart type and calls createChart()
def generateReport(path):
        print("What type of chart would you like to create?")
        print("1. Bar Chart")
        print("2. Line Chart")

        chartChoice = input("Enter your selection:\n")

        if chartChoice == "1":
            createChart(path, "bar")
        elif chartChoice == "2":
            createChart(path, "line")
        else:
            print("Invalid selection. Please enter 1 or 2.")

# Display Spreadsheet Automation Menu
print("margoo6728's New Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

number = input()

timestamp = datetime.now()
print(f"You selected {number} at {timestamp}\n")

# Call getInput when option 1 selected
if number == "1":
    getInput()

elif number == "2":
    viewData(path)
        
elif number == "3":
    generateReport(path)
    
else:
    print("Invalid menu selection")
