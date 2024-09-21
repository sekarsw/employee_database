import csv

#Create dictionary from csv file
file = 'employees.csv'
emp_list = []

with open(file, 'r') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    for row in data[1:]:
        emp_list.append(row)


#Dictionary
dict_keys = [emp[0] for emp in emp_list]
dict_values = [emp[1:] for emp in emp_list]

for dict in dict_values:
    dict[2] = int(dict[2])
    dict[5] = int(dict[5])
    dict[6] = int(dict[6])
emp_dict = {int(k):v for k,v in list(zip(dict_keys, dict_values))}

#-------------------------------------Supplemental Functions----------------------------------------------

#Function to add table header
def print_header():
    print(f'| ID   | {'Name':<20} | {'Gender':<7} | {'Age':<4} | {'Job Title':<15} | {'Department':<15} | {'Salary':<8} | {'Exp':>4} |')
    print('------------------------------------------------------------------------------------------------------')  

#-----------------------------------Display Menu Function--------------------------------------------------
#Display menu options prompt
display_prompt = '''
============================
Display Employee Data
============================
1. Display All Employee Data
2. Find Employee by ID
3. Filter Employee Data
4. Back to Main Menu
'''


def display_menu():
    employees = emp_dict

    while True:
        print(display_prompt)
        #Input menu number
        opt = input('Enter an option: ')

        #Error notification if input is a string
        try:
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
            continue
    
        #-----------------------------------------------------------------------------------
       
        #Display All Data Menu
        if opt == 1:
            print('========================')
            print('Display All Data')
            print('========================')
            print()
            #Printing Employee Data 
            print_header()
            for k,v in employees.items():
                name, gender, age, title, dept, salary, exp = v[0], v[1], v[2], v[3], v[4], v[5], v[6]
                print(f'| {k} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
       
       
        #-------------------------------------------------------------------------------------
        
        #Display Find Employee by ID Menu
        elif opt == 2:
            print('=====================')
            print('Find Employee by ID')
            print('=====================')
            print()

            try:
                id = int(input('Input Employee ID: '))
                print()
            except:
                print('ID must be a number!')
                continue

            if id not in employees.keys():
                print('ID doesn\'t exist')

            else:
               print_header()
               emp = employees[id]
               name, gender, age, title, dept, salary, exp = emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6]
               print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')

        
        #-------------------------------------------------------------------------------------
        #Filter Employee Data Menu
        elif opt == 3:
            #Define column names
            columns = ['Gender', 'Age', 'Job Title', 'Department', 'Salary ($)', 'Experience', 'Back to display menu']

            #Display menu to input filter category
            print('==========================')
            print('Filter Employee Data')
            print('==========================')
            for col in list(enumerate(columns, 1)):
                print(col[0], col[1])

            #Choose filter
            #Error if input is a string
            try:
                opt = int(input('Choose the category to filter your data: '))
                print()
            except:
                print('Wrong value! Must be a number')
                continue
            
            #If number input is not from the menu
            if opt > 8 or opt == 0:
                print('Choose the number from the menu!')
                continue

            #Go back to main display menu
            if opt == 8:
                break
            
            #Choosing filters based on category
            if opt == 1:
                filter = input('Gender\nM/F: ').upper()
                print()
                print(f'Filtered by Gender: {filter}')
        
            elif opt == 2:
                try:
                    filter_min = int(input('Input minimum age: '))
                    filter_max = int(input('Input maximum age: '))
                except:
                    print('Wrong value! Must be a number')
                    continue
                print()
                print(f'Filtered by Age: {filter_min} to {filter_max}')
                print('Sorted from youngest to oldest')
          

            elif opt == 3:
                filter = input('Enter Job Title:\nManager, Senior Staff, Staff, Engineer, Senior Engineer, Analyst, Senior Analyst\n').title()
                print()
                print(f'Filtered by Job Title: {filter}')
                print('Sorted by Salary, highest to lowest')
            

            elif opt == 4: 
                filter = input('Enter Department Name:\nFinance, Marketing, IT, Production, Sales, HR\n')
                print()
                print(f'Filtered by Job Title: {filter}')
                print('Sorted by Job Title')

            elif opt == 5:
                try:
                    filter_min = int(input('Input minimum annual salary ($): '))
                    filter_max = int(input('Input maximum annual salary ($): '))
                except:
                    print('Wrong value! Must be a number')
                    continue
                print()
                print(f'Filtered by Salary: {filter_min} to {filter_max}')
                print('Sorted from highest to lowest')
                print()

            elif opt == 6: 
                try:
                    filter_min = int(input('Input minimum years of experience: '))
                    filter_max = int(input('Input maximum years of experience: '))
                except:
                    print('Wrong value! Must be a number')
                    continue
                print()
                print(f'Filtered by Experience: {filter_min} to {filter_max}')
                print('Sorted from lowest to highest')
                print()


            #Define filtered list
            filtered = []
            #For loop to find filtered data
            for key,val in employees.items():
                id = key
                name, gender, age, title, dept, salary, exp = val[0], val[1], val[2], val[3], val[4], val[5], val[6]

                emp = [id, name, gender, age, title, dept, salary, exp]
                
                #Filter by Gender
                if opt == 1:
                    if gender == filter:
                        filtered.append(emp)  
                #Filter by Age Group
                elif opt == 2:
                    if age in range(filter_min, filter_max+1):
                        filtered.append(emp) 
                        #Sort from youngest to oldest
                        filtered.sort(key = lambda x: x[3])   
                #Filter by Job Title                   
                elif opt == 3:
                    if title == filter:
                        filtered.append(emp)
                        filtered.sort(key = lambda x: x[6], reverse = True)
                #Filter by Department
                elif opt == 4:
                    if dept == filter:
                        filtered.append(emp)
                        filtered.sort(key = lambda x: x[3])
                #Filter by Salary
                elif opt == 5:
                    if salary in range(filter_min, filter_max+1):
                        filtered.append(emp)
                        filtered.sort(key = lambda x: x[6], reverse=True)
                #Filter by Experience
                elif opt == 6: 
                    if exp in range(filter_min, filter_max+1):
                        filtered.append(emp)
                        filtered.sort(key = lambda x: x[7], reverse=True) 
                else:
                    break

            print_header()
            for emp in filtered:
                id, name, gender, age, title, dept, salary, exp = emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7]
                print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
            
        #-------------------------------------------------------------------------------------
        #Go back to Main Menu
        elif opt == 4:
            break
        
        #Notification for invalid integer value
        else:
            print('Wrong value! Enter an option from the menu: ')
            continue

#----------------------------------Summary Menu Function---------------------------------------------------

#Summary menu options prompt
summary_prompt = '''
=================================
Display Employee Summary
=================================
1. Display Overall Summary
2. Display Summary by Department
3. Back to Main Menu
'''

def summary_menu():
    employees = emp_dict 
    id = [k for k in employees.keys()]
    gender = [val[1] for val in employees.values()] 
    age = [val[2] for val in employees.values()]
    title = [val[3] for val in employees.values()]
    dept = [val[4] for val in employees.values()]
    salary = [val[5] for val in employees.values()]
    exp = [val[6] for val in employees.values()]

    #Function to format dollar sign
    def dollar(num):
        num = f"{num:,}"
        num = f'${num}'
        return num
    
    #Function to add average
    def average(col):
        return sum(col)//len(col) 
    
    #Function to calculate median
    def median(col):
        col_sort = sorted(col)
        n = len(col_sort)
        mid_id = n//2
        #If count of data is odd
        if len(col) % 2 !=1:
            m = col_sort[mid_id]
        else:
            m = (col_sort[mid_id] + col_sort[mid_id - 1])//2
        return m

    #Function to filter employee based on departments
    def filter_dept(dept=None):
        emp_gender = []
        emp_age = []
        emp_salary = []
        emp_exp = []
        for k, v in employees.items():
            if v[4] == dept:
                emp_gender.append(v[1])
                emp_age.append(v[2])
                emp_salary.append(v[5])
                emp_exp.append(v[6])
        return emp_gender, emp_age, emp_salary, emp_exp


    while True:
        print(summary_prompt)
        opt = input('Enter an option: ')

        #Notification error if opt is a string
        try: 
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
        
        #Employee summary menu
        if opt == 1:
            print('\n========================================')
            print(f'{'Employee Summary':^35}')
            print('========================================')
            print(f'Total Departments {len(set(dept)):>14}')
            print(f'{', '.join(set(dept))}')
            print()
            print(f'Total Employees {len(id):>16}')
            print(f'Male Employees {gender.count('M'):>17}')
            print(f'Female Employees {gender.count('F'):>15}')
            print()
            print(f'Average Age {(average(age)):>20}')
            print(f'Oldest Employee Age {max(age):>12}')
            print(f'Median Employee Age {median(age):>12}')
            print(f'Youngest Employee Age {min(age):>10}')
            print()
            print(f'Average Annual Salary {dollar(average(salary)):>10}')
            print(f'Highest Salary {dollar(max(salary)):>17}')
            print(f'Median Salary {dollar(median(salary)):>18}')
            print(f'Lowest Salary {dollar(min(salary)):>18}')
            print()
            print(f'Average Years of Experience {average(exp):>4}')
            print(f'Longest Experience {max(exp):>13}')
            print(f'Median Experience {median(exp):>14}')
            print(f'Shortest Experience {min(exp):>12}')

        #--------------------------------------------------------------------------------------------------------
        #Display Summary by Department Menu
        elif opt == 2:
            #Define department names
            columns = ['Finance', 'Marketing', 'IT', 'Production', 'Sales', 'HR', 'Back to display menu']

            #Display menu to input filter category
            print('==========================')
            print('Choose Department')
            print('==========================')
            for col in list(enumerate(columns, 1)):
                print(col[0], col[1])
            print()

            #Choose filter
            #Error if input is a string
            try:
                opt = int(input('Choose a department: '))
            except:
                print('Wrong value! Must be a number')
                continue
            
            #If number input is not from the menu
            if opt > 7 or opt == 0:
                print('Choose the number from the menu!')
                continue

            #Go back to main display menu
            if opt == 7:
                break

            #Summary of each departments
            if opt == 1:
                print()
                print('================================')
                print('Summary of Finance Department')
                print('================================')
                
                emp_gender, emp_age, emp_salary, emp_exp = filter_dept('Finance')

            elif opt == 2:
                print()
                print('================================')
                print('Summary of Marketing Department')
                print('================================')

                emp_gender, emp_age, emp_salary, emp_exp = filter_dept('Marketing')

            elif opt == 3:
                print()
                print('================================')
                print('Summary of IT Department')
                print('================================')

                emp_gender, emp_age, emp_salary, emp_exp = filter_dept('IT')

            elif opt == 4:
                print()
                print('================================')
                print('Summary of Production Department')
                print('================================')

                emp_gender, emp_age, emp_salary, emp_exp = filter_dept('Production')

            elif opt == 5:
                print()
                print('================================')
                print('Summary of Sales Department')
                print('================================')

                emp_gender, emp_age, emp_salary, emp_exp = filter_dept('Sales')
            
            elif opt == 6:
                print()
                print('==== ===========================')
                print('Summary of HR Department')
                print('================================')

                emp_gender, emp_age, emp_salary, emp_exp = filter_dept('HR')

            print(f'Total Employees {len(emp_gender):>16}')
            print(f'Male Employees {emp_gender.count('M'):>17}')
            print(f'Female Employees {emp_gender.count('F'):>15}')
            print()
            print(f'Average Age {(average(emp_age)):>20}')
            print(f'Oldest Employee Age {max(emp_age):>12}')
            print(f'Median Employee Age {median(emp_age):>12}')
            print(f'Youngest Employee Age {min(emp_age):>10}')
            print()
            print(f'Average Annual Salary {dollar(average(emp_salary)):>10}')
            print(f'Highest Salary {dollar(max(emp_salary)):>17}')
            print(f'Median Salary {dollar(median(emp_salary)):>18}')
            print(f'Lowest Salary {dollar(min(emp_salary)):>18}')
            print()
            print(f'Average Years of Experience {average(emp_exp):>4}')
            print(f'Longest Experience {max(emp_exp):>13}')
            print(f'Median Experience {median(emp_exp):>14}')
            print(f'Shortest Experience {min(emp_exp):>12}')

        #Go back to main menu
        elif opt == 3:
            break

        else:
            print('Wrong value! Enter an option from the menu: ')
            continue

#-----------------------------------Add Employee Function--------------------------------------------------

add_prompt = '''
===========================
Add Employee Menu
===========================
1. Add Employee Using ID
2. Back to Main Menu
'''

def add_menu():
    employees = emp_dict
  
    while True:
        #Display Add Menu
        print(add_prompt)
        opt = input('Enter an option: ')
        print()

        #Notification error if opt is a string
        try: 
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
            continue
        
        ##########################################################
        #Input Employee by ID
        if opt == 1:
            print('==========================')
            print('Add Employee by ID')
            print('==========================')
            print()

            #while True:
            try:
                id = int(input('Insert employee ID (0 to quit): '))
                print()
            except:
                print('Please enter a number')
                continue
                
            if id == 0:
                break
            if id in employees.keys():
                print('Employee ID already exists! Enter another value')
                continue

            elif id not in employees.keys():
                name = input('Enter employee name: ').title()
                for k, v in employees.items():
                    if name == v[0]:
                        print()
                        print('There is an employee with this name. Is this the same person?')
                        print()
                        print_header()
                        name, gender, age, title, dept, salary, exp = v[0], v[1], v[2], v[3], v[4], v[5], v[6]
                        print(f'| {k} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
                        print()
                        resp = input('y/n: ')
                        print()
                        if resp == 'y':
                            print('The employee is already in the database.')
                            break
                        # else:
                        #     continue
                    
                    else:
                        try:
                            age = int(input('Enter employee age: '))
                            gender = input('Enter employee gender (M/F): ').title()
                            print()
                            print('Job Title: Manager, Senior Staff, Staff, Engineer, Senior Engineer, Analyst, Senior Analyst')
                            title = input('Enter employee job title: ').title()
                            print()
                            print('Department: Finance, Marketing, IT, Production, Sales, HR')
                            dept = input('Enter employee job department: ')
                            dept = dept.title() if len(dept) > 2 else dept.upper()
                            salary = int(input('Enter employee annual salary ($): '))
                            exp = int(input('Enter number of employee\'s experience with the company: '))
                        except:
                            print('Wrong value! Needs to be a number')
                            break

                        #Confirmation to add employee data
                        print()
                        print_header()
                        print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
                        print()
                        conf = input('Confirm to input employee data to database (y/n): ')
                        if conf == 'y':
                        #Insert employee data to dictionary
                            employees[id] = [name, age, gender, title, dept, salary, exp]

                            #Display new employee data
                            print('Employee added to database\n')
                            break

                        else: 
                            break
  
        #--------------------------------------------------------------------------------------------------
        #Go back to main menu
        elif opt == 2:
            break

        else:
            print('Wrong value! Enter an option from the menu')
            continue

#-----------------------------------Update Menu Function---------------------------------------------------

update_prompt = '''
===========================================
Update Employee Menu
===========================================
1. Update Employee Data using ID
2. Update Employee Salary (per Department)
3. Back to Main Menu
'''

def update_menu():
    employees = emp_dict

    while True:
        print(update_prompt)
        opt = input('Enter an option: ')

        #Notification error if opt is a string
        try: 
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
        
        #Update employee using ID 
        if opt == 1:
            print()
            print('===============================')
            print('Update Employee Data')
            print('===============================')
            print()

            try:
                id = int(input('Input Employee ID: '))
            except:
                print('ID must be a number!')
                continue

            #Display current employee data
            if id in employees.keys():
                print()
                print_header()
                emp = employees[id]
                name, gender, age, title, dept, salary, exp = emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6]
                print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
                print()
                
                while True:
                    #Printing the options of employee data (columns) to choose
                    columns = ['Name', 'Gender', 'Age', 'Job Title', 'Department', 'Salary', 'Experience', 'Go back to previous menu']
                    for col in list(enumerate(columns, 1)):
                        print(f'{col[0]}. {col[1]}')

                    try:
                        print()
                        opt = int(input('Enter the data that you want to update: '))
                        print()
                    except:
                        print('Wrong value! Must be a number')
                        continue

                    if opt > 8:
                        print('Choose the number from the menu!')
                        continue

                    if opt == 8:
                        break

                    print(columns[opt-1])
                    data = input('Input the new data: ')

                    #Confirmation of adding data
                    print()
                    print('Current data:')
                    print()
                    print_header()
                    print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
                    print()
                    print(f'Confirm the change of {columns[opt-1]} value to {data}')
                    conf = input('y/n: ')
                    if conf == 'y':
                        
                        #Change the data according to the column chosen
                        #Name column
                        if opt == 1:
                            name = data.title()
                        #Gender column
                        elif opt == 2:
                            gender = data.title()
                        #Age column -> change to int
                        elif opt == 3:
                            try:
                                age = int(data)
                            except:
                                print('Age must be a number!')
                        #Job title column
                        elif opt == 4:
                            title = data.title()
                        #Department column
                        elif opt == 5:
                            dept = data.title() if len(data) > 2 else data.upper()
                        #Salary column -> change to int
                        elif opt == 6:
                            try:
                                salary = int(data)
                            except:
                                print('Salary must be a number!')
                        #Experience column -> change to int
                        elif opt == 7:
                            try:
                                exp = int(data)
                            except:
                                print('Experience years must be a number!')

                        print()
                        print_header()
                        print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
                        print()
                        print('Employee data successfully updated')
                        break

                    else:
                        break

           #Notification if ID doesn't exist     
            else:
                print('ID doesn\'t exist!')
                continue
        
        #------------------------------------------------------------------------------------
        #Update employee salary data per department
        #Case: Raise applied to all employees in a department
        elif opt == 2: 
            print()
            print('===============================')
            print('Update Department Salary')
            print('===============================')
            print()

            columns = ['Finance', 'Marketing', 'IT', 'Production', 'Sales', 'HR', 'Back to display menu']

            #Display menu to input filter category
            print('Filter Employee Data by ')
            for col in list(enumerate(columns, 1)):
                print(col[0], col[1])
            print()

            try:    
                dept_raise = int(input('Please choose the department: '))
                if dept_raise == 7:
                    continue
                raise_pct = int(input('Enter the increase of raise in x% (% not included): '))
            except:
                print('Please enter a number!')
                continue


            filtered = []
            for id, val in employees.items():
                #Department column = val[4]
                #Salary column = val[5]
                # dept_col = val[4]
                # salary = val[5]
                emp = employees[id]
                name, gender, age, title, dept, salary, exp = emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6]

                if dept == columns[dept_raise-1]:
                    print()
                    print_header()
                    print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
                    val[5] = int(salary * (1 + raise_pct/100))
                    print(f'Updated salary: {val[5]}')
                    salary = val[5]
                    emp = [id, name, gender, age, title, dept, salary, exp]
                    filtered.append(emp)
                    #Confirmation
                    conf = input('\nConfirm to update the salary (y/n): ')
                    if conf == 'y':
                        print()
                        print('Updated employee data saved to the database\n')
                    
                    else:
                        val[5] = salary
                        continue

            print()
            print_header()
            for emp in filtered:
                id, name, gender, age, title, dept, salary, exp = emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7]
                print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
       
        #Go back to main menu
        elif opt == 3:
            break
        
        #Option an integer not in menu
        else:
            print('Wrong value! Enter an option from the menu: ')
            continue

#-----------------------------------Delete Menu Function---------------------------------------------------
#Delete display prompts
del_prompt = '''
========================
Delete Employee Menu
========================
1. Delete Employee
2. Back to Main Menu
'''

def delete_menu():
    employees = emp_dict

    while True:
        print(del_prompt)
        opt = input('Enter an option: ')
        print()

        #Notification error if opt is a string
        try: 
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
            continue
        
        #Delete employee menu
        if opt == 1:
            print('==========================')
            print('Delete Employee')
            print('==========================')
            print()
            print('Employee ID = 10XX')
            print()

            #Input ID to delete
            try:
                id = int(input('Input Employee ID: '))
                print()
            except:
                print('ID needs to be a number')

            if id in employees.keys():
                #Display data to delete
                print_header()
                emp = employees[id]
                name, gender, age, title, dept, salary, exp = emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6]
                print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')

                #Confirm deletion
                resp = input('\nConfirm to delete the employee data (y/n): ')
                if resp == 'y':
                    employees.pop(id)
                    print('\nEmployee data succesfully deleted.')
                else:
                    continue

            #Notification if data doesn't exist 
            else:
                print('ID doesn\'t exist!')
                continue
                        
        #Go back to main menu
        elif opt == 2:
            break
        
        else:
            print('Wrong value! Enter an option from the menu: ')
            continue

#-----------------------------------Main Menu Function-----------------------------------------------------

main_prompt = '''
===================================
Employee Data Main Menu
===================================
1. Display and Filter Employee Data
2. Display Employee Data Summary
3. Add New Employee Data
4. Updata Employee Data
5. Delete Employee Data
6. Close Program
''' 

def main_menu():
    while True:
        print(main_prompt)
        option = input('Enter the menu you want to choose: ')

        #Raise error if input is not an integer
        try:
            option = int(option)
             #Print error message if option is out of range
            if option > 6 or option == 0:
                print('Option out of range! Please enter a number from the menu: ')
                continue

            #Display Menu
            elif option == 1:
                display_menu()
  
            #Summary Menu
            elif option == 2:
                summary_menu()

            #Create New Employee Menu
            elif option == 3:
                add_menu()

            #Update Employee Menu
            elif option == 4:
                update_menu()

            #Delete Employee Menu
            elif option == 5:
                print('Delete Employee Data')

            #End Program
            else:
                break  

        except:
            print('Wrong input! Please enter a number') 

#Run program
main_menu()