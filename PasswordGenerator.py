# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 21:03:36 2021

@author: 17pus
"""
import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['1','2','3','4','5','6','7','8','9','10']
symbols = ["!","$","%","@","#","*","&"]
print("welcome to the password generator")
a=int(input("how many letters do you want in your password\n"))
b=int(input("how many numbers do you want in your password\n"))
c=int(input("how many symbols do you want in your password\n"))


passwrd=[]
for char in range(1,a+1):
    passwrd+=(random.choice(letters))

for char in range(1,b+1):
    passwrd+=random.choice(numbers)

for char in range(1,c+1):
    passwrd+=random.choice(symbols)
random.shuffle(passwrd)


password=""
for char in passwrd:
    password+=char
    
print("you password is ",password)


#eg: CS@A34432%VZ10Q3
