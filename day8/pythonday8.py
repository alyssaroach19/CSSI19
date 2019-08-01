"""
def CountToN(num):

        num = abs(num)
        for i in range(1,num+1):
                print i


n = raw_input("Enter an integer:")
n = int(n)

CountToN(n)


def Factors(num):
        
        num = abs(num)
        l = []
        
        for i in range(1,num+1):
                
                if num % i == 0:
                        l.append(i)
        return l

d = raw_input("Enter an integer:")
d = int(d)


print Factors(d)
"""

def my_dict():

        w = raw_input("Enter a string:")
        
#empty dictionary 
        d = {}
        for i in w:
                if d.has_key(i):
                        d[i]+ 1
        else :
                d[i] = 1
        for x,y in d.items():
                print x, ":", y
