######## Sum of squares - squre of sum, Project Euler #6.
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
######## optimized sumofsqures function into single return.
######## optimized for user input

def sumofsquares(start, end):
    return sum([x**2 for x in range(start,end +1)])
    

def squareofsum(start, end):
    total = sum(range(start, end+1))
    return total**2

def finalarith(x,y):
    sumsq = sumofsquares(x,y)
    sqsum = squareofsum(x,y)
    print(sqsum - sumsq)

def main():
    x = int(input("Bottom number of range? (interger)")) 
    y = int(input("Top number of range? (interger)")) 
    finalarith(x,y)

if __name__ == '__main__':
    main()
