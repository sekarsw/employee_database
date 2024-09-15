employees = {}

def main_menu():
    while True:
        option = input('Enter the menu you want to choose: ')

        #Raise error if input is not an integer
        try:
            option = int(option)  
        except:
            print('Wrong input! Please enter a number') 

        #Print error message if option is out of range
        if option >= 7:
            print('Option out of range! Please enter a number from the menu: ')
            continue
        
        #Display Menu
        elif option == 1:
            print('Display')
        
        #Summary Menu
        elif option == 2:
            print('Summary')

        #Create New Employee Menu
        elif option == 3:
            print('Create New Employee')

        elif option == 4:
            print('Update Employee Data')

        elif option == 5:
            print('Delete Employee Data')

        else:
            break
        