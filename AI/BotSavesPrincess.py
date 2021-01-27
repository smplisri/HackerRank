#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    position_m, position_p = [], []
    trail = []
    for i in range(0, n):
        for j in range(0, n):
            if grid[i][j] == 'm':
                position_m = [i, j]
            elif grid[i][j] == 'p':
                position_p = [i, j]

    if position_m[0] <= position_p[0]:
        trail.extend(["DOWN"]*(position_p[0]-position_m[0]))
    elif position_m[0] > position_p[0]:
        trail.extend(["UP"]*(position_m[0]-position_p[0]))
    
    if position_m[1] <= position_p[1]:
        trail.extend(["RIGHT"]*(position_p[1]-position_m[1]))
    elif position_m[1] > position_p[1]:
        trail.extend(["LEFT"]*(position_m[1]-position_p[1]))

    for item in trail:
        print(item)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)