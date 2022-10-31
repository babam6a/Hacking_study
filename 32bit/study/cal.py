import math
i=1

def calculate(a,b) : 
    print(type(a))
    i = 2228*(a/2228)*(b/2228)
    print(i)
    j = ((i-202)**2)/i
    print(j)

value = [(718,337),(718,285),(718,721),(718,885),(1510,337),(1510,285),(1510,721),(1510,885)]

for k in value : 
    p,q = k
    calculate(int(p),int(q))

