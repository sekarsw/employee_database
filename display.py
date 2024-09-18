#Employees dictionary
emp_dict = {
       1001: ['Josh Allen', 'M', 30, 'Senior Staff', 'Production', 50000, 5], 
       1002: ['Laura Kennedy', 'F', 25, 'Staff', 'Marketing', 35000, 2], 
       1003: ['Tyler Crosby', 'M', 35, 'Manager', 'IT', 120000, 10], 
       1004: ['Michael Scott', 'M', 32, 'Engineer', 'IT', 85000, 8], 
       1005: ['David Williams', 'M', 27, 'Staff', 'Sales', 50000, 3], 
       1006: ['Alex Kim', 'M', 29, 'Engineer', 'IT', 40000, 3], 
       1007: ['Michelle Tomlinson', 'F', 31, 'Senior Staff', 'Marketing', 50000, 4], 
       1008: ['James Smith', 'M', 45, 'Manager', 'Production', 92000, 18], 
       1009: ['Angelina Lee', 'F', 38, 'Manager', 'Marketing', 80000, 10], 
       1010: ['Bella Washington', 'F', 24, 'Staff', 'HR', 32000, 1], 
       1011: ['Wendy Adams', 'F', 29, 'Senior Staff', 'HR', 45000, 5], 
       1012: ['Tom Benson', 'M', 40, 'Senior Engineer', 'IT', 98000, 12], 
       1013: ['Michael Brady', 'M', 39, 'Engineer', 'IT', 87000, 9], 
       1014: ['Katie Brown', 'F', 32, 'Senior Analyst', 'Finance', 78000, 4], 
       1015: ['Karen Scott', 'F', 34, 'Manager', 'HR', 80000, 10], 
       1016: ['Natasha Jordan', 'F', 28, 'Analyst', 'Marketing', 48000, 5], 
       1017: ['Amy Wilde', 'F', 48, 'Manager', 'Finance', 130000, 24], 
       1018: ['Farah Anissa', 'F', 36, 'Senior Analyst', 'Finance', 75000, 10], 
       1019: ['Muhammad Idris', 'M', 23, 'Staff', 'Production', 29000, 1], 
       1020: ['Jason Chen', 'M', 24, 'Engineer', 'IT', 35000, 2], 
       1021: ['Jamie Jefferson', 'M', 26, 'Staff', 'HR', 30000, 4], 
       1022: ['Melanie Anderson', 'F', 24, 'Analyst', 'Finance', 28000, 1], 
       1023: ['Tessa Bailey', 'F', 45, 'Senior Staff', 'Sales', 74000, 17], 
       1024: ['Eva Madison', 'F', 38, 'Senior Engineer', 'IT', 88000, 12], 
       1025: ['Hailey Silver', 'F', 40, 'Senior Analyst', 'Finance', 70000, 15], 
       1026: ['Julia Foster', 'F', 43, 'Senior Analyst', 'Marketing', 68000, 14], 
       1027: ['Kevin Jones', 'M', 52, 'Manager', 'Sales', 100000, 26], 
       1028: ['Irene Garner', 'F', 34, 'Senior Staff', 'Sales', 65000, 10], 
       1029: ['Jennifer Li', 'F', 31, 'Senior Engineer', 'IT', 58000, 7], 
       1030: ['Diana Torres', 'F', 27, 'Analyst', 'Marketing', 41000, 4]
       }

#Display menu options prompt
display_prompt = '''
Display Employee Data
1. Display All Employee Data
2. Find Employee by ID
3. Filter Employee Data
4. Back to Main Menu
'''

def display_menu(emp_dict = None):
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
            print('Display All Data')
            for k,v in employees.items():
                print(k, '      '.join(str(val) for val in list(v)))

        #-------------------------------------------------------------------------------------
        #Display Find Employee by ID Menu
        elif opt == 2:
            print('Find Employee by ID')
            try:
                id = int(input('Input Employee ID: '))
            except:
                print('ID must be a number!')
                continue

            if id not in employees.keys():
                print('ID doesn\'t exist')

            else:
               print(str(id), '     '.join(list(str(emp) for emp in employees[id])))

        
        #-------------------------------------------------------------------------------------
        #Filter Employee Data Menu
        elif opt == 3:
            #Define column names
            columns = ['Gender', 'Age', 'Job Title', 'Department', 'Salary', 'Experience', 'Back to display menu']

            #Display menu to input filter category
            print('Filter Employee Data')
            print('--------------------------')
            for col in list(enumerate(columns, 1)):
                print(col[0], col[1])

            #Choose filter
            #Error if input is a string
            try:
                opt = int(input('Choose the category to filter your data: '))
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
            elif opt == 2:
                filter_min = int(input('Input minimum age: '))
                filter_max = int(input('Input maximum age: '))
            elif opt == 3:
                filter = input('Job Title\nManager, Senior Staff, Staff, Engineer, Senior Engineer, Analyst, Senior Analyst\n').title()
            elif opt == 4: 
                filter = input('Department\nFinance, Marketing, IT, Production, Sales, HR\n')
            elif opt == 5:
                filter_min = int(input('Input minimum annual salary ($): '))
                filter_max = int(input('Input maximum annual salary ($): '))
            elif opt == 6: 
                filter_min = int(input('Input minimum years of experience: '))
                filter_max = int(input('Input maximum years of experience: '))


            #Define filtered list
            filtered = []
            #For loop to find filtered data
            for key,val in employees.items():
                id = key
                name = val[0]
                gender = val[1]
                age = val[2]
                title = val[3]
                dept = val[4]
                salary = val[5]
                exp = val[6]

                emp = [id, name, gender, age, title, dept, salary, exp]
                
                #Filter by Gender
                if opt == 1:
                    if gender == filter:
                        filtered.append(emp)      
                elif opt == 2:
                    if age in range(filter_min, filter_max+1):
                        filtered.append(emp)
                elif opt == 3:
                    if title == filter:
                        filtered.append(emp)
                elif opt == 4:
                    if dept == filter:
                        filtered.append(emp)
                elif opt == 5:
                    if salary in range(filter_min, filter_max+1):
                        filtered.append(emp)
                elif opt == 6: 
                    if exp in range(filter_min, filter_max+1):
                        filtered.append(emp)

                else:
                    break
            print(filtered)
        
        #-------------------------------------------------------------------------------------
        #Go back to Main Menu
        elif opt == 4:
            break
        
        #Notification for invalid integer value
        else:
            print('Wrong value! Enter an option from the menu: ')
            continue

display_menu(emp_dict)


    