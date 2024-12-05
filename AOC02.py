reports = open("02.txt").read().strip().split("\n")
from copy import deepcopy

count1,count2 = 0,0

for report in reports:
    creps = report.split(" ")
    
    acrep = []
    acrep.append(creps)
    for c in range(len(creps)): 
        o = deepcopy(creps)
        o.pop(c)
        acrep.append(o)
    

    b = 0
    for crep in acrep:
        mode = 0
        for n in range(len(crep)-1):
            if 0 < abs(int(crep[n])-int(crep[n+1])) < 4:
                if mode == 0:
                    if int(crep[n])-int(crep[n+1]) < 0:
                        mode = -1
                    else:
                        mode = 1
                elif mode == -1 and int(crep[n])-int(crep[n+1]) < 0:
                    1
                elif mode == 1 and int(crep[n])-int(crep[n+1]) > 0:
                    1
                else:
                    break
            else:
                break
            if n == len(crep)-2:
                count2 += 1
                if acrep.index(crep) == 0:
                    count1 += 1
                b = 1
        if b == 1:
            break
        
print(count1,count2)