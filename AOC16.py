input = open("16.txt").read().strip().split("\n")
from collections import defaultdict
map  = [list(row) for row in input]
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

H = len(map)
W = len(map[0])
Q = defaultdict(list)
Q[0].append((H-2,1,0,[(H-2,1)])) # cost:[(y,x,dir,path),....] dir 0123,
seen = {} # (y,x,dir):cost

best_paths = []
foundit = False
while Q:
    cost = sorted(list(Q.keys()))[0]
    poss = Q.pop(cost)
    for pos in poss:
        
        if pos[0] == 1 and pos[1] == W-2:
            foundit = True
            best_paths.append(pos)
        
        if (pos[0],pos[1],(pos[2]+1)%4) not in seen:
            Q[cost+1000].append((pos[0],pos[1],(pos[2]+1)%4,pos[3]))
            seen[(pos[0],pos[1],(pos[2]+1)%4)] = cost + 1000
        elif seen[(pos[0],pos[1],(pos[2]+1)%4)] == cost + 1000:
            Q[cost+1000].append((pos[0],pos[1],(pos[2]+1)%4,pos[3]))

        if (pos[0],pos[1],(pos[2]-1)%4) not in seen:
            Q[cost+1000].append((pos[0],pos[1],(pos[2]-1)%4,pos[3]))
            seen[(pos[0],pos[1],(pos[2]-1)%4)] = cost + 1000
        elif seen[(pos[0],pos[1],(pos[2]-1)%4)] == cost + 1000:
            Q[cost+1000].append((pos[0],pos[1],(pos[2]-1)%4,pos[3]))

        if map[pos[0]+dirs[pos[2]][0]][pos[1]+dirs[pos[2]][1]] != "#":
            if (pos[0]+dirs[pos[2]][0], pos[1]+dirs[pos[2]][1], pos[2]) not in seen:
                Q[cost+1].append((pos[0]+dirs[pos[2]][0], pos[1]+dirs[pos[2]][1], pos[2], pos[3]+[(pos[0]+dirs[pos[2]][0], pos[1]+dirs[pos[2]][1])]))
            elif seen[(pos[0]+dirs[pos[2]][0], pos[1]+dirs[pos[2]][1], pos[2])] == cost+1:
                Q[cost+1].append((pos[0]+dirs[pos[2]][0], pos[1]+dirs[pos[2]][1], pos[2], pos[3]+[(pos[0]+dirs[pos[2]][0], pos[1]+dirs[pos[2]][1])]))

    if foundit:
        break

best_positions = set()
print(cost)
[[best_positions.add(pos) for pos in path[3]] for path in best_paths]
print(len(best_positions))