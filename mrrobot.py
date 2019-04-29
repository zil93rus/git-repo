import os
import shutil

answer = input("Это робот помощник. Хотите продолжить ? [Y/N]: ")
while answer != "N":
    print("[1] - Список файлов нажмите")
    print("[2] - Информацию о системе нажмите")
    print("[3] - Вывести список процессов")
    print("[4] - Дублирование файлов в текущей директории")
    print("[5] - Дублирование указанного файла в текущей директории")
    print("[6] - Удаление дубликатов файлов в указанной директории")
    print("[7] - Удаление случайного файла в указанной директории")
    do = input("Выберите действие(Q -выход): ")
    if do == "1":
        print("Список файлов")
        print(os.listdir())
    elif do == "4":
        print("Дублирование файлов в текущей директории")
        filelist = os.listdir()
        count = 0
        for i in filelist:
            if os.path.isfile(i):
                newfile = i + ".copy"
                shutil.copy(i, newfile)
                count += 1
                if os.path.exists(newfile):
                    print("Файл " + newfile + " скопирован удачно")
        print("Всего скопировано ", count)
    elif do == "5":
        print("Дублирование указанного файла в текущей директории")
        filelist = os.listdir()
        userfile = input("Введите имя файла: ")
        if os.path.isfile(userfile):
            newfile = userfile + ".copy"
            shutil.copy(userfile, newfile)
    elif do == "6":
        print("Удаление дубликатов файлов в указанной директории")
        filelist = os.listdir()
        count = 0
        for i in filelist:
            if os.path.isfile(i):
                if i.endswith(".copy"):
                    os.remove(i)
                    count += 1
                    if not os.path.exists(i):
                        print("Файл " + i + " удален удачно")
        print("Всего удалено: ", count)
    elif do == "Q":
        print("До свидания")
        break
