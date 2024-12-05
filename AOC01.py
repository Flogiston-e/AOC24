pairs = open("01.txt").read().strip().split("\n")

num1,num2 = [],[]

sum = 0
for p in range(len(pairs)):
    num1.append(int(pairs[p].split("   ")[0]))
    num2.append(int(pairs[p].split("   ")[1]))

num1.sort()
num2.sort()

for i in range(len(pairs)):
    sum += abs(num1[i] - num2[i])

mult = 0
for l in range(len(pairs)):
    for r in range(len(pairs)):
        if num1[l] == num2[r]:
            mult += num2[r]

print(sum)
print(mult)