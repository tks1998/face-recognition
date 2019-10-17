import os
import numpy as np
import heapq 

class Node:
    def __init__(self):
        self.index = -1 
        self.threshold = 0.0
        self.left = None
        self.right = None

class vptree:
    def __init__(self,maximum):
        self.items = np.arange(1,maximum)
        self._tau = 10000000.00
        self.heap = heapq.heapify([])
        self.path = os.getcwd()+"\\train"
    def distance(self,a,b):
        a1 = np.load(self.path+str(a)) # path
        a2 = np.load(self.path+str(b)) 
        return np.linalg.norm(a1-a2)
        
    def _distance(self,a,b):
        a1 = np.load(self.path+str(a)) # path
        return np.linalg.norm(a1-b)
    def _partition(self,first,last,key):
        while first!=last:
            return 
        return 
    def build(self,lower,upper):
        if lower == upper:
            return None
        node = Node()
        node.index = lower 
        if upper-lower > 1:
            print(1)
            middle = (lower+upper)/2
            sub_arr = self.items[lower+1:upper+1]
            np.partition(sub_arr,sub_arr[middle])
            
            node.threshold = self.distance(sub_arr[lower],sub_arr[middle])

            node.index = lower
            node.left = self.build(self,lower,middle)
            node.right = self.build(self,middle+1,upper)
        return node 

    def search(self, node = None , target = [] , k = 0 ):
        if node == None:
            return 
        
        dist = self.distance(node.index,target)

        if dist < self._tau:
            if len(self.heap) == k:
                heapq.heappop(self.heap)
            heapq.heappush(self.heap,(dist,node.index))
            if len(self.heap) == k:
                _tau = heap[0][0]  # get distance
        if node.left == None and node.right == None:
            return
        if dist<node.threshold:
            if dist-_tau<=node.threshold:
                self.search(node.left,target,k)
            if dist+_tau>=node.threshold:
                self.search(node.right,target,k)
        else:
            if dist+_tau>=node.threshold:
                self.search(node.right,target,k)
            if dist-_tau<=node.threshold:
                self.search(node.left,target,k)



