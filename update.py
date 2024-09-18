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

#Menu display prompts
update_prompt = '''
Update Employee Menu
1. Update Employee Data using ID
2. Update Employee Salary (per Department)
3. Back to Main Menu
'''
# cols = [[0, 'Name'], [1, 'Gender'], [2, 'Age'], [3, 'Job Title'], 
#         [4, 'Department'], [5, 'Salary'], [6, 'Experience'], [7, 'Go back to previous menu']]

def update_menu(emp_dict):
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
            try:
                id = int(input('Input Employee ID: '))
            except:
                print('ID must be a number!')
                continue

            #Display current employee data
            if id in employees.keys():
                #CHANGE HEADERS
                print(str(id), ' '.join(list(str(emp) for emp in employees[id])))

                while True:
                    #Printing the options of employee data (columns) to choose
                    columns = ['Name', 'Gender', 'Age', 'Job Title', 'Department', 'Salary', 'Experience', 'Go back to previous menu']
                    for col in list(enumerate(columns, 1)):
                        print(f'{col[0]}. {col[1]}')

                    try:
                        opt = int(input('Enter the data that you want to update: '))
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
                    print('Current data:')
                    #CHANGE HEADERS
                    print(str(id), ' '.join(list(str(emp) for emp in employees[id])))
                    print(f'Confirm the change of {columns[opt-1]} value to {data}')
                    conf = input('y/n: ')
                    if conf == 'y':
                        
                        #Change the data according to the column chosen
                        #Name column
                        if opt == 1:
                            employees[id][0] = data.title()
                        #Gender column
                        elif opt == 2:
                            employees[id][1] = data.title()
                        #Age column -> change to int
                        elif opt == 3:
                            employees[id][2] = int(data)
                        #Job title column
                        elif opt == 4:
                            employees[id][3] = data.title()
                        #Department column
                        elif opt == 5:
                            employees[id][4] = data.title() if len(data) > 2 else data.upper()
                        #Salary column -> change to int
                        elif opt == 6:
                            employees[id][5] = int(data)
                        #Experience column -> change to int
                        elif opt == 7:
                            employees[id][6] = int(data)

                        #CHANGE HEADERS
                        print(str(id), ' | '.join(list(str(emp) for emp in employees[id])))
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
            departments = [[0, 'Finance'], [1, 'Marketing'], [2, 'IT'], [3, 'Production'], 
                           [4, 'Sales'], [5, 'HR']]
            
            for dept in departments:
                print(f'{dept[0]}. {dept[1]}')
            
            dept_raise = int(input('Please choose the department: '))
            raise_pct = int(input('Enter the increase of raise in x% (% not included): '))
            
            for key, val in employees.items():
                #Department column = val[4]
                #Salary column = val[5]
                dept_col = val[4]
                salary = val[5]
                
                if dept_col == departments[dept_raise][1]:
                    print(str(key), ' '.join(list(str(emp) for emp in employees[key])))
                    val[5] = int(salary * (1 + raise_pct/100))
                    print(f'Updated salary: {val[5]}')
                    #print(str(key), ' '.join(list(str(emp) for emp in employees[key])))
                    
                    #Confirmation
                    conf = input('\nConfirm to update the salary (y/n): ')
                    if conf == 'y':
                        print('Updated employee data saved to the database\n')
   
                    else:
                        val[5] = salary
                        continue
       
        #Go back to main menu
        elif opt == 3:
            break
        
        #Option an integer not in menu
        elif opt > 3 or opt == 0:
            print('Wrong value! Enter an option from the menu: ')

update_menu(emp_dict)