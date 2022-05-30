def isprime(num:int): #Проверка, является ли длина строки простым числом
	if num > 1:
		for i in range(2, int((num)**0.5)+1):
			if num%i == 0:
				return False
		return True
	else:
		return False

def rectangular_str(string:str, step:int=None): #создание "прямоугольника" (списка строк) из строки
	if step is None:
		sqrt = int(len(string)**0.5)
		rectangular_str(string, sqrt)
	else:

		parts = [string[i:i+step] for i in range(0, len(string), step)]
		return parts

def char_2d(string:str, step:int=None):
	if step is None:
		sqrt = int(len(string)**0.5)
		parts = rectangular_str(string, sqrt)
	char_parts = []

	for i in parts:
		char_parts.append([j for j in i])
	return char_parts