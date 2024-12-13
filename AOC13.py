input = open("13.txt").read().strip().split("\n\n")
from numpy import array,linalg

for m in [0,10**13]:
    ans = 0
    for machine in input:
        a,b,prize = machine.split("\n")
        ax, ay = int(a.split("+")[1].split(",")[0]), int(a.split("+")[2])
        bx, by = int(b.split("+")[1].split(",")[0]), int(b.split("+")[2])
        px, py = int(prize.split("=")[1].split(",")[0])+m, int(prize.split("=")[2])+m
        A = array([[ax,bx],[ay,by]])
        b = array([[px],[py]])
        Ainv = linalg.inv(A)
        X = Ainv @ b
        x,y = round(X[0][0],3),round(X[1][0],3)
        if [x,y] == [int(x),int(y)]:
            ans += int(x*3+y)
    print(ans)