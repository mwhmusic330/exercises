import time



def multiples(n):
    res = 0
    for i in range(1, n):
        if (i % 3 == 0 or i % 5 == 0):
            res+=i
    return res
print(time.perf_counter())

##### print(multiples(1000))
