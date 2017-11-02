from time import time
m = 9
n = 6
x = [9 for i in range(n)]
#x[0] = 0

def incr(x, m):
    n = len(x)
    if x[-1] < m:
        x[-1] += 1
        return x
    else:
        k = n-2
        while (x[k] == m) and (k > 0):
            k -= 1
        if (k == 0) and (x[0] == m):
            for i in range(6):
                x[i] = 0
            return x
        else:
            for i in range(1, n-k):
                x[-i] = 0
            x[k] += 1
            return x

#for i in range(999999):        
    #print(incr(x, 9))            
            
def sb():
    st = time()
    res = 0
    x = [0 for i in range(6)]
    incr(x, 9)
    while sum(x) != 0:
        incr(x, 9)
        if (sum(x[0:3]) == sum(x[3:])):
            res += 1
            #print(x)
    print(time()-st)
    return res

