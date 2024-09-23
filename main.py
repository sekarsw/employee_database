#Dictionary if database csv files are not downloaded

emp_dict = {1001: ['Josh Allen', 'M', 30, 'Senior Staff', 'Production', 50000, 5], 1002: ['Laura Kennedy', 'F', 25, 'Staff', 'Marketing', 35000, 2], 1003: ['Tyler Crosby', 'M', 35, 'Manager', 'IT', 120000, 10], 1004: ['Michael Scott', 'M', 32, 'Engineer', 'IT', 85000, 8], 1005: ['David Williams', 'M', 27, 'Staff', 'Sales', 50000, 3], 1006: ['Alex Kim', 'M', 29, 'Engineer', 'IT', 40000, 3], 1007: ['Michelle Herbert', 'F', 31, 'Senior Staff', 'Marketing', 50000, 4], 1008: ['James Smith', 'M', 45, 'Manager', 'Production', 92000, 18], 1009: ['Angelina Lee', 'F', 38, 'Manager', 'Marketing', 80000, 10], 1010: ['Bella Washington', 'F', 24, 'Staff', 'HR', 32000, 1], 1011: ['Wendy Adams', 'F', 29, 'Senior Staff', 'HR', 45000, 5], 1012: ['Tom Benson', 'M', 40, 'Senior Engineer', 'IT', 98000, 12], 1013: ['Michael Brady', 'M', 39, 'Engineer', 'IT', 87000, 9], 1014: ['Katie Brown', 'F', 32, 'Senior Analyst', 'Finance', 78000, 4], 1015: ['Karen Scott', 'F', 34, 'Manager', 'HR', 80000, 10], 1016: ['Natasha Jordan', 'F', 28, 'Analyst', 'Marketing', 48000, 5], 1017: ['Amy Wilde', 'F', 48, 'Manager', 'Finance', 130000, 24], 1018: ['Farah Anissa', 'F', 36, 'Senior Analyst', 'Finance', 75000, 10], 1019: ['Muhammad Idris', 'M', 23, 'Staff', 'Production', 29000, 1], 1020: ['Jason Chen', 'M', 24, 'Engineer', 'IT', 35000, 2], 1021: ['Jamie Jefferson', 'M', 26, 'Staff', 'HR', 30000, 4], 1022: ['Melanie Anderson', 'F', 24, 'Analyst', 'Finance', 28000, 1], 1023: ['Tessa Bailey', 'F', 45, 'Senior Staff', 'Sales', 74000, 17], 1024: ['Eva Madison', 'F', 38, 'Senior Engineer', 'IT', 88000, 12], 1025: ['Hailey Silver', 'F', 40, 'Senior Analyst', 'Finance', 70000, 15], 1026: ['Julia Foster', 'F', 43, 'Senior Analyst', 'Marketing', 68000, 14], 1027: ['Kevin Jones', 'M', 52, 'Manager', 'Sales', 100000, 26], 1028: ['Irene Garner', 'F', 34, 'Senior Staff', 'Sales', 65000, 10], 1029: ['Jennifer Li', 'F', 31, 'Senior Engineer', 'IT', 58000, 7], 1030: ['Diana Torres', 'F', 27, 'Analyst', 'Marketing', 41000, 4]}
train_dict = {'T1': ['Leadership', 10, 'Available', ['1001', '1004', '1006', '1007', '1009', '1020', '1024', '1015']], 'T2': ['Data Science', 10, 'Available', ['1002', '1003', '1010', '1014', '1019']], 'T3': ['Computer Skills', 8, 'Open Soon', ['']], 'T4': ['Safety', 10, 'Completed', ['1015', '1005', '1001', '1002', '1017', '1016', '1023', '1022', '1007', '1017']], 'T5': ['Time Management', 8, 'Completed', ['1024', '1028', '1026', '1022', '1014', '1017', '1006', '1001']]}

#-----------------------------------Import Employees Data From CSV-----------------------------------------
#Uncomment the next lines if csv file is downloaded

# import csv

# #Create dictionary from csv file
# file = 'data/employees.csv'
# emp_list = []

# with open(file, 'r') as f:
#     csv_reader = csv.reader(f)
#     data = list(csv_reader)
#     for row in data[1:]:
#         emp_list.append(row)


# #Dictionary
# #Employee ID
# dict_keys = [emp[0] for emp in emp_list]
# #Rest of employee data
# dict_values = [emp[1:] for emp in emp_list]

# #Convert age, salary, experience to integers
# for dict in dict_values:
#     dict[2] = int(dict[2])
#     dict[5] = int(dict[5])
#     dict[6] = int(dict[6])

# #zip to create a tuple for each value in dict_keys and dict_values
# emp_dict = {int(k):v for k,v in list(zip(dict_keys, dict_values))}

#----------------------------Import Training Data from CSV------------------------------------------------

# #Create dictionary from csv file
# file = 'data/trainings.csv'
# train_list = []

# with open(file, 'r') as f:
#     csv_reader = csv.reader(f, delimiter=';')
#     data = list(csv_reader)
#     for row in data[1:]:
#         id = row[4:]
#         rows = row[0:4]
#         rows.append(id) 
#         train_list.append(rows) 

# #Dictionary
# dict_keys = [train[0] for train in train_list]
# dict_values = [train[1:] for train in train_list]

# for dict in dict_values:
#     dict[1] = int(dict[1])


# train_dict = {k:v for k,v in list(zip(dict_keys, dict_values))}

#-------------------------------------Supplemental Functions----------------------------------------------

#Function to add table header -> Employee Database
def print_header():
    print(f'| ID   | {'Name':<20} | {'Gender':<7} | {'Age':<4} | {'Job Title':<15} | {'Department':<15} | {'Salary($)':<8}| {'Exp':>3}  |')
    print('------------------------------------------------------------------------------------------------------')  


#Function to add table header -> Training Database
def train_header():
    print(f'| ID  | {'Topic':<20} | {'Quota':<7} | {'Status':<10} | {'Registered Employees':<50} | ')
    print('----------------------------------------------------------------------------------------------------------')  


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
                id = int(input('Input Employee ID\n(ID = 10XX): '))
                print()
            except:
                print('ID must be a number!')
                continue

            if id not in employees.keys():
                print('ID doesn\'t exist')

            else:
               print(f'Employee ID: {id}')
               print_header()
               emp = employees[id]
               name, gender, age, title, dept, salary, exp = emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6]
               print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')

        
        #-------------------------------------------------------------------------------------
        #Filter Employee Data Menu
        elif opt == 3:
            #Define column names
            columns = ['Gender', 'Age', 'Job Title', 'Department', 'Salary $', 'Experience', 'Back to display menu']

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
                filter = filter.title() if len(filter) > 2 else filter.upper()
                print()
                print(f'Filtered by Department: {filter}')
                print('Sorted by Experience')

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
                print('Sorted from longest to shortest')
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
                #Filter by Age Group, Sorted by Age
                elif opt == 2:
                    if age in range(filter_min, filter_max+1):
                        filtered.append(emp) 
                        #Sort from youngest to oldest
                        filtered.sort(key = lambda x: x[3])   
                #Filter by Job Title, Sorted by Salary                  
                elif opt == 3:
                    if title == filter:
                        filtered.append(emp)
                        filtered.sort(key = lambda x: x[6], reverse = True)
                #Filter by Department, Sorted by Experience
                elif opt == 4:
                    if dept == filter:
                        filtered.append(emp)
                        filtered.sort(key = lambda x: x[7], reverse=True)
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
        #Sum items in list and divide by number of items in list
        return sum(col)//len(col) 
    
    #Function to calculate median
    def median(col):
        #Sort the column 
        col_sort = sorted(col)
        n = len(col_sort)
        #Find the index of the middle value
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
                id = int(input('Insert employee ID\n(ID = 10XX)\n(0 to quit): '))
                print()
            except:
                print('Please enter a number')
                continue
                
            if id == 0:
                continue
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
                            employees[id] = [name, gender, age, title, dept, salary, exp]

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
                id = int(input('Input Employee ID\n(ID = 10XX): '))
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

            #Empty filter list for the employees in the chosen department
            filtered = []
            for id, val in employees.items():
                #Department column = val[4]
                #Salary column = val[5]
                # dept_col = val[4]
                # salary = val[5]
                emp = employees[id]
                name, gender, age, title, dept, salary, exp = emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6]

                #Check if department name is equal to input value
                if dept == columns[dept_raise-1]:
                    print()
                    print_header()
                    print(f'| {id} | {name:<20} | {gender:<7} | {str(age):<4} | {title:<15} | {dept:<15} | {str(salary):>8} | {str(exp):^4} |')
                    #Updated salary formula
                    upd_salary = int(salary * (1 + raise_pct/100))
                    print(f'Updated salary: {upd_salary}')
                    #Confirmation to update salary
                    #Will check for each employee
                    conf = input('\nConfirm to update the salary (y/n): ')
                    if conf == 'y':
                        salary = upd_salary
                        emp = [id, name, gender, age, title, dept, salary, exp]

                        filtered.append(emp)
                        print()
                        print('Updated employee data saved to the database\n')
                    #To show if employees did not get raise
                    else:
                        emp = [id, name, gender, age, title, dept, salary, exp]
                        filtered.append(emp)
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
                    #Remove employee
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

#-----------------------------------Employee Training Menu Function---------------------------------------
trainings_prompt = '''
=======================
Employee Training
=======================
1. Display Training List
2. Add Training Data
3. Update Training Data
4. Delete Training Data
5. Add Employee to Training
6. Remove Employee from Training
7. Back to Main Menu
'''

def training_menu():
    trainings = train_dict
    employees = emp_dict

    while True:
        print(trainings_prompt)

        #Input menu number
        opt = input('Enter an option: ')

        #Error notification if input is a string
        try:
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
            continue
        
        #Display Training List
        if opt == 1:
            print()
            print('===========================')
            print('Display Training Data')
            print('===========================')
            print()
            train_header()
            for k,v in trainings.items():
                topic, quota, status, emps = v[0], v[1], v[2], v[3]
                print(f'| {k}  | {topic:<20} | {str(quota):<7} | {status:<10} | {' '.join(emps):<50} |')
            print()

        #Add Training Program-------------------------------------------------------------------------------
        elif opt == 2:
            print()
            print('===========================')
            print('Add Training Data')
            print('===========================')
            print()
            id = input('Enter training ID\nID format\n(Tx x = number): ').upper()
            print()

            #Check if training id exist
            if id in trainings.keys():
                print('ID already exists! Please enter another ID')
                continue
            
            else:
                topic = input('Enter training topic: ')
                try:
                    quota = int(input('Enter training quota: '))
                except:
                    print('Wrong value! Please enter a number.')
                #Check the training program status
                status = input('Is this program already available for registration? y/n: ').lower()
                if status == 'y':
                    status = 'Available'
                else: 
                    status = 'Open Soon'
                #Set employee id as empty list that will be filled by the Add Employee Function
                emps = []

                #Display the training data
                print()
                train_header()
                print(f'| {id}  | {topic:<20} | {str(quota):<7} | {status:<10} | {' '.join(emps):<50} |')
                print()

                #Confirmation to add datain to the database
                conf = input('Confirm to input the training program into the database? y/n: ').lower()
                if conf == 'y':
                    trainings[id] = [topic, quota, status, emps]
                    print('Training program added into the database.')
                else:
                    continue
                    
        #Update Training Program------------------------------------------------------------------------------
        elif opt == 3:
            print()
            print('===================')
            print('Update Training')
            print('===================')
            print()

            id = input('Input the training program ID to update\nID format\n(Tx x = number): ').upper()
            print()
            
            
            if id in trainings.keys():
                #Display current training data
                train = trainings[id]
                topic, quota, status, emps = train[0], train[1], train[2], train[3]

                print()
                print('Current Data: ')
                train_header()
                print(f'| {id}  | {topic:<20} | {str(quota):<7} | {status:<10} | {' '.join(emps):<50} |')

                while True:
                    #Display options for the field to update
                    cols = ['Topic', 'Quota', 'Status', 'Back to Menu']
                    for col in list(enumerate(cols, 1)):
                        print(col[0], col[1])

                    #Raise error message if input value is wrong
                    try:
                        opt = int(input('Choose the column you want to update: '))
                        print()
                    except:
                        print('Wrong value! Please enter a number from the menu.')
                        continue
                    
                    #Go back to previous men
                    if opt == 4:
                        break

                    #Wrong number input
                    if opt > 4 or opt == 0:
                        print('Choose a number from the menu!')
                        continue

                    #Display the field name to change
                    print(cols[opt-1])
                    #Input the new data
                    data = input('Enter the new data: ')

                    print(f'Confirm the change of {cols[opt-1]} value to {data}')
                    conf = input('y/n: ')
                    #Change the data to the value chosen
                    if conf == 'y':                   
                        #Update Topic
                        if opt == 1:
                            topic = data.title()
                        #Update Quota
                        elif opt == 2:
                            quota = int(data)
                        #Update Status
                        elif opt == 3:
                            status = data.title()

                        print()
                        train_header()
                        print(f'| {id}  | {topic:<20} | {str(quota):<7} | {status:<10} | {' '.join(emps):<50} |')
                        print('Data succesfully updated!')
                    else: 
                        continue


            #Notification if ID doesn't exist
            else:
                print('Training ID doesn\'t exist!')

        #Delete Training Program---------------------------------------------------------------------
        elif opt == 4:
            print()
            print('===================')
            print('Delete Training')
            print('===================')
            print()
            id = input('Input the training program ID to remove\nID format\n(Tx x = number): ').upper()
            print()
            if id in trainings.keys():
                train = trainings[id]
                topic, quota, status, emps = train[0], train[1], train[2], train[3]
                #Print data to remove
                train_header()
                print(f'| {id}  | {topic:<20} | {str(quota):<7} | {status:<10} | {' '.join(emps):<50} |')

                #Confirm deletion of training data
                print()
                conf = input('Confirm to delete this data? y/n: ').lower()
                if conf == 'y':
                    trainings.pop(id)
                    print()
                    print('Training program removed from the database.')
                else:
                    continue
            else:
                print('Training ID doesn\'t exist!')

        #Add Employee to a Training--------------------------------------------------
        elif opt == 5:
            print()
            print('================')
            print('Add Employee')
            print('================')
            print()
            
            #Display training list
            train_header()
            for k,v in trainings.items():
                topic, quota, status, emps = v[0], v[1], v[2], v[3]
                print(f'| {k}  | {topic:<20} | {str(quota):<7} | {status:<10} | {' '.join(emps):<50} |')

            print()
            train_id = input('Enter the training program ID: ').title()
            print()

            #Check if training id exists
            if train_id in trainings.keys():   
                train = trainings[train_id]
                topic, quota, status, emps = train[0], train[1], train[2], train[3]         

                #Notification if training is already completed
                if status == 'Completed':
                    print('Training already concluded. Please register to another program')
                #Notification if training is not open for registration
                elif status == 'Open Soon':
                    print('Registration is not yet open.')
                #Notification if program is full
                elif len(emps) == quota:
                    print('This program is already full.')
                #Input employee ID
                else:
                    try:
                        emp_id = int(input('Enter the employee ID to register to the program\nID format 10XX: '))
                        print()
                    except:
                        print('Wrong value! Employee ID must be a number')
                        continue

                    #Check if Employee Exist in Employee Database
                    if emp_id in employees.keys():                     
                        #Check if Employee ID is already registered
                        if str(emp_id) in emps:
                            print('Employee ID already registered!')
                            continue
                        else:
                            #Confirm the registration of the employee
                            conf = input(f'Confirm the registration of employee {emp_id} to training program {train_id} {topic}?\ny/n: ').lower()
                            print()
                            if conf == 'y':
                                #Append Employee ID to Registered Employees List
                                emps.append(str(emp_id))
                                #Display Data
                                train_header()
                                print(f'| {train_id}  | {topic:<20} | {str(quota):<7} | {status:<10} | {' '.join(emps):<50} |')
                            else:
                                continue

                    else:
                        print('Employee ID doesn\'t exist!')

            else:
                print('Training ID doesn\'t exist!')

        #Delete Employee From a Training------------------------------------------------------------
        elif opt == 6:
            print('================')
            print('Delete Employee')
            print('================')
            print()
            
            #Display training list
            train_header()
            for k,v in trainings.items():
                topic, quota, status, emps = v[0], v[1], v[2], v[3]
                print(f'| {k}  | {topic:<20} | {str(quota):<7} | {status:<10} | {' '.join(emps):<50} |')
            print()

            train_id = input('Enter the training program ID: ').upper()
            print()
            
            #Check if training program exists
            if train_id in trainings.keys():   
                train = trainings[train_id]
                topic, quota, status, emps = train[0], train[1], train[2], train[3]         
                #Input employee ID
                try:
                    emp_id = int(input('Enter the employee ID to remove from the program\nID format 10XX: '))
                    print()
                except:
                    print('Wrong value! Employee ID must be a number')
                    continue

                #Check if Employee Exist in Employee Database
                if emp_id in employees.keys():                     
                    #Check if Employee ID is not registered
                    if str(emp_id) not in emps:
                        print('Employee ID is not registered in this program!')
                        continue
                    else:
                        #Confirmation to remove employee data
                        conf = input(f'Confirm the removal of employee {emp_id} from the program? y/n :').lower()
                        if conf == 'y':
                            #Remove Employee ID
                            emps.remove(str(emp_id))
                            #Display Data
                            train_header()
                            print(f'| {train_id}  | {topic:<20} | {str(quota):<7} | {status:<10} | {' '.join(emps):<50} |')
                        else:
                            continue

                else:
                    print('Employee ID doesn\'t exist!')
                    continue

            else:
                print('Training ID doesn\'t exist!')
       
        #Go back to main menu
        elif opt == 7:
            break

        #Notification for invalid integer value
        else:
            print('Wrong value! Enter an option from the menu: ')

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
6. Employee Training 
7. Close Program
''' 

def main_menu():
    while True:
        print(main_prompt)
        option = input('Enter the menu you want to choose: ')

        #Raise error if input is not an integer
        try:
            option = int(option)
               
        except:
            print('Wrong input! Please enter a number') 
            continue

    #Print error message if option is out of range
        if option > 7 or option == 0:
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
            delete_menu()

        #Employee Training Menu
        elif option == 6:
            training_menu()
            
        #End Program
        else:
            break

#Run program
main_menu()