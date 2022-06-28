#Happy Number by amqib

import math

def sumofdigit(number):
    total = 0
    rem = 0
    while number>0:
        rem = number%10
        total = total + (rem*rem)
        number = number//10
    return total

def happy(number):
    num = number
    while num!=1 and num!=4:
        num = sumofdigit(num)
    if num == 1:
        return True
    else :
        return False
        
n = int(input())
numb = []
for i in range(n):
    x = input()
    if happy(int(x)) == True:
        print("{} :)".format(x))
    else :
        print("{} :(".format(x))
