import csv

#Create dictionary from csv file
file = 'employees.csv'
header = []
emp_list = []

with open(file, 'r', encoding='utf-8-sig') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    header = data[0]
    for row in data[1:]:
        emp_list.append(row)


#Dictionary
dict_keys = [emp[0] for emp in emp_list]
dict_values = [emp[1:] for emp in emp_list]

#Converting numbers data to integers
for dict in dict_values:
    dict[2] = int(dict[2])
    dict[5] = int(dict[5])
    dict[6] = int(dict[6])
emp_dict = {int(k):v for k,v in list(zip(dict_keys, dict_values))}

#Menu display prompts
update_prompt = '''
Update Employee Menu
1. Update Employee Data using ID
2. Update Employee Salary (per Department)
3. Back to Main Menu
'''

def print_header():
    print(f'| ID   | {'Name':<20} | {'Gender':<7} | {'Age':<4} | {'Job Title':<15} | {'Department':<15} | {'Salary':<8} | {'Exp':>4} |')
    print('------------------------------------------------------------------------------------------------------')  

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

            # departments = [[0, 'Finance'], [1, 'Marketing'], [2, 'IT'], [3, 'Production'], 
            #                [4, 'Sales'], [5, 'HR']]
            
            # for dept in departments:
            #     print(f'{dept[0]}. {dept[1]}')

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
        elif opt > 3 or opt == 0:
            print('Wrong value! Enter an option from the menu: ')

update_menu(emp_dict)