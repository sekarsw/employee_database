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
add_prompt = '''
Add Employee Menu
1. Add Employee Using ID
2. Back to Main Menu
'''
def print_header():
    print(f'| ID   | {'Name':<20} | {'Gender':<7} | {'Age':<4} | {'Job Title':<15} | {'Department':<15} | {'Salary':<8} | {'Exp':>4} |')
    print('------------------------------------------------------------------------------------------------------')  


def add_menu(emp_dict):
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
  

        #########################################################
        #Go back to main menu
        elif opt == 2:
            break
        
        else:
            print('Wrong value! Enter an option from the menu: ')

add_menu(emp_dict)