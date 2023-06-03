import datetime

def Bill_for_renting(Name_of_customer,Address_of_customer,Phone_number_of_Customer, Total_Price,Total_Quantity, List_of_rented_customes,Brand_of_rented_costumes,Price_for_rented_costumes,Quantity_of_rented_customes):
    """displays the BillForRenting"""
    print("==========================================================================================")
    print("                              BILL DETAILS --- OF RENTING A COSTUME "  )
    print("==========================================================================================")
    print("Enter your name: ", Name_of_customer)
    print("Enter your address : ", Address_of_customer)
    print("Enter your phone number: ",Phone_number_of_Customer)
    print("\t\t\t\t\t\t\tDate:",str(datetime.datetime.now()))
    print("------------------------------------------------------------------------------------------")
    print("S.No\tCostume Name\t\tBrand\t\t\tUnit Price\tQuantity")
    print("------------------------------------------------------------------------------------------")
    for i in range(len(List_of_rented_customes)):
        print(str(i+1)+"\t"+List_of_rented_customes[i]+"\t\t"+Brand_of_rented_costumes[i]+"\t\t"+Price_for_rented_costumes[i]+"\t\t"+str(Quantity_of_rented_customes[i]))
    
    print("------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tTotal quantity: "+ str(Total_Quantity))
    print("\t\t\t\t\t\t\tTotal Price   : "+"$"+ str(Total_Price))
    print("------------------------------------------------------------------------------------------")
    print("==========================================================================================\n")
    print("                                   CONTACT US AT\n")
    print("                              facebook.com/marvalcostume\n")
    print("                              instagram.com/marvalcostume\n")
                                                
    print("==========================================================================================\n")
    print("                       Thank you for renting the costume.                      ")
    
    print("\n\n")
    Txt_for_rent_bill(Name_of_customer,Address_of_customer,Phone_number_of_Customer, Total_Price, Total_Quantity, List_of_rented_customes,Brand_of_rented_costumes,Price_for_rented_costumes,Quantity_of_rented_customes)
    
    

def Txt_for_rent_bill(Name_of_customer,Address_of_customer, Phone_number_of_Customer,Total_Price, Total_Quantity, List_of_rented_customes,Brand_of_rented_costumes,Price_for_rented_costumes,Quantity_of_rented_customes):
    ''' stores bill in .txt file'''
    Rent_bill = open((str(Name_of_customer)+(str(datetime.datetime.now().microsecond)) )+".txt","w")
    
    Rent_bill.write("==========================================================================================\n")
    Rent_bill.write("                               marvalcostume Rental Ltd. \n ")
    Rent_bill.write("                                  puranoAirport,Dhangadhi\n")                                          
    Rent_bill.write("==========================================================================================\n")
    Rent_bill.write("Enter your name:  "+ Name_of_customer+"\n")
    Rent_bill.write("Enter your address: "+ Address_of_customer+"\n")
    Rent_bill.write("Enter your phone number : "+ Phone_number_of_Customer+"\n")
    Rent_bill.write("\t\t\t\t\t\t\tDate: "+ str(datetime.datetime.now()) +"\n")
    Rent_bill.write("------------------------------------------------------------------------------------------\n")
    Rent_bill.write("S.No\tCostume Name\t\tBrand\t\t\tUnit Price\tQuantity\n")
    Rent_bill.write("------------------------------------------------------------------------------------------\n")
    for i in range(len(List_of_rented_customes)):
        Rent_bill.write(str(i+1)+"\t"+List_of_rented_customes[i]+"\t\t"+Brand_of_rented_costumes[i]+"\t\t"+Price_for_rented_costumes[i]+"\t\t"+str(Quantity_of_rented_customes[i])+"\n")
    
    Rent_bill.write("------------------------------------------------------------------------------------------\n")
    Rent_bill.write("\t\t\t\t\t\t\tTotal quantity: "+ str(Total_Quantity)+("\n"))
    Rent_bill.write("\t\t\t\t\t\t\tTotal Price   : "+"$"+ str(Total_Price)+("\n"))
    Rent_bill.write("------------------------------------------------------------------------------------------\n")
    Rent_bill.write("==========================================================================================\n")
    Rent_bill.write("                               CONTACT US AT\n")
    Rent_bill.write("                          facebook.com/marvalcostume\n")
    Rent_bill.write("                          instagram.com/marvalcostume\n")
    
    Rent_bill.write("==========================================================================================\n")
    Rent_bill.write("                      THANKS FOR RENTING!!VISIT US AGAIN.\n")                                        
    Rent_bill.close()
    
def Txt_for_return_bill(Name_Customer,Total_Rquantity,Total_Fine_for_renting,Total_rented_days, List_of_returned_customes,Brand_of_returned_customes,Price_for_costume_returned,quantity_of_customes_returned):
    ''' stores bill in .txt file'''
    Return_Bill = open((str(Name_Customer)+(str(datetime.datetime.now().microsecond)) )+".txt","w")
    Return_Bill.write("==========================================================================================\n")
    Return_Bill.write("                                marvalcostume Rental Ltd. \n ")
    Return_Bill.write("                                     PuranoAirport,Dhangadhi\n")                                           
    Return_Bill.write("==========================================================================================\n")
    Return_Bill.write("Enter your name: "+ Name_Customer+"\n")
    Return_Bill.write("\t\t\t\t\t\t Date: "+ str(datetime.datetime.now()) +"\n")
    Return_Bill.write("------------------------------------------------------------------------------------------\n")
    Return_Bill.write("S.No\tCostume Name\t\tBrand\t\t\tQuantity\n")
    Return_Bill.write("------------------------------------------------------------------------------------------\n")
    for i in range(len(List_of_returned_customes)):
        Return_Bill.write(str(i+1)+"\t"+List_of_returned_customes[i]+"\t\t"+Brand_of_returned_customes[i]+"\t\t"+str(quantity_of_customes_returned[i])+"\n")
    
    Return_Bill.write("------------------------------------------------------------------------------------------\n")
    Return_Bill.write("\t\t\t\t\t\t\tTotal quantity: "+ str(Total_Rquantity)+("\n"))
    Return_Bill.write("\t\t\t\t\t\t\tTotal Price   : "+"$"+ str(Total_rented_days*Total_Rquantity*20)+("\n"))
    Return_Bill.write("------------------------------------------------------------------------------------------\n")
    Return_Bill.write("==========================================================================================\n")
    Return_Bill.write("                              CONTACT US AT\n")
    Return_Bill.write("                         facebook.com/marvalcostume\n")
    Return_Bill.write("                         instagram.com/marvalcostume\n")
                                                
    Return_Bill.write("==========================================================================================\n")
    Return_Bill.write("                      THANKS FOR RETURNING!!VISIT US AGAIN.\n")  

    

    
def Bill_for_returning(Name_Customer,Total_Rquantity,Total_Fine_for_renting,Total_rented_days, List_of_returned_customes,Brand_of_returned_customes,Price_for_costume_returned,quantity_of_customes_returned):
    """displays the Bill_for_renting"""

    
    print("==================================================================================================")
    print("                          BILL Details --- FOR RETURN " )
    print("==================================================================================================")
    print("Enter your name: ", Name_Customer)
    print("\t\t\t\t\t\t\tDate: ", str(datetime.datetime.now()))
    print("-------------------------------------------------------------------------")
    print("S.No\tCostume Name\t\tBrand\t\t\tQuantity")
    print("-------------------------------------------------------------------------")
    for i in range(len(List_of_returned_customes)):
        print(str(i+1)+"\t"+List_of_returned_customes[i]+"\t\t"+Brand_of_returned_customes[i]+"\t\t"+str(quantity_of_customes_returned[i]))
    
    print("-------------------------------------------------------------------------")
    print("\t\t\t\tTotal returned quantity: "+ str(Total_Rquantity))
    print("\t\t\t\tTotal Fine   : "+"$"+ str(Total_rented_days*Total_Rquantity*20))
    print("-------------------------------------------------------------------------")
    print("==========================================================================================\n")
    print("                              CONTACT US AT\n")
    print("                           facebook.com/marvalcostume\n")
    print("                           instagram.com/marvalcostume\n")
    print("==========================================================================================\n")
    print("                  Thank you! for returning the costume. See ya soon          ")
    
    print("\n\n")
    Txt_for_return_bill(Name_Customer,Total_Rquantity,Total_Fine_for_renting,Total_rented_days, List_of_returned_customes,Brand_of_returned_customes,Price_for_costume_returned,quantity_of_customes_returned)


