import math
from Functions.pillow_colors import *
'''
Начало английского и конец русского алфавитов
32 dec = space char
48 dec = 0 (zero) char
64 dec = @ char
65 dec = A char
90 dec = Z char
97 dec = a char
122 dec = z char

English [32-90, 97-122]

0410 hex = А char
042f hex = Я char
0430 hex = а char
044f hex = я char
0451 hex = ё char
0463 hex = ѣ char 
Русский [0410-0463] hex [1040-1123] dec

Final [32-128, 1040-1123]
'''

def hashing(x:int): #Кодирование с помощью сигмоидной функции
	hashed_value = int(1123/(1123 + (x))*1000000)
	hashed_value = pillow_dec_to_hex(hashed_value)
	return hashed_value

def archashing(hashed_value): #Раскодирование с помощью сигмоидной функции
	archashed_value = pillow_hex_to_dec(hashed_value)
	if archashed_value > 0:
		archashed_value = int((1123/(archashed_value/1000000) - 1123))
	return archashed_value