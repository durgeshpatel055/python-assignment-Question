# John is trying to solve the arithmetic series (AP). He wants to find two things in the series

a = [2, 6, 9, 12, 15, 18, 21]
sum = 0
APlength = len(a)
for i in range(0, APlength):
    if a[i] == a[APlength-1]:
        print("nth term is: ",a[i])
for i in range(0, APlength):
    sum = sum + a[i]
print("Sum of Arithemetic series is: ", sum)
