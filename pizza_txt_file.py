# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 00:07:03 2023

@author: asus
"""


def menu_listeleme(line):
    
    print(line)
    



with open("Menu.txt","r",encoding= "utf-8") as file:
    
    for i in file:
        
        menu_listeleme(i)




