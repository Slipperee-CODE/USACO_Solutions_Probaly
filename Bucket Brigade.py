firearea = """
..........
..........
..........
.....L....
..........
.....R....
..........
..........
.....B....
..........
"""


def putoutthefire(firearea):
	cows = 0
	listoflines = [[line for line in i] for i in firearea.split("\n")[1:-1]]

	for index,i in enumerate(listoflines):
		try:
			spotinline = i.index("L")            
			currentpos = [index,spotinline]
		except:
			pass
		try:
			spotinline = i.index("B")            
			barnpos = [index,spotinline]
		except:
			continue 

	while True:
		try:
			if listoflines[int(((barnpos[0] - currentpos[0])//abs(barnpos[0] - currentpos[0]))+currentpos[0])][currentpos[1]] == ".":
				currentpos[0] = currentpos[0] + ((barnpos[0] - currentpos[0])//abs(barnpos[0] - currentpos[0]))
				cows += 1
			else:
				currentpos[1] = currentpos[1] + ((barnpos[1] - currentpos[1] )//abs(barnpos[1] - currentpos[1]))
				cows += 1
		except Exception:
			try:
				currentpos[1] = currentpos[1] + ((barnpos[1] - currentpos[1] )//abs(barnpos[1] - currentpos[1]))
				cows += 1
			except Exception:
				if listoflines[currentpos[0]-1][currentpos[1]] == "R":
					currentpos[1] += 1
					cows += 1
				elif listoflines[currentpos[0]+1][currentpos[1]] == "R":
					currentpos[1] += 1
					cows += 1
				else:
					return cows-1 #FIX IF BARN BEHIND ROCK 
				#CHECK IF ROCK IN WAY THEn ELSE DO THE THING
				#IF DOUBLE ERROR CHECK IF ROCK IN WAY THEN MOVE LEFT OR RIGHT

	

print(putoutthefire(firearea))