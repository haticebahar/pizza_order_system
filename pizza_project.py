#Import csv and datetime libraries
import csv
import datetime
import time
import pandas as pd

#Define the get_description() and get_cost() methods for encapsulation that creates the pizza class and inside this class.
class Pizza:
    def get_description(self): 
        return self.__class__.__name__

    def get_cost(self): 
        return self.__class__.cost
    
    def menu_listeleme(line):
            
         print(line)

        
#Classic, Margherita, Turk Pizza, Dominos Pizza. Create pizza classes. Since each of these pizza types is a type of pizza, these classes will be defined as subclasses        
class Classic(Pizza):
    cost = 70.0

    def __init__(self):
        
        self.description = "Klasik Pizza Malzemeler: Kaşar,Sucuk,Sosis,Domates,Salam"
        print(self.description +"\n")

class Margaritha(Pizza):
    cost = 50.0

    def __init__(self):
        self.description = "Margarita Pizza Malzemeler: Mozarella,Fesleğen"
        print(self.description +"\n")

class TurkishPizza(Pizza):
    cost = 100.0

    def __init__(self):
        self.description = "Turkish Pizza Malzemeler: Soğan,Kavurma,Biber,Sarımsak,Kaşar"
        print(self.description +"\n")
        
class PlainPizza(Pizza):
    cost = 80.0


    def __init__(self):
        self.description = "Sade Pizza Malzemeler: Sucuk, Kaşar,Zeytin,Mısır"
        print(self.description +"\n")

#Create a decorator class. Decorator is called super class of all sauce classes here. 
#The decorator class will use the get_description() and get_cost() methods using the properties of the pizza class. 
#Complete the decorator class using the following methods.

class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
          Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
          ' ;' + Pizza.get_description(self)
 
#Determine Olives, Mushrooms, Goat Cheese, Meat, Onions, and Corn as sauces, and define each of the sauces you have determined as a class.
class Olive(Decorator):
    cost = 2.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mushroom(Decorator):
    cost = 3.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Cheese(Decorator):
    cost = 4.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Meat(Decorator):
    cost = 10.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Onion(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Corn(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)     
    
  
#Create a main function. This function will print the menu on the screen first. Then let the user choose a pizza and sauce from the menu. 
#After calculating the total price of the selected products, it should ask the user for a name, ID number, credit card number and credit card password. 
#with all required information

def main():
    with open("Menu.txt","r",encoding= "utf-8") as file:
    
        for i in file:
        
            Pizza.menu_listeleme(i)
    
    menu_dict = {1: Classic,2: Margaritha,3: TurkishPizza,4: PlainPizza,5: Olive, 
                  6: Mushroom,7: Cheese,8: Meat,9: Onion,10: Corn}
    
    choice = input("Lütfen menüden isteğiniz pizzayı seçiniz:")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Hatalı seçim yaptınız....")
        time.sleep(3)

    order = menu_dict[int(choice)]()

    while choice != "y":
        choice = input("Siparişi onaylamak için 'y' tuşuna basınız.Ek malzeme için seçim yapınız:")
        if choice in ["5","6","7","8","9","10"]:
            order = menu_dict[int(choice)](order)
    
    
#Calculate the payments of the people who choose their pizza and keep the user's name, user id, credit card information, description of order, 
#time order and credit card password in the "Orders_Database.csv" file, which we call the database.            

    print("\n" + order.get_description().strip() + " " + str(order.get_cost()) + " TL")
    
    print("\n")
  
    
    print("-------------Sipraiş Özeti---------------\n")
    name = input("İsminiz: ")
    tc_no = input ("TC Kimlik numaranız: ")
    kk_no = input ("Kredi Kartı Numaranızı giriniz: ")
    kk_password = input ("Kredi KArtı Şifrenizi giriniz: ")
    order_time = datetime.datetime.now()
    
    with open('Oreder_Database.csv','a') as orders:
        
        orders = csv.writer(orders, delimiter = ',')
        orders.writerow([name,tc_no,kk_no,kk_password,order.get_description(),order_time])
        
    print("Siparişiniz Onaylandı.")
    
    
main()    
    
