display_prompt = '''
Display Employee Data
1. Display All Employee Data
2. Filter Employee Data
3. Back to Main Menu
'''

def display_menu(dict=None):
    while True:
        print(display_prompt)
        #Input menu number
        opt = input('Please enter the menu of your choice: ')

        #Error notification if input is a string
        try:
            opt = int(opt)
        except:
            print('Wrong value! Please enter a number from the menu: ')
            continue

        #Display All Data Menu
        if opt == 1:
            print('Display All Data')
            continue

        #Display Filter Data Menu
        elif opt == 2:
            print('Filter Data')
            continue
        
        #Go back to Main Menu
        elif opt == 3:
            break
        
        #Notification for invalid integer value
        else:
            print('Wrong value! Please enter the correct number: ')
            continue

display_menu()


    