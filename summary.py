import csv

#Create dictionary from csv file
file = 'employees.csv'
header = []
emp_list = []

with open(file, 'r') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    header = data[0]
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

#Summary menu options prompt
summary_prompt = '''
Display Employee Summary
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

    def dollar(num):
        num = f"{num:,}"
        num = f'${num}'
        return num

    def average(col):
        return sum(col)//len(col) 
    
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

summary_menu(emp_dict)