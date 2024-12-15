robots = open("14.txt").read().strip().split("\n")
from time import sleep
def pprint(rob):
    image = ""
    for y in range(103):
        image += "\n"
        for x in range(101):
            if (x,y) in rob:
                image += "#"
            else:
                image += "." 
    print(image)
    sleep(0.5)

def blinker(blinks):
    roblocs = []
    for robot in robots:
        loc,vel = robot.split(" ")
        x,y = loc.split("=")[1].split(",")
        vx,vy = vel.split("=")[1].split(",") # list comp 1 row
        x = (int(x)+int(vx)*blinks)%101
        y = (int(y)+int(vy)*blinks)%103
        roblocs.append((x,y))
    return(roblocs)

roblocs = blinker(100)

q1,q2,q3,q4 = 0,0,0,0
for robloc in roblocs:
    if robloc[0] <= 49 and robloc[1] <= 50:
        q1 += 1
    if robloc[0] <= 49 and 52 <= robloc[1]:
        q2 += 1
    if 51 <= robloc[0] and robloc[1] <= 50:
        q3 += 1
    if 51 <= robloc[0] and 52 <= robloc[1]:
        q4 += 1

print(q1*q2*q3*q4)
sleep(3)

for blinks in range(48,10000,101):
    roblocs = blinker(blinks)
    pprint(roblocs)
    print(blinks)