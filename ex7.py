# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:58:33 2024

@author: GF LAB
"""


gram = {
    "S":  ["S+S", "S*S",'S-S','(S)', "id"]
}
start = "S"
inp = "(id+id)$"
stack = "$"

print(f'{"Stack": <15}' + "|" + f'{"Input Buffer": <15}' + "|" + f'Parsing Action')
print(f'{"-":-<50}')

while True:
    flag = 1
    i = 0

    for i in range(len(gram[start])):
        if gram[start][i] in stack:
            stack = stack.replace(gram[start][i], start)
            print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + f'Reduce S->{gram[start][i]}')
            flag = 0

    if len(inp) > 1:
        stack += inp[0]
        inp = inp[1:]
        print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + f'Shift')
        flag = 0

    if inp == "$" and stack == ("$" + start):
        print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + f'Accepted')
        break

    if flag:
        print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + f'Rejected')
        break
