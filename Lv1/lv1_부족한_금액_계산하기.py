# -*- coding: utf-8 -*-
"""lv1_부족한 금액 계산하기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hvaCjuo0SzqP0G32vQwnl0q9MUiaqUK1
"""

def solution(price, money, count):
    pay = 0
    for i in range(1,count+1) :
        pay += price * i

    if pay > money :
        return pay - money
    else :
        return 0

print(solution(3,20,4))