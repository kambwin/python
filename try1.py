# -*- coding: utf-8 -*-
age = int(input("Введите возраст:\n"))
if age >= 0 and age < 18:
	print ("Вы юноша")
elif age >= 18 and age < 45:
	print ("Вы молодой")
if age >= 45 and age < 60:
	print ("Вы среднего возраста")
elif age >= 60 and age < 75:
	print ("Вы пожилой")
if age >= 75 and age < 90:
	print ("Вы старец")
elif age >=90 and age < 110:
	print ("Вы долгожитель")
else:
	print ("Неправильно введен возраст.")
