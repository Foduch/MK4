n = 3
first = [i+1 for i in range(n)]

last = [i for i in range(n, 0, -1)]

def NextP(x):
    n = len(x)-1
    if x != last:
        k = n -1  

    try:
        while x[k] > x[k+1]:
            k -= 1
    except IndexError:
        pass
    
    t = k + 1
    while (t < n) and (x[t+1] > x[k]):
        t += 1
    

    f = True
    for i in range(k+1, len(x)-1):
        if x[i]<x[i+1]:
            f = False
            break
    if f:
        x[k], x[t] = x[t], x[k]
        
    if f:
        for i in range(len(x)//2):
            x[k+1], x[len(x)-1-i] = x[len(x)-1-i], x[k+1]
	    
    return x

m = 1

print(first)
while (first != last): 
    print(NextP(first))
    m += 1
print(m)

    
    
