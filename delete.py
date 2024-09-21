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

for dict in dict_values:
    dict[2] = int(dict[2])
    dict[5] = int(dict[5])
    dict[6] = int(dict[6])
emp_dict = {int(k):v for k,v in list(zip(dict_keys, dict_values))}

#Menu display prompts
del_prompt = '''
Delete Employee Menu
1. Delete Employee
2. Back to Main Menu
'''
def print_header():
    print(f'| ID   | {'Name':<20} | {'Gender':<7} | {'Age':<4} | {'Job Title':<15} | {'Department':<15} | {'Salary':<8} | {'Exp':>4} |')
    print('------------------------------------------------------------------------------------------------------')  


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

delete_menu()