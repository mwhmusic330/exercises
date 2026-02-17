### Project Euler Problem Zero


odd_squares = []

for n in range(1,230001,2):
    square = n**2
    odd_squares.append(square)
ans = sum(odd_squares)
print(ans)
