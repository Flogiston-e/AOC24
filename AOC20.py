input = open("20.txt").read().strip().split("\n")
maze = [list(row) for row in input]

for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == "S": start = (y,x)
        if maze[y][x] == "E": end = (y,x)

no_cheat = {start:0}
Q = {(start,0)}
while Q:
    (y,x),time = Q.pop()
    for dy,dx in ((1,0),(0,1),(-1,0),(0,-1)):
        if maze[y+dy][x+dx] != "#" and (y+dy,x+dx) not in no_cheat:
            Q.add(((y+dy,x+dx),time+1))
            no_cheat[(y+dy,x+dx)] = time+1

for cdy,cdx in ((3,3),(21,21)):
    cArea = {}
    for j in range(0,cdy):
        for i in range(0,cdx-j):
            for jsign in (1,-1):
                for isign in (1,-1):
                    cArea[(jsign*j, isign*i)] = i+j

    ans = 0
    for (y,x),time in no_cheat.items():
        for (j,i),dt in cArea.items():
            if (y+j,x+i) in no_cheat:
                if no_cheat[(y+j,x+i)]-(time+dt) >= 100:
                    ans += 1
    print(ans)