# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:30:51 2024

@author: Student
"""

GPA = float(input("Nhập điểm trung bình (GPA):"))
if GPA < 3.5:
    print("Học lực Kém")
if 3.5 <= GPA < 5.0:
    print("Học lực Yếu")
if 5.0 <= GPA < 7.0:
    print("Học lực Trung Bình")
if 7.0 <= GPA < 8.0:
    print("Học lực Khá")
if 8.0 <= GPA < 9.0:
    print("Học lực Giỏi")
if 9.0 <= GPA <= 10:
    print("Học lực Xuất sắc")