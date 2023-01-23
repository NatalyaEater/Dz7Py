import shutil
import os

x = 0

def get_commands(a):
    global x
    x = a
    while True:
        if a == 1:
            data = open('Spot.txt', 'r',encoding='UTF-8')
            for line in data:
                print(line)
            data.close()
            a=0
        elif a == 2:
            print('Введите имя')
            n = str(input())
            with open('Spot.txt', 'a') as file:
                file.write(f'\n{n}')
                file.close()
            print('Введите номер')
            t = str(input())
            with open('Spot.txt', 'a') as file:
                file.write(f'    {t}')
                file.close()
            a=0
        elif a == 0:
            print('Для просмотра справочника нажмите 1')
            print('Для записи нового контакта нажмите 2')
            print('Для экспорта в cvs нажмите 3')
            print('Для импорта базы в txt нажмите 4')
            print('Для экспорта базы в txt нажмите 5')
            a=int(input())
        elif a == 3:
            shutil.copyfile('Spot.txt', 'Spot1.txt')
            os.rename('Spot1.txt', 'Spot1.csv')
            print(r'Выполнен экспорт базы в csv')
            a=0
        elif a == 4:
            with open('Basa_import.txt', "r", encoding='utf-8') as imp:
                with open('Spot.txt', "a", encoding='utf-8') as basa:
                    for line in imp:
                        basa.write(f'\n{line}')
            print(r'Выполнен импорт базы в txt')
            a=0
        elif a==5:
            with open('Spot.txt', "r", encoding='utf-8') as basa_1:
                with open('spot2_exp.txt', "w", encoding='utf-8') as basa_2:
                    for line in basa_1:
                        basa_2.write(line)
            print(r'Выполнен экспорт базы в txt')
            a=0
        else:
            print('Введите верно команду')
            a=int(input())
            print()
