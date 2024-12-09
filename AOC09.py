disk = open("09.txt").read().strip()

# PART 1
data = []
space = []
for x in range(len(disk)//2):
    data.append([x for _ in range(int(disk[x*2]))])
    space.append(["." for _ in range(int(disk[x*2+1]))])
data.append([x+1 for _ in range(int(disk[-1]))])
      
fullbreak = False
for datai in range(len(data)):
    datablock = data[len(data)-1-datai]
    runs = len(datablock)
    for i in range(runs):
        value = datablock.pop(-1)
        breaker = False
        for spaceI in range(len(space)):
            for spaceJ in range(len(space[spaceI])):
                if len(data)-1-datai <= spaceI:
                    fullbreak = True
                    break
                if space[spaceI][spaceJ] == ".":
                    space[spaceI][spaceJ] = value
                    breaker = True
                    break
            if breaker or fullbreak:
                break
        if fullbreak:
            break
    if fullbreak:
        break
data[len(data)-1-datai].append(value)

sortdisk = []

for x in range(len(space)):
    sortdisk.extend(data.pop(0))
    sortdisk.extend(space.pop(0))

sum = 0
for x in range(len(sortdisk)):
    if sortdisk[x] == ".":
        break
    sum += sortdisk[x]*x

print(sum)

# PART 2
data = []
space = []
for x in range(len(disk)//2):
    data.append([x for _ in range(int(disk[x*2]))])
    space.append(["." for _ in range(int(disk[x*2+1]))])
data.append([x+1 for _ in range(int(disk[-1]))])

for datai in range(len(data)):
    datablock = data[len(data)-1-datai]
    for spacei in range(len(space)):
        spaceblock = space[spacei]
        if spacei < len(data)-1-datai:
            if len(datablock) <= spaceblock.count("."):
                for i in range(len(datablock)):
                    for j in range(len(spaceblock)):
                        if spaceblock[j] == ".":
                            spaceblock[j] = datablock[i]
                            datablock[i] = "."
                            break

sortdisk = []

for x in range(len(space)):
    sortdisk.extend(data.pop(0))
    sortdisk.extend(space.pop(0))

sum = 0
for x in range(len(sortdisk)):
    if sortdisk[x] != ".": 
        sum += sortdisk[x]*x
print(sum)