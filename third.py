person = ['Энакин Скайуокер',
		  41,
		  ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
		  {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
		  ]

# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы
# Your code here /ᐠ˵- ⩊ -˵マ

def task_1(person):
	full_name = person[0].split()
	print(f"Персона: {full_name[1]}, {full_name[0]}")


def task_2(person):
	print(person[1])


def task_3(person):
	places = person[2]
	print(", ".join(places))


def task_4(person):
	print(len(person[2]))


def task_5(person):
	print('Звезда Смерти' in person[2])


def task_6(person):
	print(person[3]['световой меч'])


def task_7(person):
	person[1] = 42
	print(person[1])


def task_8(person):
	if 'Эндор' not in person[2]:
		person[2].append('Эндор')
	print(person[2])


def task_9(person):
	if person[3]['ранг'] == 'лорд ситхов':
		print("Энакин - лорд ситхов")
	else:
		print("Энакин - джедай")


def task_10(person):
	if len(person[2]) > 4:
		print("Энакин побывал во многих местах")
	else:
		print("Энакин не так много путешествовал")


def main():
	person = ['Энакин Скайуокер',
			  41,
			  ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
			  {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
			  ]

	while True:
		task_number = input("Введите номер задания (1-10) или 'выход' для завершения: ")

		if task_number.lower() == 'выход':
			break

		try:
			task_number = int(task_number)
			if task_number < 1 or task_number > 10:
				print("Неверный номер задания. Пожалуйста, введите число от 1 до 10.")
				continue

			task_functions = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10]
			task_functions[task_number - 1](person)

		except ValueError:
			print("Неверный ввод. Пожалуйста, введите число от 1 до 10 или 'выход'.")


if __name__ == "__main__":
	main()
