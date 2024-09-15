def delete_menu(dict=None):
    while True:
        #print(delete_prompt)
        opt = input('Enter an option: ')

        #Notification error if opt is a string
        try: 
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
        
        #Update employee menu
        if opt == 1:
            print('Delete employee')

        
        #Go back to main menu
        elif opt == 2:
            break
        
        else:
            print('Wrong value! Enter an option from the menu: ')