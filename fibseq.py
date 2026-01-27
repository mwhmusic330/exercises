
a = 1
b = 2
fib_seq = [a,b]
evens = []

while (a + b) <= 4000000:
    next_term = a + b
    fib_seq.append(next_term)
    a = b
    b = next_term

for num in fib_seq:
    if num % 2 == 0:
        evens.append(num)
answer = sum(evens)
print(answer)
