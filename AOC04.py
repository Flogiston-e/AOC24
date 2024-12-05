xmasL = [[x for x in row] for row in open("04.txt").read().strip().split("\n")]

count = 0

for r in range(len(xmasL)):
    for c in range(len(xmasL[0])):
        for i in [1,-1,0]:
            for j in [0,1,-1]:
                if 0 <= min(r,r+3*i) <= len(xmasL)-1 and 0 <= max(r,r+3*i) <= len(xmasL)-1:
                    if 0 <= min(c,c+3*j) <= len(xmasL[0])-1 and 0 <= max(c,c+3*j) <= len(xmasL[0])-1:
                        if xmasL[r][c] + xmasL[r+1*i][c+1*j] + xmasL[r+2*i][c+2*j] + xmasL[r+3*i][c+3*j] == "XMAS":
                            count += 1

print(count)
count = 0

for r in range(1,len(xmasL)-1):
    for c in range(1,len(xmasL[0])-1):
        if xmasL[r-1][c-1] + xmasL[r][c] + xmasL[r+1][c+1] in ["MAS","SAM"]:
            if xmasL[r-1][c+1] + xmasL[r][c] + xmasL[r+1][c-1] in ["MAS","SAM"]:
                count += 1

print(count)