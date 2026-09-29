n = input("Введіть кількість рядків: ")

if n.isdigit():
    n = int(n)

    if n == 0:
        print("Список порожній")
    else:
        found = False

        for i in range(n):
            row = input("Введіть рядок " + str(i + 1) + ": ")
            has_digit = False

            for symbol in row:
                if symbol.isdigit():
                    has_digit = True
                    break

            if has_digit:
                print(row)
                found = True

        if not found:
            print("Рядків із цифрами немає")
else:
    if len(n) > 1 and n[0] == "-" and n[1:].isdigit():
        print("Кількість рядків не може бути від’ємною")
    else:
        print("Вхідні дані - не коректні")