import random
from functools import reduce
class bloom:
   
    def __init__(self, e, bits, k):
       
        self.e = bits
        self.bits = bits
        self.k = k

        self.c = 0
        self.B = [0 for i in range(self.bits)]
        
        self.gen()

    def gen(self):
        self.elements=random.sample(range(0,1000000000),e)

    def hash(self):
        self.s = random.sample(range(0, 1000000000), self.k)

    def encode(self):
        i,j=0,0
        while(i<len(self.elements)):
            while(j<len(self.s)):
                l=[self.elements[i],self.s[j]]
                res = reduce(lambda x, y: x ^ y, l)
                ind = res % len(self.B)
                if self.B[ind] ==1:
                    pass
                else:
                    self.B[ind] = 1
                j=j+1
            i=i+1
            j=0


    def lookup(self, element):
        i=0
        while(i<len(self.s)):

            l=[element,self.s[i]]
            res = reduce(lambda x, y: x ^ y, l)
            ind = res % len(self.B)
            if self.B[ind] ==1:
                pass
            elif self.B[ind]!=1:
                return False
            i=i+1
        self.c += 1
        return True


if __name__ == "__main__":

    e = int(input("no. of elements: "))
    bits = int(input("no. of bits: "))
    k = int(input("no.of hashes: "))
    bf = bloom(e, bits, k)
    bf.hash()
    bf.encode()
    
    i,j=0,0
    file = open('bloom.txt', 'w')
    print()
    
    result_a = []
    while(i<len(bf.elements)):
        result_a.append(bf.lookup(bf.elements[i]))
        i=i+1
    
    print(str(bf.c))
    print(str(bf.c), file=file)

    bf.c = 0
    bf.gen()
    
    result_b = []
    while(j<len(bf.elements)):
        result_b.append(bf.lookup(bf.elements[j]))
        j=j+1

    print(str(bf.c), file=file)
















