# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:52:15 2024

@author: Quynh Trang
"""

GPA = float(input("Nhập điểm trung bình (GPA):"))
if GPA < 3.5:
    print("Học lực Kém")
elif GPA >= 3.5 and GPA < 5.0:
    print("Học lực Yếu")
elif GPA >= 5.0 and GPA < 7.0:
    print("Học lực Trung Bình")
elif GPA >= 7 and GPA < 8:
    print("Học lực Khá")
elif GPA >= 8 and GPA < 9:
    print("Học lực Giỏi")
elif GPA >= 9 and GPA <= 10:
    print("Học lực Xuất sắc")
else:
    print("không xác định")