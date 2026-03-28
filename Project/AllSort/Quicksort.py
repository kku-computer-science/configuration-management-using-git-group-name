from .SortInterface import SortFact
import numpy as np

class Quicksort(SortFact):
    def sort(self, data):
        firstindex = 0
        lastindex = len(data)-1
        self.recursive(data, firstindex, lastindex)
        return data
        
    def recursive(self,data,firstindex,lastindex):
        if firstindex < lastindex :
            
            oldpivot = self.partition(data,firstindex,lastindex)
        
            self.recursive(data, firstindex, oldpivot-1)
            self.recursive(data, oldpivot+1, lastindex)
            
    def partition(self,data,firstindex,lastindex):
        lowerindex = firstindex-1
        pivot = data[lastindex]
        for currentindex in range(firstindex, lastindex):
            if data[currentindex] < pivot:
                lowerindex += 1
                data[lowerindex], data[currentindex] = data[currentindex], data[lowerindex]
                
        data[lowerindex+1], data[lastindex] = data[lastindex], data[lowerindex+1]
        return lowerindex+1 
            


            