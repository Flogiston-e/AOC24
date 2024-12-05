orders, updates = open("05.txt").read().strip().split("\n\n")

updatesL = [update.split(",") for update in updates.split("\n")]
ordersL = [order.split("|") for order in orders.split("\n")]

count1 = 0
count2 = 0

for update in updatesL:
    updsort = ["" for _ in update]
    revorders = []
    good = True
    for order in ordersL:
        if order[0] in update and order[1] in update:
            if update.index(order[0]) > update.index(order[1]):
                good = False
            revorders.append(order)

    for num in update:
        rank = 0
        for revorder in revorders:
            if num == revorder[1]:
                rank += 1
        updsort[rank] = num
  
    if good:
        count1 += int(update[len(update)//2])
    else:
        count2 += int(updsort[len(updsort)//2])
print(count1,count2)