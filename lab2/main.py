print("=== Космический корабль «Аврора» ===")
print("Почините реактор и запустите спасательную капсулу!")
print("Введите help, чтобы увидеть команды\n")

room = "bridge"
energy = 100
reactor_fixed = False
has_tool = False

while True:
    print("Текущая комната:", room)
    print("Энергия:", energy, '\n')

    if energy <= 0:
        print("Энергия закончилась!")
        print("Корабль обесточен. Вы проиграли")
        break

    if room == "capsule" and reactor_fixed and energy > 0:
        print("Спасательная капсула успешно запущена!")
        print("Вы спаслись! Победа!")
        break

    command = input("Введите команду: ")

    if command == "help":
        print("Доступные команды:")
        print("help - список команд")
        print("look - осмотреть комнату")
        print("go - перейти в другую комнату")
        print("take - взять предмет")
        print("use - использовать предмет")
        print("inventory - проверить инвентарь")
        print("exit - выйти из игры")

    elif command == "look":
        if room == "bridge":
            print("Вы на мостике корабля")
            print("Отсюда можно попасть в кают-компанию")

        elif room == "mess":
            print("Вы в кают-компании")
            print("Здесь лежит ремонтный инструмент")
            print("Переходы: bridge, reactor, cargo")

        elif room == "reactor":
            print("Вы в реакторном отсеке")
            if reactor_fixed:
                print("Реактор уже отремонтирован")
            else:
                print("Реактор повреждён. Нужен инструмент")

        elif room == "cargo":
            print("Вы в грузовом трюме")
            print("Здесь находятся контейнеры с грузом")

        elif room == "airlock":
            print("Вы в шлюзе.")
            print("Отсюда можно попасть в спасательную капсулу")

        elif room == "capsule":
            print("Вы внутри спасательной капсулы")

    elif command == "go":
        destination = input("Куда перейти? ")

        if destination == room:
            print("Вы уже находитесь здесь")

        elif room == "bridge" and destination == "mess":
            room = destination
            energy -= 5
            print("Вы перешли в кают-компанию.")

        elif room == "mess" and destination == "bridge":
            room = destination
            energy -= 5

        elif room == "mess" and destination == "reactor":
            room = destination
            energy -= 5

        elif room == "reactor" and destination == "mess":
            room = destination
            energy -= 5

        elif room == "mess" and destination == "cargo":
            room = destination
            energy -= 5

        elif room == "cargo" and destination == "mess":
            room = destination
            energy -= 5

        elif room == "cargo" and destination == "airlock":
            room = destination
            energy -= 5

        elif room == "airlock" and destination == "cargo":
            room = destination
            energy -= 5

        elif room == "airlock" and destination == "capsule":
            room = destination
            energy -= 5

        elif room == "capsule" and destination == "airlock":
            room = destination
            energy -= 5

        else:
            print("Нельзя перейти в эту комнату!")

    elif command == "take":
        item = input("Что взять? ")

        if room == "mess" and item == "tool":
            if not has_tool:
                has_tool = True
                print("Вы взяли ремонтный инструмент")
            else:
                print("Инструмент уже у вас")
        else:
            print("Здесь нет такого предмета")

    elif command == "use":
        item = input("Что использовать? ")

        if item == "tool":
            if not has_tool:
                print("У вас нет инструмента")
            elif room != "reactor":
                print("Инструмент нужно использовать в реакторе")
            elif reactor_fixed:
                print("Реактор уже отремонтирован")
            else:
                reactor_fixed = True
                print("Вы успешно починили реактор!")
        else:
            print("Этот предмет нельзя использовать")

    elif command == "inventory":
        if has_tool:
            print("Инвентарь: tool")
        else:
            print("Инвентарь пуст")

    elif command == "exit":
        print("Вы завершили игру")
        break

    else:
        print("Неизвестная команда. Введите help")
