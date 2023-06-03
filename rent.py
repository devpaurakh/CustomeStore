import datetime
import bill 
def costume_table():
    #This displays all the available customes with the details
    print("---------------------------------------------------------------------------------------------------")
    print("S_No","\t","Costume Name","\t\t","Company","\t\t","Price","\t\t","Quantity" )
    print("---------------------------------------------------------------------------------------------------")  
    text_file = open("Costume_for_rent.txt","r")
    S_No = 1
    for line in text_file:        
        print(S_No,"\t"+line.replace(",","\t\t"))
        S_No = S_No + 1
        print("---------------------------------------------------------------------------------------------------")

        
    print("\n")
    text_file.close()

def costumeDictionary():
    ''' This functions stores the data of text file in dictionary in key value pair'''
    text_file = open("Costume_for_rent.txt","r")
    Costumes = {}
    costume_S_No = 1
    for line in text_file:
        line = line.replace("\n","")
        Costumes.update({costume_S_No:(line.split(","))})
        costume_S_No += 1
    text_file.close()
    return Costumes

def update_dictionary(user_input_SNo,user_input_Quantity):
    '''This function updates the dictionary after renting the costumes'''
    Costume = costumeDictionary()
    Total_Quantity = int(Costume[user_input_SNo][3])
    while user_input_Quantity<=0 or user_input_Quantity>Total_Quantity:
        if user_input_Quantity>Total_Quantity:
            print("Quantity exceeded !!! Please enter the value within the availability range.")
        else:
            print("Invalid !!! Please enter valid quantity.")
        print("\n")
        user_input_Quantity = int(input("Enter the quantity of costume you want to rent: "))
        print("\n")
    print(Costume)


def validation_of_SNo():
    ''' validates the id of the costume '''
    valid_SNo = False
    while valid_SNo == False:
        try:            
            user_input_SNo = int(input("Please enter the ID of the costume you want to rent: "))
            valid_SNo = True
        except:
            print("\n")
            print("Invalid input!!! Please enter the ID in correctly.")
            print("\n")
    while user_input_SNo <= 0 or user_input_SNo > len(costumeDictionary()):
        print("\n The input Costume ID in invalid! Please enter it correctly. \n")
        user_input_SNo = int(input("Enter the ID of the costume you want to rent: "))
    print("\n")
    print("You are in luck! The costume is in stock.")
    print("\n")
    return user_input_SNo
    


def Rent_costumes():
    '''rents the costume and also supports multiple rent '''
    print("\n")
    print("\n")
    print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                            Let's rent the costume.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
    print("\n")
    costume_table()
    print("\n")
    Rent_more = True
    List_of_rented_customes=[]
    Brand_of_rented_costumes=[]
    Price_for_rented_costumes=[]
    Quantity_of_rented_customes =[]
    Total_Price = 0
    Total_Quantity = 0
    while Rent_more:
        user_input_SNo = validation_of_SNo()
        valaid_quantity = False
        while valaid_quantity == False:
            try:
                
                user_input_Quantity = int(input("Enter the quantity of costume you want to rent: "))
                Quantity_of_rented_customes.append(user_input_Quantity)
                valaid_quantity =True
                print("\n")
            except:
                print("Please enter the valid quantity!!!")

        Costume = validation_of_quantity(user_input_SNo,user_input_Quantity)
        update_file(Costume)

        Total_Quantity += user_input_Quantity
        Price_of_unit_quantity = float((Costume[user_input_SNo][2]).replace("$",""))
        Total_Price += Price_of_unit_quantity*user_input_Quantity
        
        print("\n")
        List_of_rented_customes.append(Costume[user_input_SNo][0])
        Brand_of_rented_costumes.append(Costume[user_input_SNo][1])
        Price_for_rented_costumes.append(Costume[user_input_SNo][2])
        
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Do you want to rent more?")
        print("If yes press 'Y' else press any other key")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\n")

        ask_user_for_more = input("Do you want to rent more? : ")
        print("\n")
        if ask_user_for_more.lower() == "y":
            costume_table()
            print("\n")
        else:
            Rent_more = False
            Name_of_customer = input("Please enter your name: ")
            Address_of_customer = input("Please enter your address: ")
            Phone_number_of_Customer = input("Please enter your phone number: ")

        print("the total quantity is: " ,Total_Quantity)   
    bill.Bill_for_renting(Name_of_customer,Address_of_customer,Phone_number_of_Customer,Total_Price,Total_Quantity,List_of_rented_customes,Brand_of_rented_costumes,Price_for_rented_costumes,Quantity_of_rented_customes)
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("The updated custome table is:")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            
    costume_table()

def update_file(Costume):
    '''updates text file '''
    text_file = open("Costume_for_rent.txt","w")
    for key,value in Costume.items():
        text_file.write(str(value[0]) +","+ str(value[1]) +","+ str(value[2]) +","+ str(value[3]))        
        text_file.write("\n")
    text_file.close()    

def validation_of_quantity(user_input_SNo,user_input_Quantity):
    '''validates the quantity for costume '''
    Costume = costumeDictionary()
    Total_Quantity = int(Costume[user_input_SNo][3])
    while user_input_Quantity<=0 or user_input_Quantity>Total_Quantity:
        if user_input_Quantity>Total_Quantity:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Please enter the quantity within the stock range.")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(" Please enter valid quantity.")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n")
        user_input_Quantity = int(input("Enter the quantity of costume you want for rent: "))
        print("\n")
    Costume[user_input_SNo][3] = str(Total_Quantity - user_input_Quantity)
    return Costume
