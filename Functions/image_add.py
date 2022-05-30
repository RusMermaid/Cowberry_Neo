from PIL import Image as IMG

def img_add_h(img1, img2=None):
	if img2 is None:
		return img1
	else:
		img_new = IMG.new("RGB", (img1.width + img2.width, max(img1.height, img2.height)))
		img_new.paste(img1, (0, 0))
		img_new.paste(img2, (img1.width, 0))
		return img_new

def img_add_v(img1, img2=None):
	if img2 is None:
		return img1
	else:
		img_new = IMG.new("RGB", (img1.width, img1.height + img2.height))
		img_new.paste(img1, (0, 0))
		img_new.paste(img2, (0, img1.height))
		return img_new

def img_add_h_with_color(img1, img2=None, c=None): #Добавление картинки по горизонтали с заполнением недостающих символов
	if img2 is None:
		return img1
	else:
		if c is None:
			c = "#000000" #Если не получилось сделать прямоугольник, то оставшееся пространство по горизонтали заполнится черным цветом
		else:
			c = c
		img_new = IMG.new("RGB", (img1.width + img2.width, max(img1.height, img2.height)), color=c)
		img_new.paste(img1, (0, 0))
		img_new.paste(img2, (img1.width, 0))
		return img_new

def img_add_v_with_color(img1, img2, c=None): #Добавление картинки по вертикали с заполнением недостающих символов
	if img2 is None:
		return img1
	else:
		if c is None:
			c = "#fcd1cc" #Если не получилось сделать прямоугольник, то оставшееся пространство по горизонтали заполнится светло-розовым цветом
		else:
			c = c
		img_new = IMG.new("RGB", (max(img1.width, img2.width), img1.height + img2.height), color=c)
		img_new.paste(img1, (0, 0))
		img_new.paste(img2, (0, img1.height))
	return img_new


def img_add_h_list(img_list): #Соединение изображений в списке по горизонтали
	cumulative_img = img_list.pop(0)
	while not img_list == []:
		cumulative_img = img_add_h(cumulative_img, img_list.pop(0))
	return cumulative_img

def img_add_v_list(img_list): #Соединение изображений в списке по вертикали
	cumulative_img = img_list.pop(0)
	while not img_list == []:
		cumulative_img = img_add_v(cumulative_img, img_list.pop(0))
	return cumulative_img

def img_repeat_h(img, n:int):
	img_list = [img] * n
	return img_add_h_list(img_list)

def img_black_h(img_list, total_num_img):
	total_w = total_num_img * 5
	set_w = len(img_list) * 5
	wanted_w = total_w - set_w
	repeats = wanted_w // 5
	
	return [IMG.new("RGB", size=(5, 5), color="#000000")] * repeats

def img_add_list_2d(img_2d_list): #Соединение изображений в 2d списке
	img_cols = []
	maxi = 0
	for row in img_2d_list:
		if len(row) >= maxi:
			maxi = int(len(row))

	for row in img_2d_list:
		if len(row) < maxi:
			row.extend(img_black_h(img_2d_list, maxi))
	
	for row in img_2d_list:
		
		if row == []:
			row.append(img_repeat_h(IMG.new("RGB", size=(5, 5), color="#000000"), maxi))
			#row = img_add_h_list(row)
		else:
			row.append(img_add_h_list(row))
	
	for row in img_2d_list:
		
		img_cols.append(row[0])
		
	return img_add_v_list(img_cols)