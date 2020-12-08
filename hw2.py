import random
my_list = ['Знать ничего не хочу', 'Выйти']
n = [my_list]
if "Скажи мудрость":
	print(random.randint(0, n))
	if my_list == "Знать ничего не хочу":
		print ("Ок(((")
	if my_list == "Выйти":
		exit() 
	else:  
		print("Неверный ввод")