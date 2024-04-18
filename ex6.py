# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:56:49 2024

@author: GF LAB
"""

print("Recursive Desent Parsing For following grammar\n")
print("E->TE'\nE'->+TE'/@\nT->FT'\nT'->*FT'/@\nF->(E)/i\n")
print("Enter the string want to be checked\n")
global s
s=list(input())
global i
i=0
def match(a):
    global s
    global i
    if(i>=len(s)):
        return False
    elif(s[i]==a):
        i+=1
        return True
    else:
        return False
def F():
    if(match("(")):
        if(E()):
            return match(")")
        else:
            return False
    else:
      return match("i")

def Tx():
    if(match("*")):
        if(F()):
            return Tx()
        else:
            return False
    else:
        return True
def T():
    if(F()):
        return Tx()
    else:
        return False
def Ex():
    if(match("+")):
        if(T()):
            return Ex()
        else:
            return False
    else:
        return True
def E():
    if(T()):
        return Ex()
    else:
        return False
if(E()):
    if(i==len(s)):
        print("String is accepted")
    else:
         print("String is not accepted")
else:
    print("string is not accepted")