#Davos wants to build a game and he wants to build a staircase in the game.
#The staircase must be in the form of

#
##
###
####


# Read input
N = int(input())

# Print staircase pattern
for i in range(1, N + 1):
    print('#' * i)
