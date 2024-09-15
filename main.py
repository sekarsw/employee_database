employees = {}

def main_menu():
    while True:
        option = input('Enter the menu you want to choose: ')

        #Raise error if input is not an integer
        try:
            option = int(option)
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

            #Update Employee Menu
            elif option == 4:
                print('Update Employee Data')

            #Delete Employee Menu
            elif option == 5:
                print('Delete Employee Data')

            #End Program
            else:
                break  

        except:
            print('Wrong input! Please enter a number') 

       

main_menu()