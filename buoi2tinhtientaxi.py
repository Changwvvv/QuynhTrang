# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:46:15 2024

@author: Quynhtrang
"""
a = float(input("Số km taxi đi được:"))
if a==1:
    b=20
    print("tiền taxi là: ",b , "k")
elif a<=3:
    b=a*13
    print("tiền taxi là: ",b , "k")
elif a<=8:
    b=3*13+(a-3)*12
    print("tiền taxi là: ",b , "k")
elif a>8:
    b= 3*13 + 5*12 + (a-8)*10
    print("tiền taxi là: ",b , "k")
if b >100:
    b=b*0.92
    print("tiền taxi sau giảm là:", b)
     
     
     
    
    

