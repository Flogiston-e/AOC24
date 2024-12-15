from time import sleep
input = open("15.txt").read().strip().split("\n\n")
dirs = {"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}
map1 = [list(row) for row in input[0].split("\n")]
for row in range(len(map1)):
    for col in range(len(map1[0])):
        if map1[row][col] == "@":
            rob1 = [row,col]

map2 = []
for i,row in enumerate(input[0].split("\n")):
    map2.append([])
    for j,c in enumerate(row):
        if c == "#":
            map2[i].extend(["#","#"])
        elif c == "O":
            map2[i].extend(["[","]"])
        elif c == ".":
            map2[i].extend([".","."])
        elif c == "@":
            map2[i].extend(["@","."])
            rob2 = [i,j*2]

maps = [map1,map2]
robs = [rob1,rob2]

def yisintheway(itw,map,move,dirs):
    moveto = map[itw[0]][itw[1]]
    if moveto == ".":
        return [[None]]
    if moveto == "[":
        return [[itw[0]+dirs[move][0],itw[1]], [itw[0]+dirs[move][0],itw[1]+1]]
    if moveto == "]":
        return [[itw[0]+dirs[move][0],itw[1]], [itw[0]+dirs[move][0],itw[1]-1]]
    if moveto == "O":
        return [[itw[0]+dirs[move][0],itw[1]]]
    if moveto == "#":
        return [[False]]

def xisintheway(itw,map,move,dirs):
    moveto = map[itw[0]][itw[1]]
    if moveto == ".":
        return [[None]]
    if moveto == "[":
        return [[itw[0],itw[1]+2], [itw[0],itw[1]+1]]
    if moveto == "]":
        return [[itw[0],itw[1]-2], [itw[0],itw[1]-1]]
    if moveto == "O":
        return [[itw[0],itw[1]+dirs[move][1]]]
    if moveto == "#":
        return [[False]]

for part in range(2):
    map = maps[part]
    rob = robs[part] 
    moves = []
    for row in input[1].split("\n"):
        moves.extend(list(row))
    while moves:
        move = moves.pop(0)
        intheway = [[rob[0]+dirs[move][0], rob[1]+dirs[move][1]]]
        moveaway = [[rob[0]+dirs[move][0], rob[1]+dirs[move][1]]]
        while intheway:
            itw = intheway.pop(0)
            if move in "<>":
                blockage = xisintheway(itw,map,move,dirs)
                if len(blockage) == 2:
                    moveaway.append(blockage.pop(1))
            elif move in "^v":
                blockage = yisintheway(itw,map,move,dirs)
            intheway.extend(blockage)
            moveaway.extend(blockage)
            if intheway[-1] == [False]:
                moveaway = []
                break
            elif intheway[-1] == [None]:
                intheway.pop(-1)
                moveaway.pop(-1)
        moved = set()
        moveaway.reverse()
        for push in moveaway:
            if tuple(push) not in moved:
                map[push[0]][push[1]] = map[push[0]-dirs[move][0]][push[1]-dirs[move][1]]
                map[push[0]-dirs[move][0]][push[1]-dirs[move][1]] = "."
            moved.add(tuple(push))
        if moved:
            rob = [rob[0]+dirs[move][0], rob[1]+dirs[move][1]]

    sum = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "[" or map[y][x] == "O":
                sum += y*100 + x
    print(sum)