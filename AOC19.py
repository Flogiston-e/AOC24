towels, designs = open("19.txt").read().strip().split("\n\n")
towels = [list(x) for x in towels.split(", ")]
designs = [list(x) for x in designs.split("\n")]
p1,p2 = 0,0

for design in designs:
    dlen = len(design)
    Q = {0}
    ways = [[] for _ in range(dlen)]
    answers = [1]+[0 for _ in range(dlen)]
    while Q:
        i = Q.pop()
        for ti,towel in enumerate(towels):
            tlen = len(towel)
            if dlen >= i+tlen:
                if design[i:i+tlen] == towel:
                    Q.add((i+tlen))
                    ways[i].append(tlen)
        if i == dlen:
            for i,way in enumerate(ways):
                for jump in way:
                    answers[i+jump] += answers[i]
            p1 += 1
            p2 += answers[-1]
            
print(p1)
print(p2)