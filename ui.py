
from logger import input_data, print_data, find_data

def find_data_ui():
    
    print('В каком файле будем искать: \n'
          '1 - В первом\n'
          '2 - Во втором\n'
          '> ', end='')
    
    comand_1 = int(input(''))
    
    while comand_1 < 1 or 2 < comand_1:
        print('Неправильный ввод')
        comand_1 = int(input('Введите число: '))

    print('Как будем искать: \n'
          '1 - По фамилии\n'
          '2 - По имени\n'
          '3 - По фамилии и имени\n'
          '> ', end='')
    
    comand_2 = int(input(''))

    while comand_2 < 1 or 3 < comand_2:
        print('Неправильный ввод')
        comand_2 = int(input('Введите число: '))
    
    find_data(comand_1, comand_2)

def interface():
    
    print('Добрый день!\n'
          'Вы попали на специальный бот-справочник!\n'
          '1 - Запись данных\n'
          '2 - Вывод данных\n'
          '3 - Найти (изменить, удалить) данные\n'
          '0 - Выйти из программы')
    
    comand = int(input('> '))

    while comand < 0 or 3 < comand:
        print('Неправильный ввод')
        comand = int(input('Введите число: '))

    if comand == 1:
        input_data()
    elif comand == 2:
        print_data()
    elif comand == 3:
        find_data_ui()
    elif comand == 0:
        print('До скорых всреч!')

