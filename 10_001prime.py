#### Project Euler #7
#### Find the 10,001st prime number.
#### Add 1 to limit for accuracy.
#### Create a set to dump not prime numbers.
#### Create a list of prime numbers starting with 2.
#### Implement sieve of Eratosthenes.
#### Call function with upper limit that seemed safe.
#### Index list for 10000th entry in print statement.
#### 10001st prime.



def primes_upto(limit):
    limitN = limit+1
    notprime = set()
    primes = [2]
    for i in range(3, limitN, 2):
        if i in notprime:
            continue
        for j in range(i*3, limitN, i*2):
            notprime.add(j)
        primes.append(i)
    return primes

def main():
    list = primes_upto(1000000)
    print(list[10000])

if __name__  == '__main__':
    main()
