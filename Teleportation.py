# 3 10 8 2

def findroute(number):
	numberlist = number.split(" ")
	firstpos,secondpos,teleporter1,teleporter2 = int(numberlist[0]),int(numberlist[1]),int(numberlist[2]),int(numberlist[3])

	tpdistance = teleporterdistance(firstpos,secondpos,teleporter1,teleporter2)
	if abs(firstpos-secondpos) < tpdistance:
		return abs(firstpos-secondpos)
	else:
		return tpdistance

def teleporterdistance(firstpos,secondpos,teleporter1,teleporter2):
	distancemoved = 0
	if abs(firstpos-teleporter1) < abs(firstpos-teleporter2):
		distancemoved += abs(firstpos-teleporter1) + abs(teleporter2-secondpos)
	else:
		distancemoved += abs(firstpos-teleporter2) + abs(teleporter1-secondpos)
	
	return distancemoved



print(findroute("3 15 14 2"))