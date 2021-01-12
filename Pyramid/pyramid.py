import sys

def pyramid(n, heights):
    stacks = [int(s) for s in heights.split()]

    # Building an "increasing" pyramid from left to right
    inc_pyram = [0] * n
    # The first stack's height cannot exceed 1 or the number of available squares in the first given stack
    inc_pyram[0] = min(1, stacks[0])
    for i in range(1, n):
        inc_pyram[i] = min(
        inc_pyram[i - 1] + 1, # Cannot exceed the height of the stack to the left + 1
        stacks[i], # Cannot exceed the number of available squares
        i + 1) # Cannot exceed i+1 as the heighest possible pyramid has height 1 at index 0

    # Building a "decreasing" pyramid (height increases from right to left)
    dec_pyram = [0] * n
    # The last stack's height cannot exceed 1 or the number of available squares in the last given stack
    dec_pyram[n - 1] = min(1, stacks[n - 1])
    for i in range(n - 2, -1, -1):
        dec_pyram[i] = min(
        dec_pyram[i + 1] + 1, # Cannot exceed the height of the stack to the right + 1
        stacks[i], # Cannot exceed the number of available squares
        n - i) # Cannot exceed n-i as the heighest possible pyramid has height 1 at index n-1

    # Building a "centered" pyramid from the increasing and the decreasing ones
    centered = [0] * n
    for i in range(n):
        centered[i] = min(inc_pyram[i], dec_pyram[i])

    # Find the index of the stack with maximum height
    # If there are multiple heighest pyramids, we keep the one that we first encountered (the leftmost one)
    max_index = 0
    for i in range(n):
        if centered[i] > centered[max_index]:
            max_index = i

    max_height = centered[max_index] # Maximum height of the pyramid
    print(str(max_height)+" "+str(max_index))


n = int(sys.stdin.readline()) # Number of stacks
heights = sys.stdin.readline() # Heights of the stacks
pyramid(n, heights)
