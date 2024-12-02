from sorting import *
import random

n= int(input("How many numbers do you want to get?"))
numbers=[]
for i in range(n):
    numbers.append(random.randint(0,100))
print(numbers)
BubbleSort(numbers)
print("The list aftter sorted")
print(numbers)
