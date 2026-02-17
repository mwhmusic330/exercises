#### project Euler #10



def sieve(n):
    isprime = [True] * (n + 1)
    isprime[0] = isprime[1] = False

    p = 2
    while (p * p <= n):
        if (isprime[p] == True):
            for i in range(p* p, n + 1, p):
                isprime[i] = False
        p += 1

    primes = [p for p, is_p in enumerate(isprime) if is_p]
    return primes 



n = 2000000
sievlist =sum(sieve(n))
print(sievlist)
