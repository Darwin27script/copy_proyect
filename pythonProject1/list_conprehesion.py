# Usando un bucle for tradicional
squares = []
for x in range(1, 6):
    squares.append(x**2)

# Usando una list comprehension
squares_comp = [x**2 for x in range(1, 6)]

print(squares_comp)  # Output: [1, 4, 9, 16, 25]
