# Write a Python program to print "Pascal's Triangle".
# The numbers in the r-th row of Pascal's triangle represent
# the coefficients in the Binomial expansion of (a+b)^{r-1}.
# The first four rows of the Pascal triangle are shown below:-
# 1
# 1 1
# 1 2 1
# 1 3 3 1




def pascal_triangle(n):
    for i in range(n):
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()


n = int(input("Enter number of rows: "))

pascal_triangle(n)
