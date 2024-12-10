map = open("10.txt").read().strip().split("\n")
map = [[int(x) for x in list(row)] for row in map]

paths = []
pheads = []
rating = 0
index = 0
H = len(map)
W = len(map[0])

for i,row in enumerate(map):
    for j,pos in enumerate(row):
        if pos == 0:
            paths.append((i,j,0,index))
            pheads.append(set())
            index += 1

while paths:
    loc = paths.pop(0)
    if loc[2] == 9:
        pheads[loc[3]].add((loc[0],loc[1]))
        rating += 1
    else:
        for dir in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0 <= loc[0]+dir[0] < H and 0 <= loc[1]+dir[1] < W:
                if map[loc[0]+dir[0]][loc[1]+dir[1]] == loc[2] + 1:
                    paths.append((loc[0]+dir[0], loc[1]+dir[1], loc[2]+1, loc[3]))

print(sum([len(x) for x in pheads]))
print(rating)