#WORK IN PROGRESS KINDA WORKS ¯\_(ツ)_/¯
numberstofind = int(input())
numberstofindlist = []
for i in range(numberstofind):
	numberstofindlist.append(int(input()))

def numpos(num):
	currentnum = 0
	while True:
		if num <= (((10**(currentnum+1)) - (10**currentnum)))*(currentnum+1):
			currentnum +=1
			break
		currentnum += 1

	numinsection = (num - (10**(currentnum-1)))//currentnum

	trunum = 10**(currentnum-1) + numinsection

	truindex = str(trunum)[num%currentnum]

	return truindex

finalprint = []
for i in numberstofindlist:
	finalprint.append(numpos(i))

for i in finalprint:
	print(i)
