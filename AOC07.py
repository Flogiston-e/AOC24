eqs = open("07.txt").read().strip().split("\n")
from copy import deepcopy

def comb(l,mode):
    Q = [[]]
    while len(Q[0])<len(l)-1:
        x = Q.pop(0)
        y = deepcopy(x)
        z = deepcopy(x)
        x.append(0), y.append(1), z.append(2)
        Q.append(x), Q.append(y)
        if mode:
            Q.append(z)
    return Q

for part in range(2):
    ans = 0
    for eq in eqs:
        eq = eq.split(":")
        eq[1] = eq[1].split(" ")
        eq[1].pop(0)
        for ops in comb(eq[1],part):
            sum = int(eq[1][0])
            p = 0
            for op in ops:
                if sum > int(eq[0]):
                    break
                else:
                    p += 1
                    if op == 0:
                        sum += int(eq[1][p])
                    elif op == 1:
                        if sum == 0:
                            sum += int(eq[1][p])
                        else:
                            sum *= int(eq[1][p])
                    else:
                        if p == 1:
                            sum = int(eq[1][0]+eq[1][1])
                        else:
                            sum = int(str(sum)+eq[1][p])
                
            if sum == int(eq[0]):
                ans += sum
                break 

    print(ans)