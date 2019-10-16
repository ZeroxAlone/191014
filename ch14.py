# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:17:25 2019

@author: lisa_
"""

#1
def outputTimesTable(n):
    for i in range(1,11):
        if len(str(i)) >= 2:
            print(str(i) + " x " + str(n) + " = " + str(i*n))
        else:
            print(" " + str(i) + " x " + str(n) + " = " + str(i*n))
    print("\n")

outputTimesTable(5)

#2
def isDivisible(x, y):
    if x % y == 0:
        print("True")
    else:
        print("False")
    print("\n")

isDivisible(9, 3)

#3
def EggsintoBoxes(NumberOfEggs):
    NumberOfBoxes = NumberOfEggs // 6
    EggsLeftOver = NumberOfEggs % 6
    print("The number of boxes is: ", NumberOfBoxes)
    print("The number of eggs left over is: ", EggsLeftOver)

EggsintoBoxes(9)