text = """
10 7
hello my name is Bessie and this is my essay
"""

def formattext(text):
	allinfo = text.split("\n")
	maxchars = int(allinfo[1].split(" ")[1])
	texttoformat = allinfo[2]
	charsonline = 0
	formatedtext = ""
	for i in texttoformat.split(" "):
		if charsonline + len(i) > maxchars:
			formatedtext += "\n"
			charsonline = 0
		formatedtext += i + " "
		charsonline += len(i)
	return formatedtext


print(formattext(text))