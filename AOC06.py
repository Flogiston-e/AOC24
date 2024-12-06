map = [list(row) for row in open("06.txt").read().strip().split("\n")]
from copy import deepcopy

for row in range(len(map)-1):
    for column in range(len(map[row])-1):
        if map[row][column] == "^":
            guard = [row,column,0]

def pathfinder(map,loc,dirs,mode):
    path = []
    while True:
        if 0 < loc[0] < len(map)-1 and 0 < loc[1] < len(map[0])-1:
            path.append(deepcopy(loc))
            if map[loc[0] + dirs[loc[2]][0]] [loc[1] + dirs[loc[2]][1]] == "#":
                loc[2] = (loc[2]+1)%4
            else:
                loc[0] += dirs[loc[2]][0]
                loc[1] += dirs[loc[2]][1]
            if loc in path:
                return 1        
        else:
            if mode == 0:
                return path
            else:
                return 0

dirs = [(-1,0,),(0,1),(1,0),(0,-1)]
path = pathfinder(map,deepcopy(guard),dirs,0)

p1 = len(set((l[0],l[1]) for l in path)) + 1 # + 1 for the edge loc
print(p1)

p2 = 0
blocktested = []
for p in path:
    blocked = (p[0] + dirs[p[2]][0], p[1] + dirs[p[2]][1])
    if blocked not in blocktested:
        omap = deepcopy(map)
        omap[blocked[0]][blocked[1]] = "#"
        p2 += pathfinder(omap,list(p),dirs,1)
    blocktested.append(blocked)
   
print(p2)