# -*- coding: utf-8 -*-
"""Lv1_완주하지 못한 선수.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RkWf4v5TTN0VqJIx9ptwjRBPn1DcHdl5
"""

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]

    return participant[-1]
            
'''
def solution(participant, completion):
    for i in completion :
        participant.remove(i)

    return participant[0]

'''

print(solution(participant,completion))