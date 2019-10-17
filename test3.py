import numpy as np 
import os
import random
path = os.getcwd()+"\\train\\"
items = np.arange(1,11)
random.shuffle(items)
items2 = items
print("***")
print(np.partition(items2,4))
print("***")
print(items)
def distance(a = 0 , b = 0):
    #a1 = np.load(path+str(a)+".npy") # path
    #a2 = np.load(path+str(b)+".npy")
    return a-b#np.linalg.norm(a1-a2)
def _partition(first,middle,last,key):
    (items[middle] , items[last]) = (items[last],items[middle])
    pivot = items[last]
    R = distance(pivot,key)
    i = first - 1 
    for j in range(first,last):
        if distance(items[j],key) < R:
            i= i+1
            (items[i],items[j])= (items[j],items[i])
    (items[i+1],items[last]) = (items[last], items[i+1])
    print(pivot)
    
    return 
_partition(1,3,9,items[0])
print(items)
