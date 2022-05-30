from Classes.Class_Encrypted_Image import EncryptedImage
from Functions.rectangular_str import rectangular_str
from Functions.image_add import img_add_list_2d
from Functions.Encription.first_encription import *
#импорт нужных классов и функций

class String:
	def __init__(self, chars="", str_ascii=None, str_unicode=None, str_hex_color=None, full_img=None):
		if chars is None:
			self.chars = ""
		else:
			self.chars = str(chars) #Превращает chars в нужную нам строку

		self.chars_list = [i for i in chars]
		self.unicode_chars_list = [ord(i) for i in self.chars_list]


	def __str__(self):
		return self.chars #изменяет значение функции str
	
	def ISascii(self):
		return str(self).isascii() #Проверяет, все ли символы имеют значения в ascii

	def hex_color_list(self):
		list_colors = []
		for i in self.unicode_chars_list:
			hashed_value = hashing(i)
			list_colors.append(hashed_value)
		return list_colors

		
	def chars_to_image_list(self):
		image_list = []
		for i in self.hex_color_list():
			image_list.append(IMG.new(mode="RGB", size=(5,5), color=i))
		
		return image_list 
		#Переводит список символов в одномерный список изображений
	
	def chars_to_image_list2d(self, step:int=None):
		image_list = self.chars_to_image_list()
		#Шифр Цезаря начинается
		enc_image_list = String.encryption_list(image_list)
		#Шифр Цезаря заканчивается
		if step is None:
			step = int(len(self.chars)**0.5) 
		image_list2d = rectangular_str(enc_image_list, step)
		return image_list2d #Превращает строку в двумерный список картинок

	@staticmethod
	def encryption_list(image_list, key:int=1):
		#image_list = image_list[key:] + image_list[:key]
		#порядок картинок в  массиве
		return image_list #Возвращает список картинок с шифром Цезаря
	
	def str_to_full_img(self):

		self.full_img = img_add_list_2d(self.chars_to_image_list2d())
		self.full_img = EncryptedImage(self.full_img)
		return self.full_img #Возвращает объект EncriptedImage
