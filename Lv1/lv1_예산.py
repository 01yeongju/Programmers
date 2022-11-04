# -*- coding: utf-8 -*-
"""lv1_예산.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13gr_3qtlfeaUBb8QeniBB3_F1-IhMEfN
"""

def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    return len(d)

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))