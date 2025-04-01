import numpy as np
# 1. Creating NumPy arrays
print("1. Creating NumPy arrays:")
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
c = np.zeros((3, 3))
d = np.ones((2, 4))
e = np.arange(0, 10, 2)
f = np.linspace(0, 1, 5)

print("a:", a)
print("b:\n", b)
print("c:\n", c)
print("d:\n", d)
print("e:", e)
print("f:", f)

# 2. Array operations
print("\n2. Array operations:")
print("a + 2:", a + 2)
print("a * 2:", a * 2)
print("a ** 2:", a ** 2)
print("np.sqrt(a):", np.sqrt(a))
print("np.exp(a):", np.exp(a))

# 3. Array indexing and slicing
print("\n3. Array indexing and slicing:")
print("b[1]:", b[1])
print("b[:, 1]:", b[:, 1])
print("b[0:2, 1:3]:\n", b[0:2, 1:3])

# 4. Array reshaping
print("\n4. Array reshaping:")
g = np.arange(12).reshape(3, 4)
print("g:\n", g)
print("g.T:\n", g.T)  # Transpose

# 5. Basic statistics
print("\n5. Basic statistics:")
print("Mean of a:", np.mean(a))
print("Sum of a:", np.sum(a))
print("Max of b:", np.max(b))
print("Min of b:", np.min(b))

# 6. Boolean indexing
print("\n6. Boolean indexing:")
print("a > 3:", a[a > 3])

# 7. Broadcasting
print("\n7. Broadcasting:")
h = np.array([1, 2, 3])
i = np.array([[1], [2], [3]])
print("h + i:\n", h + i)

# 8. Matrix multiplication
print("\n8. Matrix multiplication:")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A:\n", A)
print("B:\n", B)
print("Dot product (A @ B):\n", A @ B)
print("Matrix multiplication (np.matmul(A, B)):\n", np.matmul(A, B))

# 9. Solving linear equations
print("\n9. Solving linear equations:")
X = np.array([[1, 2], [3, 4]])
Y = np.array([5, 11])
print("X:\n", X)
print("Y:", Y)
print("Solution to XZ = Y:")
Z = np.linalg.solve(X, Y)
print("Z:", Z)
print("Verification XZ:", X @ Z)