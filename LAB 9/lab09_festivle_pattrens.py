
print("====================================================")
print("             FESTIVAL DECORATION DESIGNER")
print("====================================================")

n = int(input("Enter the number of rows: "))

print("\nPattern 1: Star Triangle")
print("-" * 40)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern 2: Number Triangle")
print("-" * 40)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern 3: Inverted Star Triangle")
print("-" * 40)
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern 4: Pyramid")
print("-" * 40)
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()

print("====================================================")