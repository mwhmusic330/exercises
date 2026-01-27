import math






def findfactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) +1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)

    return factors
number = 600851475143
factorslist = findfactors(number)


print(max(factorslist))



