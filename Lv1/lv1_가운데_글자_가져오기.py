# -*- coding: utf-8 -*-
"""lv1_가운데 글자 가져오기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LD6CsRRvz1Ezha82rqRQc639JBX32gDW
"""

def solution(s):
    if len(s) % 2 == 0 :
        return s[len(s)//2-1:len(s)//2+1]
    else :
        return s[len(s)//2]

print(solution("abcde"))
print(solution("qwer"))