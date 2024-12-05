memory = open("03.txt").read().strip()

memory = memory.split("mul(")

parts = []
sum1 = 0
sum2 = 0
state = 1

for p in memory:
    parts.extend(p.split(")"))

for part in parts: 
    num = part.split(",")
    try:
        n0, n1 = int(num[0]), int(num[1])
        sum1 += n0*n1
        if state:
            sum2 += n0*n1
    except:
        if "don't(" in part:
            state = 0
        elif "do(" in part:
            state = 1

print(sum1,sum2)