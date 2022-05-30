from PIL import Image as IMG
from PIL import ImageColor as Color

def pillow_hex_to_dec(hexi:str):
	hexi = hexi.lower()
	# hexi is in format '#ffffff'
	dec = 0
	hexi_list = []
	l = [16**i for i in range(6)]
	hexi = hexi[1:]
	for i in hexi:
		if i == "a":
			i = 10
		elif i == "b":
			i = 11
		elif i == "c":
			i = 12
		elif i == "d":
			i = 13
		elif i == "e":
			i = 14
		elif i == "f":
			i = 15
		elif i.isdigit():
			i = int(i)
		else:
			print("String is not a hex value")
			return False
		hexi_list.append(i)
	hexi_list.reverse()
	for i, base_to_power in zip(hexi_list, l):
		dec += i * base_to_power
	return dec

  
def pillow_dec_to_hex(number:int):
	hexi = hex(number) #hexadecimal in the format 0xffffff
	hexi = hexi[2:] # removeing '0x'
		
	if len(hexi) < 6:
		missing_size = 6 - len(hexi) # calculating number of '0's to fill in
		hexi = "0" * missing_size + hexi # str * int is repeating str int num of times
		# this if fills in blacks: '1' --> '000001' 
	hexi = "#" + hexi # adding '#' to the start  of hexadecimal color 
	# so hexadecimal '0x0f55ae' turned into pillow form '#0f55ae'
	return hexi

def RGB_to_pillow_hex(rgb):
	hex_color = "{:X}{:X}{:X}".format(rgb[0], rgb[1], rgb[2])
	pillow_hex_color = "#" + "0"*(6-len(hex_color.lower())) + hex_color.lower()
	return pillow_hex_color

