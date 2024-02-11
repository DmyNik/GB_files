
from data_create import name_data, surname_data, phone_data, address_data

def write_file1(strings): # Перезапись файла 1
    
    with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
        
        for i in strings:
            for j in i:
                f.write(j+'\n')
            f.write('\n')

        print('Внимание: файл "data_first_variant.csv" записан!')

    from ui import interface
    interface()


def write_file2(strings): # Перезапись файла 2
    
    with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
        
        for i in strings:
            
            flg = False
            str = ''
            
            for j in i:
                if flg:
                    str += ';' + j
                else:
                    str += j
                    flg = True
            
            f.write(str)
            f.write('\n')
    
        print('Внимание: файл "data_second_variant.csv" записан!')

    from ui import interface
    interface()


def edit_data(file, data_list, cmd, namelist): # Редактирование записей справочника

    findSurname = namelist[0]
    findName = namelist[1]
    cnt = 0 # Счетчик совпадений
    coincidence_list = list() # Список совпадений
    
    for i in data_list:
        if cmd == 1: # Поиск по фамилии
            if i[1] == findSurname:
                cnt += 1
                coincidence_list.append(i)
        elif cmd == 2: # Поиск по имени
            if i[0] == findName:
                cnt += 1
                coincidence_list.append(i)
        elif cmd == 3: # Поиск по фамилии и имени
            if i[1] == findSurname and i[0] == findName:
                cnt += 1
                coincidence_list.append(i)

    print(f'Найдено {cnt} совпадени(е/й):')
    
    if cnt < 1: 
        
        from ui import interface
        interface()

    else:

        for i in range(0, len(coincidence_list)):
            print('#' + str(i+1) + ':\t', end='')
            for j in range(0, len(coincidence_list[i])):
                if j != 0:
                    print(', ' + coincidence_list[i][j], end='')
                else:
                    print(coincidence_list[i][j], end='')
            print('')
        
        print('Какую запись изменить (удалить)?\n'
              '[Подсказка: введите порядковый номер совпадения или 0 для выхода в главное меню.]')
        edtNum = int(input('> '))

        while edtNum < 0 or cnt < edtNum:
            print('Неправильный ввод')
            edtNum = int(input('Введите число: '))

        if edtNum != 0:
            
            print('Данную запись нужно изменить или удалить?\n'
                  '[Подсказка: 1 - изменить, 2 - удалить, 0 - выход в главное меню.]')
            edtNum2 = int(input('> '))

            while edtNum2 < 0 or 2 < edtNum2:
                print('Неправильный ввод')
                edtNum2 = int(input('Введите число: '))

            if edtNum2 != 0:

                tupleToEdit = coincidence_list[edtNum-1]
                
                if edtNum2 != 2:
                    
                    editName = name_data()
                    editSurname = surname_data()
                    editPhone = phone_data()
                    editAddress = address_data()
                
                    tupleNew = tuple([editName, editSurname, editPhone, editAddress])

                    print('Записть: "', *tupleToEdit, '"')
                    print('Будет заменена на: "', *tupleNew, '"')

                cnt = 0 # Еще раз считаем совпадения

                for i in range(len(data_list)):                
                    
                    if cmd == 1: # Поиск по фамилии
                        if data_list[i][1] == findSurname:
                            cnt += 1
                            if cnt == edtNum:
                                if edtNum2 == 1:
                                    data_list[i] = tupleNew
                                elif edtNum2 == 2:
                                    ii = i

                    elif cmd == 2: # Поиск по имени
                        if data_list[i][0] == findName:
                            cnt += 1
                            if cnt == edtNum:
                                if edtNum2 == 1:
                                    data_list[i] = tupleNew
                                elif edtNum2 == 2:
                                    ii = i

                    elif cmd == 3: # Поиск по фамилии и имени
                        if data_list[i][1] == findSurname and data_list[i][0] == findName:
                            cnt += 1
                            if cnt == edtNum:
                                if edtNum2 == 1:
                                    data_list[i] = tupleNew
                                elif edtNum2 == 2:
                                    ii = i

                if edtNum2 == 2:
                    data_list.pop(ii)

                if file == 1:
                    write_file1(data_list)
                elif file == 2:
                    write_file2(data_list)
            
            else:
                from ui import interface
                interface()   
            
        else:
            from ui import interface
            interface()


def find_data_in1file(cmd, namelist): # Поиск записи в 1-ом файле

    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        
        data_first = f.readlines()
        data_first = list(map(lambda x: x.replace('\n', '') , data_first))
        data_first_list = []
        j = 0
        
        for i in range(len(data_first)):
            if data_first[i] == '' or i == len(data_first) - 1:
                data_tuple = tuple(filter(lambda x: (x != ''), data_first[j:i+1]))
                data_first_list.append(data_tuple)
                j = i
                       
        data_first_list = list(filter(lambda x: (len(x) != 0), data_first_list))

        edit_data(1, data_first_list, cmd, namelist)
    

def find_data_in2file(cmd, namelist): # Поиск записи во 2-ом файле
    
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:

        data_second = f.readlines()
        data_second = list(map(lambda x: (x.replace('\n', '')), data_second))
        data_second = list(filter(lambda x: (len(x) != 0), data_second))
        data_second_list = []
        
        for i in range(len(data_second)): 
            data_tuple = tuple(list(data_second[i].split(';')))
            data_second_list.append(data_tuple)

    edit_data(2, data_second_list, cmd, namelist)

    
def input_data(): # Ввод данных в файл   
    
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    
    var = int(input(f'В каком формате записать данные?\n\n'
                    f'1 Вариант:\n\n'
                    f'{name}\n{surname}\n{phone}\n{address}\n\n'
                    f'2 Вариант:\n\n'
                    f'{name};{surname};{phone};{address}\n\n'
                    f'Выберите вариант: '))
    
    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name};{surname};{phone};{address}\n\n')


def print_data(): # Вывод данных из файлов
    
    print('Вывожу данные из первого файла: \n')
    
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        
        data_first = f.readlines()
        data_first = list(map(lambda x: x.replace('\n', '') , data_first))
        data_first_list = []
        j = 0
        
        for i in range(len(data_first)):
            if data_first[i] == '' or i == len(data_first) - 1:
                data_tuple = tuple(filter(lambda x: (x != ''), data_first[j:i+1]))
                data_first_list.append(data_tuple)
                j = i
                       
        data_first_list = list(filter(lambda x: (len(x) != 0), data_first_list))

        for i in range(len(data_first_list)):
            for j in data_first_list[i]: print(j)
            print('')

    print('Вывожу данные из второго файла: \n')
    
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        
        data_second = f.readlines()
        data_second = list(map(lambda x: (x.replace('\n', '')), data_second))
        data_second = list(filter(lambda x: (len(x) != 0), data_second))
        data_second_list = []
        
        for i in range(len(data_second)): 
            data_tuple = tuple(list(data_second[i].split(';')))
            data_second_list.append(data_tuple)
        
        for i in data_second_list:
            for j in range(len(i)): 
                if j != 0: print(';' + i[j], end='') 
                else: print(i[j], end='')    
            print('')

        print('')
    
    from ui import interface
    interface()


def find_data(cmd1 = 1, cmd2 = 1): # Поиск записей в фалах
    
    namelist = list()
    namelist.append('')
    namelist.append('')

    if cmd2 == 1:
        namelist[0] = input('Введите фамилию: ')
    elif cmd2 == 2:
        namelist[1] = input('Введите имя: ')
    elif cmd2 == 3:
        namelist[0] = input('Введите фамилию: ')
        namelist[1] = input('Введите имя: ')

    if cmd1 == 1:
        find_data_in1file(cmd2, namelist)
    elif cmd1 == 2:
        find_data_in2file(cmd2, namelist)

#print_data()
