# Employee Database

## Project Overview
This is the Module 1 Capstone Project for the DTI Data Science Program at Purwadhika Digital School.
In this project, we are tasked to apply our basic Python knowledge to create an application with CRUD (Create, Read, Update, Delete) features. 
The application that I have built to fulfill this requirement is an employee database. I utilized basic Python constructs for this project, such as regular functions, for loops, and while loops.

### Databases
1. Employee Database
    - Fields:
        - `Employee ID`: A unique ID for each employee
        - `Name`: The name of each employee.
        - `Gender`: The gender of each employee.
        - `Age`: The age of each employee.
        - `Job Title`: The job title of each employee.
        - `Department`: The department where the employee works.
        - `Salary`: The salary of each employee in USD.
        - `Experience`: The experience of each employee in years.

2. Training Database
    - Fields:
        - `Training ID`: A unique ID for each training program.
        - `Topic`: The topic of the training program.
        - `Quota`: The number of employees that can join the program.
        - `Status`: The status of the training program: Available, Not Open, Completed.
        - `Employee ID`: Shows a list of employees that are registered to the training program.

There are 6 menus defined in this application:
1. `Display Employee Data` <br>
    The Display menu will show the data of the employees on a table. In this menu, you can choose to display all employee data, find an employee by their ID, and filter employee data by choosing the value you want to filter on. This menu has 3 submenus:
    - Display All Employee Data
    - Find Employee by ID
    - Filter Employee Data
2. `Display Employee Data Summary` <br>
    This menu will show basic statistics summary of the employee database such as the average, minimum, maximum, and median of each column. The 2 submenus are:
    - Display Overall Summary
    - Display Summary by Department  
3. `Add Employee Data` <br>
    This menu allows the creation of a new employee data that will be stored inside the database.
4. `Update Employee Data` <br>
    This menu allows the modification of a certain value of the employee's data. You can choose which column you want to update. Another feature of the Update Employee menu is modifying the salary of all the employees in a department based on a certain percentage as an input to the function.
5. `Delete Employee Data` <br>
    This menu is for deleting employee data by their ID.
6. `Employee Training` <br>
    This menu allows the user to display, add, and delete training programs in the database. User can also add or remove an employee from a specific training program.