# moduels
import random
import rich
from rich import print
from rich.console import Console
from rich.table import Table
import eel

# choise action
print()
print(
	"[bold cyan]Выберете, что вы хотите сделать:[/bold cyan]\n"
	" [1] [yellow]Посмотреть таблицу[/yellow]\n"
	" [2] [yellow]Проверить себя тестом[/yellow]\n"
	" [3] [yellow]О приограмме и авторе[/yellow]"
)

choise_action = input("Введице цифру действия: ")

# table action (1)
if choise_action == "1":

	table = Table(title="Названия и химические знаки некоторых элементов")

	table.add_column("Русское название", justify="left", style="cyan", no_wrap=True)
	table.add_column("Латинское название", style="magenta", justify="left")
	table.add_column("Химический знак", justify="center", style="green")
	table.add_column("Произношение знака в формуле вецества", justify="left", style="white")

	table.add_row("Азот", "Нитрогениум", "N", "Эн")
	table.add_row("Алюминий", "Алюминиум", "Al", "Алюминий")
	table.add_row("Водород", "Гидрогениум", "H", "Аш")
	table.add_row("Железо", "Феррум", "Fe", "Феррум")
	table.add_row("Кислород", "Оксигениум", "O", "О")
	table.add_row("Медь", "Купрум", "Cu", "Купрум")
	table.add_row("Ртуть", "Гидраргирум", "Hg", "Гидраргирум")
	table.add_row("Свинец", "Плюмбум", "Pb", "Плюмбум")
	table.add_row("Сера", "Сульфур", "S", "Эс")
	table.add_row("Углевод", "Карбонеум", "C", "Цэ")
	table.add_row("Фосфор", "Фосфорум", "P", "Пэ")
	table.add_row("Хлор", "Хлорум", "Cl", "Хлор")

	console = Console()
	console.print(table)

	otdl_window = input("Вывести в отдельном окне? [Д / н] ")
	if otdl_window == "Д":
		eel.init('')
		eel.start('table.html', size=(700, 620))
		eel.stop('table.html')

# test action (2)
elif choise_action == "2":

	while choise_action == "2":

		# random element
		him_el_list = ['N', 'Al', 'H', 'Fe', 'O', 'Cu', 'Hg', 'Pb', 'S', 'C', 'P', "Cl"]
		rand_him_el = random.choice(him_el_list)
		print("Химический знак: [bold cyan]" + rand_him_el + "[/bold cyan]")

		# ture / false
		ture = "[bold green]Верно![/bold green]"
		false = "[bold red]Неверно![/bold red]"

		# Азот - N - Нитрогениум
		if rand_him_el == 'N':
			rus_name = "Азот"
			lat_name = "Нитрогениум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Алюминий - Al - Алюминиум
		elif rand_him_el == "Al":
			rus_name = "Алюминий"
			lat_name = "Алюминиум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Водород - H - Гидрогениум
		elif rand_him_el == 'H':
			rus_name = "Водород"
			lat_name = "Гидрогениум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Железо - Fe - Феррум
		elif rand_him_el == 'Fe':
			rus_name = "Железо"
			lat_name = "Феррум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Кислород - O - Оксигениум
		elif rand_him_el == 'O':
			rus_name = "Кислород"
			lat_name = "Оксигениум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Медь - Cu - Купрум
		elif rand_him_el == 'Cu':
			rus_name = "Медь"
			lat_name = "Купрум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Ртуть - Hg - Гидраргирум
		elif rand_him_el == 'Hg':
			rus_name = "Ртуть"
			lat_name = "Гидраргирум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Свинец - Pb - Плюмбум
		elif rand_him_el == 'Pb':
			rus_name = "Свинец"
			lat_name = "Плюмбум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Сера - S - Сульфур
		elif rand_him_el == 'S':
			rus_name = "Сера"
			lat_name = "Сульфур"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Углерод - C - Карбонеум
		elif rand_him_el == 'C':
			rus_name = "Углерод"
			lat_name = "Карбонеум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Фосфор - P - Фосфорум
		elif rand_him_el == 'P':
			rus_name = "Фосфор"
			lat_name = "Фосфорум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

		# Хлор - Cl - Хлорум
		elif rand_him_el == 'Cl':
			rus_name = "Хлор"
			lat_name = "Хлорум"
			check_true = input("Русское название: ")
			if check_true == rus_name:
				print(ture)
			else:
				print(false + " Правильно: " + rus_name)
			check_lat_true = input("Латинское название: ")
			if check_lat_true == lat_name:
				print(ture)
			else:
				print(false + " Правильно: " + lat_name)

			question_exit = input("Продолжить? [Д / н] ")
			if question_exit == "Д":
				pass
			elif question_exit == "н":
				exit()

# credits action (3)
elif choise_action == "3":
	print()
	print("Оригинальный создатель: Vionar Brekky (Вионар Брекки)")
	print(" - Discord: [bold cyan]Viönar#5526[/bold cyan]")
	print(" - Сделано за 2 часа (дада я знаю какой я улитка прост я на питоне кидить не умею) для тестировки перед химичиским дисктантом в школе (да мне нечем было заняться на дистанционке во время выборов :/ ).")
	input()


# non listed action (abobus)
else:
	print("[ [bold red]ОШИБКА[/bold red] ] Введено не верное значение")