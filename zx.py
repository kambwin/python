import random

while True:  
	command = input("Скажи мудрость\n")
	phrases = ['Знать ничего не хочу', 'Выйти']
	if command == "Скажи мудрость":  
		print (random.choice(phrases))  
	if command == 'Знать ничего не хочу': 
		print('Ок(((')  
	if command == 'Выйти':
	   print("Выйти")  
	   break   
else:  
    print('Неверный ввод')