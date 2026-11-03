# Graphing_Dynamically_Generated_Data
ECPI 202610E OL SDC205L AO Python for Data Analytics Lab

## 5.3 Project: Graphing Dynamically Generated Data

# Criteria 
- Create a function called createChart that takes two arguments as the path to the CSV data file and a chart type (line or bar). Within the function, complete the following:
  - Ask the user to choose the data source for which to generate the data—either the initial data (pounds, inches, or Fahrenheit) or the converted type (kilograms, centimeters, or Celsius). This will depend on the spreadsheet you chose to automate at the beginning of your project. 
  - Open the csv file and extract the appropriate data (remember to cast your data types).
  - Using openpyxl, save the data to an Excel spreadsheet titled final.xlsx.
  - Using openpyxl, generate the bar or line chart (depending on the argument passed) using the selected data source as values and the dates as labels.
  - Label the x and y-axis of the chart appropriately.
  - Create a title as "<student ID> <current date>" (example: student1234 10/10/2022).
- Create a function called generateReport that takes one argument as a path to the CSV data file. Within this function, complete the following:
  - Ask the user which graph type they would like to create, choosing between a line or bar chart.
  - Call the createChart function and pass the path to the csv data file and the appropriate chart type.
- Update the main menu to add the "Generate Report" option to call the generateReport function when a user enters "3" from the main menu created at the beginning of your project.
- Add a comment above each additional function (createChart and generateReport) as you have in the previous week. In the comments describe the required arguments, the argument type(s), and any return value.
