import csv
import os


def output_menu_console(string):
    '''
    Вывод меню в консоль
   
    '''
    os.system('cls')
    with open(string, 'r', encoding='utf-8') as txtfile:
        for line in txtfile:
            print(line.rstrip())


def output_list_contacts_console():
    '''
    Вывод списка контактов в консоль
    '''
    os.system('cls')
    with open('telephone_contacts.csv', 'r', encoding='utf-8') as csvfile:
        print('  СПИСОК КОНТАКТОВ: ')
        print(csvfile.read())
        

def add_contact(contact):
    '''
    Добавления  в файл csv.
    '''
    with open('telephone_contacts.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter= ',')
        writer.writerow(contact)


def del_contact(index):
    '''
    Удаление  контакта в файле csv.
    ''' 
    with open("telephone_contacts.csv","r", encoding='utf-8') as file:
        lines = file.readlines()
    del lines[index]  
    with open("telephone_contacts.csv","w", encoding='utf-8') as file:
        file.writelines(lines)


def contact_search(data):
    '''
    Поиск контакта.
    '''
    line = []
    count = 0
    try:
        open('telephone_contacts.csv')
        with open('telephone_contacts.csv', encoding='utf-8') as csvfile:
            file_reader = list(csv.reader(csvfile, delimiter=','))
            for row in file_reader:
                if data.capitalize() in row:
                   
                    count += 1
                    line.append(row)   
                    index = file_reader.index(row)  
                
            if count == 0:
                print('Эй Кожаный - контакт не найден')
                return None
    except FileNotFoundError:
        print('Кожаный - у тебя нет контактов!')
    return index