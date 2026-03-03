def is_toeplitz(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True


# ---- Input Section ----
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

# ---- Display Matrix ----
print("\nYour Matrix:")
for row in matrix:
    print(row)

# ---- Check Toeplitz ----
if is_toeplitz(matrix):
    print("\nMatrix is Toeplitz ✅")
else:
    print("\nMatrix is NOT Toeplitz ❌")