#### Project Euler Problem #5
#### cut down list, 20 includes (2,4,5), etc.
divisorlist = [11,13,14,16,17,18,19,20]

def check_divisor(step):
    num = step
    while True:
        if all(num % n == 0 for n in divisorlist):
            return num
        num += step


if __name__ == '__main__':
    ans = check_divisor(20)
    print(ans)
