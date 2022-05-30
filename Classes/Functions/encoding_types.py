def encodeUnicode(string:str): #перевод строки в Unicode
	return u"{}".format(str(string))

def encodeRaw(string:str): #Перевод строки в raw
	r"{}".format(str(string))
	