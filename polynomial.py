#!/anaconda/bin/python
class Polynomial(object):

    def __init__(self,coeffList):
        self.coeffs = coeffList
        self.order = len(coeffList)-1

    def __len__(self):
        return len(self.coeffs)

    def __neg__(self):
        return Polynomial(map(lambda x: -x,self.coeffs))
    
    def __add__(self,other):
        if len(self) < len(other):
             return Polynomial([self.coeffs[ii] + other.coeffs[ii] if ii <= self.order\
                    else other.coeffs[ii] for ii in range(other.order+1)])
        elif len(self) > len(other):
            return Polynomial([self.coeffs[ii] + other.coeffs[ii] if ii <= other.order\
                    else self.coeffs[ii] for ii in range(self.order+1)])
        else:
            return Polynomial(map(lambda x,y: x + y,self.coeffs,others.coeffs))

    def __sub__(self,other):
        p = -other
        return self + p
            
    def __mul__(self,other):
        prod = [0]*(len(self)+len(other))
        for ii,cc in enumerate(self.coeffs):
            for jj,qq in enumerate(other.coeffs):
                prod[ii+jj] += cc*qq
        return Polynomial(prod)

    def __str__(self):
        return '+'.join('%d*x^%d'%(c,ii) for (ii,c) in enumerate(self.coeffs) if c!= 0)


def main():
    p1 = Polynomial([0,1,2,1])
    p2 = Polynomial([0,1,3,1,5])
    p3 = p1 + p2
    print str(p1)
    print p3
    print p1*p2
    p = p1-p2
    print p

if __name__ == '__main__':
    main()
