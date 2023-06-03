import rent,returning

def welcome_message():
    '''This function called welcome_message displays welcome message to the user'''
    print("\n")
    print('''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                            Welcome to the marvalcostume rental Shop
                                    Hope you have a great time!
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
print("\n")    

    
def exit_message():
    ''' Thsi function display message after exiting the system helps user to exit the system'''
    print ("\n")
    print('''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        Thank You for using our system.Have a great day!
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
welcome_message()

def options():
    """ This function displays the options to the user"""
    print("\n")
    print("\n")
    print("Please select an option:")
    print("\n")
    print("(1) ** Press 1 to rent Costume. **")
    print("\n")
    print("(2) ** Press 2 to return Costume. **")
    print("\n")
    print("(3) ** Press 3 to exit from the system. **")
    print("\n")

    
while True:
    options()
    option=(input("Choose suitable option according to you: "))
    if option=="1":
        rent.Rent_costumes()
        
    elif option == "2":
        returning.Return_costumes()
    elif option =="3":
        exit_message()
        break
    else:
        print("\n\nInvalid input!!!!!\nPlease enter the value as per the provided options. Thank you!!.\n\n")
