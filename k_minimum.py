#!/usr/bin/python
import heapq
import random
import time

def createArray():
    array = list(range( 20 ))
    random.shuffle( array )
    return array

def heapSearch( bigArray, k ):
    heap = []
    for item in bigArray:
        if len(heap) < k or item > heap[0]:
            if len(heap) == k: heapq.heappop( heap )
            heapq.heappush( heap, item )
    return heap

start = time.time()
bigArray = createArray()
print(bigArray)
start = time.time()
print (heapSearch( bigArray, 2 ))    

print ("Heap search took %g s" % (time.time() - start))