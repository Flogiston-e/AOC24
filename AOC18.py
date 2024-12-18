input = open("18.txt").read().strip().split("\n")
bytes = [(int(x),int(y)) for byte in input for x,y in [byte.split(",")]]

def calculator(bytes,part1):
    Q, seen = [((0,0),0)], [(0,0)]
    while Q:
        (x,y),steps = Q.pop(0)
        if (x,y) == (70,70):
            if part1: return steps
            return True
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0 <= x+dx <= 70 and 0 <= y+dy <= 70:
                if (x+dx, y+dy) not in seen+bytes:
                    Q.append(((x+dx, y+dy), steps+1))
                    seen.append((x+dx, y+dy))

print(calculator(bytes[0:1024],True))
for i in range(len(bytes),-1,-1):
    if calculator(bytes[0:i],False):
        print(f"{bytes[i][0]},{bytes[i][1]}"); break