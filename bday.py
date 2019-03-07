# bday.py
# Raunak Anand
# ECS 36A Winter 2019
# Simulation of Birthday Problem

# 24 people are the minimum number of people required to get a probaility of atleast 0.5
# 42 people are the minimum number of people required to get a probabilty of atleast 0.9

import random

def hasduplicates(l):  
    lst = set(l)  # set the list 
    for i in lst:  
        number = l.count(i) # to check if there are duplicates 
        if number > 1:  
            return True   
    return False

def onetest(count):
    bday = [] # random numbers which are the bday dates
    for i in range(count):
        day = random.randint(1, 365) # year has 365 days 
        bday.append(day) # random numbers added to the list bday
    duplications = hasduplicates(bday)
    return duplications
    
def probab(count, num):
    duplications = 0
    for i in range(num): # trials done 'num' number of times
        if onetest(count) == True:
            duplications = duplications + 1 # if duplicates exist add 1 
            
    value = duplications/num # probabilty 
    return value 

def main():
    probability = probab(2,5000)
    count = 2
    while probability <= 0.9: # program will run while probability is less than 0.9
        probability = probab(count,5000)
        count = count + 1
        print("For",count,"people, the probability of 2 birthdays is",probability)
        

main()
