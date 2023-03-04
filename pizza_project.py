# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:58:00 2023

@author: asus
"""

import csv
import datetime
import time
import pandas as pd


class Pizza:
    def get_description(self): 
        return self.__class__.__name__

    def get_cost(self): 
        return self.__class__.cost
    
    def menu_listeleme(line):
            
         print(line)

class Klasik(Pizza):
    cost = 70.0

    def __init__(self):
        
        self.description = "Klasik Pizza Malzemeler: Kaşar,Sucuk,Sosis,Domates,Salam"
        print(self.description +"\n")

class Margarita(Pizza):
    cost = 50.0

    def __init__(self):
        self.description = "Margarita Pizza Malzemeler: Mozarella,Fesleğen"
        print(self.description +"\n")

class TurkPizza(Pizza):
    cost = 100.0

    def __init__(self):
        self.description = "Turkish Pizza Malzemeler: Soğan,Kavurma,Biber,Sarımsak,Kaşar"
        print(self.description +"\n")
        
class SadePizza(Pizza):
    cost = 80.0


    def __init__(self):
        self.description = "Sade Pizza Malzemeler: Sucuk, Kaşar,Zeytin,Mısır"
        print(self.description +"\n")
  
class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
          Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
          ' ;' + Pizza.get_description(self)
          
class Zeytin(Decorator):
    cost = 2.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mantar(Decorator):
    cost = 3.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Peynir(Decorator):
    cost = 4.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Et(Decorator):
    cost = 10.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Sogan(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Misir(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)     
    
    
def main():
    with open("Menu.txt","r",encoding= "utf-8") as file:
    
        for i in file:
        
            Pizza.menu_listeleme(i)
    
    menu_dict = {1: Klasik,2: Margarita,3: TurkPizza,4: SadePizza,5: Zeytin, 
                  6: Mantar,7: Peynir,8: Et,9: Sogan,10: Misir}
    
    choice = input("Lütfen menüden isteğiniz pizzayı seçiniz:")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Hatalı seçim yaptınız....")
        time.sleep(3)

    order = menu_dict[int(choice)]()

    while choice != "y":
        choice = input("Siparişi onaylamak için 'y' tuşuna basınız.Ek malzeme için seçim yapınız:")
        if choice in ["5","6","7","8","9","10"]:
            order = menu_dict[int(choice)](order)
    
    
            
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
    