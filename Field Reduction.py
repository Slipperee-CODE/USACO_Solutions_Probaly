cowinput = """
6
1 1
7 8
10 9
8 12
4 100
50 7
"""
#12

def fieldreduce(cows):
	cows = cows.split("\n")[2:-1]
	cows = [i.split(" ") for i in cows]
	
	#FIND AVG COW POS
	avgx = 0
	avgy = 0
	for i in cows:
		avgx += int(i[1])
		avgy += int(i[0])
	avgx = avgx//len(cows)
	avgy = avgy//len(cows)
	#print(avgx)
	#print(avgy)
	#MAKE NEW COW LIST OF BEST COWS
	newcowlist = []
	for i in cows:
		newcowlist.append(abs(avgx-int(i[1]))+abs(avgy-int(i[0])))
	#print(newcowlist)
	littelestnot3 = sorted(newcowlist)[:-3]
	bestcows = []
	#REMOVE NOT GOOD COWS
	for i in littelestnot3:
		bestcows.append(cows[newcowlist.index(i)])
	#print(bestcows)
	#FIND AREA OF ALL COWS ENCLOSED ENCLORUSRE
	firstpos = sorted([int(i[0]) for i in bestcows])
	secondpos = sorted([int(i[1]) for i in bestcows])
	firstposdifference = abs(firstpos[0] - firstpos[-1])
	secondposdifference = abs(secondpos[0] - secondpos[-1])
	#RETURN AREA
	return secondposdifference*firstposdifference
print(fieldreduce(cowinput))