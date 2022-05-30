from PIL import Image as IMG
from Functions.pillow_colors import *
from Functions.list_2d_to_1d import *
from Functions.Encription.first_encription import *

class EncryptedImage:
	def __init__(self, image, full_str:str=None):
		#конструктор
		self.image = image
		self.width, self.height = image.size # Из кортежа берет значения height и width
		self.full_str = full_str

	def __str__(self):
		plaintext = str(self.decode())
		return plaintext

	def img_splitting_2d(self): #данная функциявозвращает 2d список картинок для раскодирования
		repeats = (self.width//5, self.height//5)
		rows = []
		imgs_2d = [] #Итоговый двумерный список картинок из ячеек 5х5
		singles = []
		row_area = (0, 0, self.width, 5) #Картинка одного ряда
		unit_area = (0, 0, 5, 5) #Один квадрат из строки

		for i in range(repeats[1]):
			rows.append(self.image.crop(row_area))
			#В цикле добавляется картинка одного ряда из исходного изображения
			row_area = (0, row_area[1]+5, self.width, row_area[3]+5)
			#Сдвиг ряда вниз на одну ячейку/клетку 5х5
		
		for i in range(len(rows)):
			#Проходит по каждому ряду из списка рядов
			for j in range(repeats[0]):
				#Проходит по каждой клетке в ряду
				#print(f"{i}-{j}={(j*5, 0, j*5, 5)}")
				singles.append(rows[i].crop((j*5, 0, 5+j*5, 5)))

				#unit_area = (j*5, 0, 5+j*5, 5)
				#Добавляет каждую клетку ряда в список
				#Смещает на одну клетку вправо по ряду
				
			imgs_2d.append(singles)
			singles = []
		return imgs_2d #массив из списков клеток каждого ряда в картинке
	
	def img_in_1d(self): #Перевод двумерного списка картинок в одномерный
		list_imgs_2d = self.img_splitting_2d()
		list_imgs_1d = []

		for i in list_imgs_2d:
			list_imgs_1d.extend(i) #Перевод 2D списка в 1D без расшифровки
		#Раскодировка шифра Цезаря начинается
		list_imgs_1d = EncryptedImage.decryption_list(list_imgs_1d)
		#Раскодировка шифра Цезаря заканчивается
		print(len(list_imgs_1d), " img_in_1d ")
		return list_imgs_1d
	
	@staticmethod
	def decryption_list(enc_image_list, key:int=1):
		dekey = len(enc_image_list) - key
		image_list = enc_image_list[dekey:] + enc_image_list[:dekey]
		#Дешифровка закодированного списка картинок 
		return image_list #Возвращает раскодированный список картинок
	
	def create_encrypted_colors(self): #Получение закодированных цветов
		img_1d = list_2d_to_1d(self.img_splitting_2d())
		#encrypted_colors = [RGB_to_pillow_hex(self.i.getpixel(pixel)) for i in img_1d]
		encrypted_colors = []
		for j in img_1d:
			rgb = RGB_to_pillow_hex(j.getpixel((1, 1)))
			encrypted_colors.append(rgb)
		for i in encrypted_colors:
			if i == "#000000":
				encrypted_colors.remove(i)

		return encrypted_colors
	def decode(self): #Функция раскодирования
		encrypted_colors = self.create_encrypted_colors()

		list_values = [archashing(i) for i in encrypted_colors]
		#Из-за неточности сигмоидной функции придётся заменить некоторые символы с помощью if-ов
		for i in range(len(list_values)):
			if list_values[i] == ord("䑒"):
				list_values[i] = ord("a")

			if list_values[i] == ord("䔾"):
				list_values[i] = ord("b")

			if list_values[i] == ord("䘯"):
				list_values[i] = ord("c")

			if list_values[i] == ord("䜦"):
				list_values[i] = ord("d")

			if list_values[i] == ord("䘩"):
				list_values[i] = ord("F")

			if list_values[i] == ord("䏋"):
				list_values[i] = ord(" ")

			if list_values[i] == ord("蔞"):
				list_values[i] = ord("ж")

			if list_values[i] == ord("藂"):
				list_values[i] = ord("р")

			if list_values[i] == ord("莥"):
				list_values[i] = ord("О")

			if list_values[i] == ord("䔪"):
				list_values[i] = ord("6")

			if list_values[i] == ord("䱹"):
				list_values[i] = ord("«")

			if list_values[i] == ord("䱹") or list_values[i] == ord("𤏢"):
				list_values[i] = ord("…")


		self.plaintext = ""

		chars_list = [chr(i) for i in list_values] #Генератор списка ссимволов
		full_str = self.plaintext.join(i for i in chars_list) #создание получившейся строки

		self.plain_text = full_str
		return self.plain_text #Возвращает раскодированную строку