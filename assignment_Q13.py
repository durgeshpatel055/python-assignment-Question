#Ramesh and Suresh playing a simple game. they have to put some number of Stones from one place to another and started doing their work. They decided, they end up with a fun challenge who will put the last Stone. They to follow a simple rule, In the i'th round, Ramesh puts i stones whereas Suresh puts ix2 stones. There are only N stones, you need to help find the challenge result to find who put the last stone.

N = int(input())

total = 0
i = 1

while total < N:
    total += i
    if total >= N:
        print("Ramesh")
        break
    total += i * 2
    if total >= N:
        print("Suresh")
        break
    i += 1
