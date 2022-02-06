def bananabuyingbananza(allthestuff):
	price,money,bananastohave = int(allthestuff.split(" ")[0]),int(allthestuff.split(" ")[1]),int(allthestuff.split(" ")[2])
	bananasbought = 0
	moneyborrowed = 0

	for banana in range(1,bananastohave+1):
		if money - (price*banana) < 0:
			moneyborrowed += abs(money - price*banana)
			money += abs(money - price*banana)

		money = money - (price*banana)
		bananasbought += 1
	return moneyborrowed

print(bananabuyingbananza("1 2 3"))