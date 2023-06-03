import datetime
import rent,bill
def Return_costumes(): #this function is used to return the constume which is ranted 
    rent.costume_table() #calling function "Costume_table" from the rent module.
    print("\n")
    print("\n")
    print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    Let's renturn the costume.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
    #creating the empty list to store data 
    List_of_returned_customes     = []
    Brand_of_returned_customes    = []
    Price_for_costume_returned    = []
    quantity_of_customes_returned = []
    Name_Customer = input("Please! Enter your name : ")
    Total_Rquantity = 0
    Total_Fine_for_renting =0
    Total_rented_days = 0
    
    Return_more = True
    while Return_more == True:
        rent.costume_table()
        while True:
            try:
                S_No = int(input("Please! Enter the ID of the costume you wanna return: "))
                break
            except:
                print("Please input the valid ID of the costumes!!!")
            
        while True:
            try:
                quantity = int(input("Please! Enter the quantity of the costume you wanna return: "))
                break
            except:
                print("Please enter valid quantity of the costumes!!! ")
            
        quantity_of_customes_returned.append(quantity)

        Costume = rent.costumeDictionary()
        stock_quantity = int(Costume[S_No][3])
            
        Costume[S_No][3] = str(stock_quantity + quantity)
        rent.update_file(Costume)
        Total_Rquantity += quantity

        List_of_returned_customes.append(Costume[S_No][0])
        Brand_of_returned_customes.append(Costume[S_No][1])
        return_other = input("Press y to return more ?")
        if return_other.lower() == "y":
            Return_more = True
        else:
            Return_more = False
            print("Thank you!! The costume has been returned successfully. Have a nice day.")
            while True:
                try:
                    ask_user_days_rented = int(input("Please! enter the no.of days you rented the costumes for: "))
                    break
                except:
                    print("Please enter the days in correctely!! " )
            
            if ask_user_days_rented > 5:
                Total_rented_days = ask_user_days_rented -5
            else:
                Total_Fine_for_renting = ("You dont have any fine.")
                print(Total_Fine_for_renting)
    bill.Bill_for_returning(Name_Customer, Total_Rquantity, Total_Fine_for_renting,Total_rented_days,List_of_returned_customes,Brand_of_returned_customes,Price_for_costume_returned,quantity_of_customes_returned)
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Now, The updated custome table is:")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    rent.costume_table()


