start = 1
end = 5
# Nested loop to print the multiplication table
for i in range(start, end + 1):
    for j in range(start, end+1):  # Multiplying by numbers 1 to 5
        product = i * j
        print(f"{i} * {j} = {product}")
