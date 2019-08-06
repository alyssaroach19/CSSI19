#How to define a function
def f(x):
    return 2 * x + 3

'''the above above function is named F. 
It takes one parameter which should be a number.
The function returns twice the parameter plus 3'''

'''Once a function is defined, you can use it by calling it. 
To call a function, you must use the function's name followed
by parentheses with the arguments of the function enclosed in them.
Arguments are literals, objects, expressions or return-value 
function calls that takes the place of the parameters in the function
definition. The arguments are associated with the parameter in the 
same position as them in. Hence, the first argument is associated
with the first parameter '''

#function call with a literal
print f(2) #returns 7

#function call with an expression
print f(3 + 4 * 6) # returns 57

#function call with a function call
print f(f(6)) #return 33

v = 89
#function call with a variable
print f(v) #return 181

'''Task 1: Define a function that takes
 two parameters. It returns the greater of the 
 two parameters. Assume that the parameters are numbers'''

def num (x,y):
    if x >= y:
        return x
    else:
        return y

x = float(raw_input("Enter a number:"))
y = float(raw_input("Enter a second number:"))
print num(x,y)

'''Task 
'''
def Echo():
    msg = raw_input("Enter a string:")
    return msg + msg

print Echo()

def Display3(x,y,z):
    v = x * y * z + 3
    print v
    
Display3(2,3,4)

'''What is a list'''
'''A list is an ordered collection of objects'''
'''You access the element of a list with an index which is
a an integer between -n to n-1 where n is the length of the list.
Negative indices access the list in reverse and non-negative 
indices access the list is order. For any non-negative index
 i, it's equivalent negative index is n - i where n is the length
 of the list.'''

 #creating a list
l = [] #[] are called subscript operators.
 #The above is an empty list

k = list() #another way of creating an empty list

j = [1,2,3,4,5,6,7,8,9,10] #a list content

 #list methods
print "l =", l
print "k =", k
print "j =", j

j.clear() #j is now an empty list

print "The lists after clear is called on j"
print "l =", l
print "k =", k
print "j =", j

l.append('a')
k.append('t') 
j.append('p')

#dictionary
'''What is a dictionary?'''
'''An unordered collection of key-value pairs'''
'''How to create a dictionary'''
d = {}
b = dict()
a = {1:2,2:1,3:3,4:5,5:4} #A DICTIOANRY OF PERMUTATED
c = {12:"John smith", 89:"Jane doe"}

print a[1] 