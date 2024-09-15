add_prompt = '''
Add Employee Menu
1. Add Employee
2. Back to Main Menu
'''

def add_menu(dict=None):
    while True:
        #print(add_prompt)
        opt = input('Enter an option: ')

        #Notification error if opt is a string
        try: 
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
        
        #Add employee menu
        if opt == 1:
            print('Add employee')

        
        #Go back to main menu
        elif opt == 2:
            break
        
        else:
            print('Wrong value! Enter an option from the menu: ')

add_menu()