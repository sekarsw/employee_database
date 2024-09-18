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
del_prompt = '''
Delete Employee Menu
1. Delete Employee
2. Back to Main Menu
'''


def delete_menu(emp_dict):
    employees = emp_dict

    while True:
        print(del_prompt)
        opt = input('Enter an option: ')

        #Notification error if opt is a string
        try: 
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
        
        #Delete employee menu
        if opt == 1:
            print('Delete Employee\n')
            try:
                id = int(input('Input Employee ID: '))
            except:
                print('ID needs to be a number')

            if id in employees.keys():
                #Display data
                '''Need string formatting'''
                print(str(id), ' '.join(list(str(emp) for emp in employees[id])))

                #Confirm deletion
                resp = input('Confirm to delete the employee data (y/n): ')
                if resp == 'y':
                    employees.pop(id)
                    print('Employee data succesfully deleted.')
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

delete_menu(emp_dict)