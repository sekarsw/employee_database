def summary_menu(dict=None):
    while True:
        #print(summary_prompt)
        opt = input('Enter an option: ')

        #Notification error if opt is a string
        try: 
            opt = int(opt)
        except:
            print('Wrong value! Input must be a number')
        
        #Employee summary menu
        if opt == 1:
            print('Employee summary')

        #Filter summary 
        elif opt == 2:
            print('Filter summary')

        #Go back to main menu
        elif opt == 3:
            break
        
        else:
            print('Wrong value! Enter an option from the menu: ')