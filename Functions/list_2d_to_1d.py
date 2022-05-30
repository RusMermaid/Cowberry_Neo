def list_2d_to_1d(list_2d): #Перевод двумерного списка в одномерный
	list_1d = []
	for i in list_2d:
		for j in i:
			list_1d.append(j)
	return list_1d