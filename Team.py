def howmanysure(theproblems):
	problemgood = 0
	allproblems = theproblems.split("\n")[2:]
	#Square brackets after list names are slicing lists
	for i in allproblems[:-1]:
		total = 0
		for number in i.split(" "):
			total += int(number)
		if total >= 2:
			problemgood += 1
	return problemgood



theproblemsarehere = """
3
1 0 0
0 1 1
1 1 1
"""


print(howmanysure(theproblemsarehere))
