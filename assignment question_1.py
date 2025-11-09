# Program to print Pascal's Triangle without using a function

rows = int(input("Enter number of rows: "))

print("Pascal's Triangle:")

for i in range(rows):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
