map = [list(x) for x in open("08.txt").read().strip().split("\n")]
from collections import defaultdict

anttypes = defaultdict(list)
for y,row in enumerate(map):
    for x,obj in enumerate(row):
        if obj != ".":
            anttypes[obj].append((y,x))

locations1, locations2 = set(), set()
for anttype in anttypes:
    for loc1 in anttypes[anttype]:
        for loc2 in anttypes[anttype]:
            if loc1 != loc2:
                if 0 <= 2*loc1[0] - loc2[0] < len(map) and 0 <= 2*loc1[1] - loc2[1] < len(map[0]):
                    locations1.add((2*loc1[0] - loc2[0],2*loc1[1] - loc2[1]))
                for n in range(-max(len(map),len(map[0])),max(len(map),len(map[0]))):
                    if 0 <= loc1[0] - n*(loc1[0] - loc2[0]) < len(map) and 0 <= loc1[1] - n*(loc1[1] - loc2[1]) < len(map[0]):
                        locations2.add((loc1[0] - n*(loc1[0]-loc2[0]), loc1[1] - n*(loc1[1]-loc2[1])))
print(len(locations1), len(locations2))