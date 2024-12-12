stones = open("11.txt").read().strip().split(" ")
stones = [int(x) for x in stones]

def Lsplit(s):
    return (s-s%(10**(len(str(s))//2)))//(10**(len(str(s))//2))

def Rsplit(s):
    return s%(10**(len(str(s))//2))

seen = {}

def sc(s,depth):
    if depth == 0:
        return 1
    if (s,depth) in seen:
        return seen[(s,depth)]
    if s == 0:
        ans = sc(1,depth-1)
    elif len(str(s))%2 == 0:
        ans = sc(Rsplit(s),depth-1) + sc(Lsplit(s),depth-1)
    else:
        ans = sc(s*2024,depth-1)
    seen[(s,depth)] = ans
    return ans

print(sum([sc(stone,25) for stone in stones]))
print(sum([sc(stone,75) for stone in stones]))