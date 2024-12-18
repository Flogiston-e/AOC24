input = open("18.txt").read().strip().split("\n")
bytes = [(int(x),int(y)) for byte in input for x,y in [byte.split(",")]]

def calculator(bytes,part1):
    Q, seen = [((0,0),0)], [(0,0)]
    while Q:
        loc = Q.pop(0)
        if loc[0] == (70,70):
            if part1: return loc[1]
            return True
        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0 <= loc[0][0]+d[0] <= 70 and 0 <= loc[0][1]+d[1] <= 70:
                if (loc[0][0]+d[0], loc[0][1]+d[1]) not in seen+bytes:
                    Q.append(((loc[0][0]+d[0], loc[0][1]+d[1]), loc[1]+1))
                    seen.append((loc[0][0]+d[0], loc[0][1]+d[1]))

print(calculator(bytes[0:1024],True))
for i in range(len(bytes),0,-1):
    if calculator(bytes[0:i],False):
        print(f"{bytes[i][0]},{bytes[i][1]}"); break