#

def nextMove(n,r,c,grid):
    #print(grid)
    [[pm, pn]] = [ [i, item.find("p")] for (i, item) in enumerate(grid) if "p" in item ]
    if pm != r:
        nextMove = "UP" if pm < r else "DOWN"
    else:
        nextMove = "LEFT" if pn < c else "RIGHT"
    return nextMove

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))