######## Sum of squares - squre of sum, Project Euler.
######## Solve for first 100 natural numbers.
######## First created a function to find the sum of squares.
######## Using a for loop to square each number in range and add to list.
######## Tested that with (1,10).
######## Created a function to find the square of the sum.
######## Nesting the range function within the sum function.
######## Squaring on the return statement.
######## Tested with with (1,10).
######## Called both functions/assigned variables.
######## subtracted the two variables in a print statement.

def sumofsquares(start, end):
    total = 0
    for x in range(start,end +1):
        total += x**2
    return total

def squareofsum(start, end):
    total = sum(range(start, end+1))
    return total**2

def main():
    sumsq = sumofsquares(1,100)
    sqsum = squareofsum(1,100)
    print(sqsum - sumsq)

if __name__ == '__main__':
    main()
