def abcs(nowiknowmyabcs):
	abclist = [int(i) for i in nowiknowmyabcs.split(" ") if len(i) > 0]
	abclist.sort()
	abclist.pop(abclist.index(abclist[0]+abclist[1]))
	return f'{abclist[0]} {abclist[1]} {abclist[2]}'


#STUFF TO CHECK IT WORKS BELOW

import random

def makestringtocheck():
	newstring = ""
	a,b,c = random.randint(1,3),random.randint(3,7),random.randint(7,10)
	thelist = [a,b,c,a+b,b+c,c+a,a+b+c]
	random.shuffle(thelist)
	for i in thelist:
		newstring += str(i) + " "
	print(f'A : {a} B : {b} C : {c}')
	return newstring

stringtouse = makestringtocheck()
print(stringtouse)
print(abcs(stringtouse))