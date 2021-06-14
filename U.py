import random

def performLogin():
	Попытки1 = 2
	while True:
		Login = input("Введите ваш логин: ")
		if (Login == "vuk") or (Login == "Валерий") or (Login == "sas"):
			print("Логин Классифицирован. Здраствуйте, Валерий!\n")
			break
		elif (Login == "auk") or (Login == "Алексей"):
			print("Логин Классифицирован. Здраствуйте, Алексей!\n")
			break
		elif (Login == "sas") or (Login == "SasAnanas") or (Login == "Елена"):
			print("Логин Классифицирован. Здраствуйте, Елена!\n")	
		else:
			print("Неверная попытка! Осталось", Попытки1, "попыток\n")

		Попытки1 -= 1
		if Попытки1 < 0:
			print("Обновите сессию и попробуйте снова\n")
			raise SystemExit

	while True:
		Password = input("Введите пароль, " + Login + ": \n")
		if (Password == "LolHero") or (Password == "1"):
			print("Доступ разрешен. Здраствуйте, " + Login + ": \n") 
			break
		else:
			print("Неверный пароль\n")

print("Здраствуйте, я АББ!\n")
performLogin()

pravda = True
while pravda:
     RandomChislo = random.randint(1,1000)
     joke = random.randint(1,3)
     Coin = random.randint(1,3)
     Sovet = random.randint(1,3)	

     Command = input("Выберите функцию, " + Login + ": \n")

     if joke == 1 and (Command == "Пошути") or joke == 1 and (Command == "пошути") or joke == 1 and (Command == "Расскажи анекдот") or joke == 1 and (Command == "расскажи анекдот"):
     	print("Сколько бы Ярик не учил русский всё равно получается ку-ка-ре-ку\n") and str(print(joke))
     	Command = (" ".join(input("Введите вашу команду," + Login + ": \n").split()))

     if joke == 2 and (Command == "Пошути") or joke == 2 and (Command == "пошути") or joke == 2 and (Command == "Расскажи анекдот") or joke == 2 and (Command == "расскажи анекдот"):
     	print("Ярик разбил подбородок, но ничего страшного я могу разбить и второй\n") and str(print(joke))
     	Command = (" ".join(input("Введите вашу команду," + Login + ": \n").split()))

     if joke == 3 and (Command == "Пошути") or joke == 3 and (Command == "пошути") or joke == 3 and (Command == "Расскажи анекдот") or joke == 3 and (Command == "расскажи анекдот"):
     	print("Нового года не дед мороз, будет Ислам принял\n") and str(print(joke))
     	Command = (" ".join(input("Введите вашу команду," + Login + ": \n").split()))	

     if Coin == 1 and (Command == "Подбрось монету") or Coin == 1 and (Command == "подбрось монету") or Coin == 1 and (Command == "Монетка") or Coin == 1 and (Command == "монетка"):
     	print("Орёл\n")
     	Command = (" ".join(input("Введите вашу команду," + Login + ": \n").split()))

     if Coin == 2 and (Command == "Подбрось монету")  or Coin == 2 and (Command == "подбрось монету") or Coin == 2 and (Command == "Монетка") or Coin == 2 and (Command == "монетка"):
     	print("Решка\n") 
     	Command = (" ".join(input("Введите вашу команду," + Login + ": \n").split()))		

     if Coin == 3 and (Command == "Подбрось монету") or Coin == 3 and (Command == "подбрось монету") or Coin == 3 and (Command == "Монетка") or Coin == 3 and (Command == "монетка"):
     	print("Ребро\n") 
     	Command = (" ".join(input("Введите вашу команду," + Login + ": \n").split()))

     if (Command == "Случайное число") or (Command == "случайное число") or (Command == "Рандом") or (Command == "рандом"):
     	print(Login + ", вам выпало: " + str(RandomChislo), "\n")  
     	Command = (" ".join(input("Введите вашу команду," + Login + ": \n").split()))

     if (Command == "help") or (Command == "Help") or (Command == "Помоги") or (Command == "помоги"):
     	print("Список команд на сегодняшний день: \n    Монетка - бот подбрасывает монетку и показывает орла или решку \n    Пошути - Рассказывает не смешную шутку про Ярика (Сам их придумал:)) \n    Рандом - показывает случайное число от 1 до 1000\n")
     	Command = (" ".join(input("Введите вашу команду," + Login + ": \n").split()))

     if (Command == "Отключись") or (Command == "отключись") or (Command == "Стоп") or (Command == "стоп"):
     	print("Отключаюсь. До следующей встречи, " + Login)
     	raise SystemExit 

     else:
     	print("Команда не распознана\n")
     	Command = (" ".join(input("Введите вашу команду," + Login + ": ").split()))
