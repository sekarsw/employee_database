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

#Display menu options prompt
display_prompt = '''
Display Employee Data
1. Display All Employee Data
2. Find Employee by ID
3. Filter Employee Data
4. Back to Main Menu
'''

def print_header():
    print(f'| ID   | {'Name':<20} | {'Gender':<7} | {'Age':<4} | {'Job Title':<15} | {'Department':<15} | {'Salary':<8} | {'Exp':>4} |')
    print('------------------------------------------------------------------------------------------------------')  


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
            columns = ['Gender', 'Age', 'Job Title', 'Department', 'Salary', 'Experience', 'Back to display menu']

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

display_menu()


    