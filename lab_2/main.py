import os
from lab2 import folder_summary

folder = input("Введіть шлях до папки: ")
ext = input("Введіть розширення файлів (Enter — .txt): ")

if ext == "":
    ext = ".txt"
elif not ext.startswith("."):
    ext = "." + ext

if not os.path.exists(folder):
    print("Помилка: такої папки не існує")

elif not os.path.isdir(folder):
    print("Помилка: вказаний шлях не є папкою")

elif not os.access(folder, os.R_OK | os.X_OK):
    print("Помилка: немає доступу до вмісту папки")

elif not os.access(folder, os.W_OK):
    print("Помилка: неможливо створити файл у папці")

elif ext == "." or "/" in ext or "\\" in ext:
    print("Помилка: неправильне розширення")

else:
    try:
        count = folder_summary(folder, ext)

        print()
        print("Зведення успішно створено")
        print("Кількість оброблених файлів:", count)
        print("Файл зведення:", os.path.join(folder, "summary.txt"))

    except UnicodeError:
        print("Помилка: один із файлів не є текстом у кодуванні UTF-8")

    except OSError:
        print("Помилка: не вдалося прочитати файл або записати summary.txt")