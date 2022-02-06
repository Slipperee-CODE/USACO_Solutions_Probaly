allthestuff = """
1 3
1 1
1 2
1 2
"""

def promotioncount(allthestuff):
	los = allthestuff.split("\n")
	platbefore,platafter,goldbefore,goldafter,silverbefore,silverafter,bronzebefore,bronzeafter = int(los[1].split(" ")[0]),int(los[1].split(" ")[1]),int(los[2].split(" ")[0]),int(los[2].split(" ")[1]),int(los[3].split(" ")[0]),int(los[3].split(" ")[1]),int(los[4].split(" ")[0]),int(los[4].split(" ")[1])

	dictofranksbeforeandafter = {"plat" : [platbefore,platafter], "gold" : [goldbefore,goldafter], "silver" : [silverbefore,silverafter], "bronze" : [bronzebefore,bronzeafter]}
	dictofranksmove = {"plat" : 0, "gold" : 0, "silver" : 0, "bronze" : 0}
	ranklist = [i for i in dictofranksmove.keys()]



	for rank in ranklist:
		for i in range(abs(dictofranksbeforeandafter[rank][0]-dictofranksbeforeandafter[rank][1])):
			for ranksdown in ranklist[ranklist.index(rank):]:
				dictofranksmove[ranksdown] += 1


	newstring = ""
	for i in dictofranksmove:
		if i != "bronze":
			newstring += str(dictofranksmove[i]) + "\n"

	return newstring






print(promotioncount(allthestuff))