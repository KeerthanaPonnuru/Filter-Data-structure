import random
import math
from functools import reduce

class Set:

    def __init__(self, set_ele):
       
        self.id = 0
        self.x = str(bin(self.id))[2:] 
        self.generate_elements()

    def generate_elements(self):

        self.elements = random.sample(range(0, 10000000000000), set_ele)
        
        for i in range(len(self.elements)):
            if self.elements[i] not in self.elements:
                pass
            else:
                i -= 1
                continue

class Filter:

    def __init__(self, bit):

        self.filter_id = 0
        self.B = [0 for i in range(bit)]


class cbf:
   
    def __init__(self, set, set_ele,
                 filter, bit,
                 k):

        self.set = set 
        self.set_ele = set_ele  
        self.filter = filter  
        self.k = k  
        self.bit = bit

        self.c = self.set * self.set_ele  
        self.l = math.ceil(math.log2(self.set + 1))

        self.sets = [Set(self.set_ele) for i in range(self.set)]
        self.filters = [Filter(self.bit)for i in range(self.filter)]

        self.hash()

    def hash(self):
        self.s = random.sample(range(0, 10000000000000), self.k)
        

    def helper_sets(self):
        i=0
        while(i<self.set):
            self.sets[i].id = i + 1
            self.sets[i].x = str(bin(self.sets[i].id)[2:])
            while len(self.sets[i].x) < self.filter:
                self.sets[i].x = '0' + self.sets[i].x
            i=i+1

    def helper_filter(self):
        i=0
        while(i<self.filter):
            self.filters[i].filter_id = i + 1
            i=i+1

    def encode(self):
        i,j=0,0
        k,m=0,0
        while(i<self.set):
            while(j<self.l):
                if self.sets[i].x[j] != "1":
                    pass
                else:
                    while(k<self.set_ele):
                        while(m<len(self.s)):

                            l=[self.sets[i].elements[k],self.s[m]]
                            res = reduce(lambda x, y: x ^ y, l)
                            hash_index = res % self.bit
                            if self.filters[j].B[hash_index] == 1:
                                pass
                            else:
                                self.filters[j].B[hash_index] = 1
                            m=m+1
                        k=k+1
                        m=0

                j=j+1
                k=0
            i=i+1
            j=0
            

    def lookup(self, element, filter):
        i=0
        while(i<len(self.s)):
            l=[element,self.s[i]]
            res = reduce(lambda x, y: x ^ y, l)
            hash_index = res % self.bit
           
            if filter.B[hash_index] == 1:
                pass

            else:
                return False
            i=i+1
        return True


if __name__ == "__main__":

    set = int(input("no. of sets: "))
    set_ele = int(input("no. of elements per set: "))
    filter = int(input("no.of filters: "))
    bit = int(input("no. of bits: "))
    k = int(input("no. of hashes: "))

    cobf = cbf(set, set_ele,filter, bit, k)
    cobf.helper_sets()
    cobf.helper_filter()
    cobf.encode()

    doc = open('codedbloom.txt', 'w')
    i,j,k=0,0,0
    while(i<cobf.set):
        while(j<cobf.l):
            if cobf.sets[i].x[j] != "0":
                pass
            else:
                while(k<cobf.set_ele):
                    if not cobf.lookup(cobf.sets[i].elements[k], cobf.filters[j]):
                        pass
                    else:
                        cobf.c -= 1
                    k=k+1
            j=j+1
            k=0
        i=i+1
        j=0
    
    print(str(cobf.c), file=doc)



















