input = [list(row) for row in open("12.txt").read().strip().split("\n")]
H = len(input)
W = len(input[0])
map = {}

for i in range(H):
    for j in range(W):
        map[(i,j)] = input[i][j]

otherareas = set()
for i in [-1,H]:
    for j in range(0,W):
        otherareas.add((i,j))
for j in [-1,W]:
    for i in range(0,H):
        otherareas.add((i,j))

def fencesadd(fences,m,p):
    if move[0]<p[0] or move[1]<p[1]:
        fences.add((m[0]+p[0],m[1]+p[1],1))
    else:
        fences.add((m[0]+p[0],m[1]+p[1],0))
    return fences

sum1 = 0
sum2 = 0
while map:
    places, regtype = map.popitem()
    region = set()
    region.add(places)
    places = [places]
    fence = 0
    fences = set()
    sides = 0
    while places:
        p = places.pop(0)
        for move in ((p[0]+1,p[1]), (p[0],p[1]+1), (p[0]-1,p[1]), (p[0],p[1]-1)):
            if move in region:
                1
            elif move in otherareas:
                fence += 1
                fences = fencesadd(fences,move,p)
            elif map[move] == regtype:
                places.append(move), region.add(move)
                map.pop(move)
            else:
                fence += 1
                fences = fencesadd(fences,move,p)

    for (y,x) in [(H,W),(W,H)]:
        for under_over in (0,1):
            for i in range(-1,y*2,2):
                onfence = False
                for j in range(0,x*2,2):
                    if (i,j,under_over) in fences:
                        if not onfence:
                            sides +=1
                        onfence = True
                    else:
                        onfence = False

    sum1 += len(region)*fence
    sum2 += len(region)*sides
    for spot in region:
        otherareas.add(spot)

print(sum1)
print(sum2)