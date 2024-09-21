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
summary_prompt = '''
Display Employee Summary
1. Display Overall Summary
2. Display Summary by Department
3. Back to Main Menu
'''


def summary_menu(emp_dict=None):
    employees = emp_dict 
    id = [k for k in employees.keys()]
    gender = [val[1] for val in employees.values()] 
    age = [val[2] for val in employees.values()]
    title = [val[3] for val in employees.values()]
    dept = [val[4] for val in employees.values()]
    salary = [val[5] for val in employees.values()]
    exp = [val[6] for val in employees.values()]

    def average(col):
        return (sum(col)//len(col))

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
            print('\n====================================')
            print(f'{'Employee Summary':^30}')
            print('====================================')
            print(f'Total Departments: {len(set(dept))}')
            print(f'{', '.join(set(dept))}')
            print()
            print(f'Total Employees: {len(id):>10}')
            print(f'Male Employees: {gender.count('M'):>11}')
            print(f'Female Employees: {gender.count('F'):>10}')
            print()
            print(f'Average Age: {average(age)}')
            print(f'Oldest Employee Age: {max(age)}')
            print(f'Youngest Employee Age: {min(age)}')
            print()
            print(f'Average Annual Salary: ${average(salary):,}')
            print(f'Highest Salary: ${max(salary):,}')
            print(f'Lowest Salary: ${min(salary):,}')
            print()
            print(f'Average Years of Experience: {average(exp)}')

        #--------------------------------------------------------------------------------------------------------
        #Display Summary by Department Menu
        elif opt == 2:
            #Define department names
            columns = ['Finance', 'Marketing', 'IT', 'Production', 'Sales', 'HR', 'Back to display menu']

            #Display menu to input filter category
            print('Filter Employee Data by ')
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
            if opt > 7 or opt == 7:
                print('Choose the number from the menu!')
                continue

            #Go back to main display menu
            if opt == 7:
                break

            # emp_gender = []
            # emp_age = []
            # emp_salary = []
            # emp_exp = []

            #Summary of Finance Department 
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
                print('==== ============================')
                print('Summary of HR Department')
                print('================================')

                emp_gender, emp_age, emp_salary, emp_exp = filter_dept('HR')


            print(f'Total Employees: {len(emp_gender)}')
            print(f'Male Employees: {emp_gender.count('M'):>11}')
            print(f'Female Employees: {emp_gender.count('F'):>10}')
            print()
            print(f'Average Age: {average(emp_age)}')
            print(f'Oldest Employee Age: {max(emp_age)}')
            print(f'Youngest Employee Age: {min(emp_age)}')
            print()
            print(f'Average Annual Salary: ${average(emp_salary):,}')
            print(f'Highest Salary: ${max(emp_salary):,}')
            print(f'Lowest Salary: ${min(emp_salary):,}')
            print()
            print(f'Average Years of Experience: {average(emp_exp)}')

        #Go back to main menu
        elif opt == 3:
            break
        

        else:
            print('Wrong value! Enter an option from the menu: ')
            continue

summary_menu(emp_dict)