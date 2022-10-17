import cheat as ch
import check as ck


def get_menu_item(n):
    '''
    Получение пункта меню от пользователя
    
    '''
    return ck.check_M('выберете пункт меню: ', n)

 
def convert_type(number):
    '''
    Конвертация типа телефона из числа [1, 6] 
        
    '''
    if number == 1: return 'Сотовый'
    if number == 2: return 'Городской'
    if number == 3: return 'Домашний'
    if number == 4: return 'Рабочий'
    if number == 5: return 'Личный'
    if number == 6: return 'Другое'


def get_name(string):
    '''
    Получение имени,фамилии,отчества,комментария

    '''
    return ck.check_NC(string)


def get_number(string):
    '''
    Получение номера телефона от пользователя
    '''
    return ck.check_NT(string)


def add_contact(contact):
    '''
    Добавление контакта в телефонную книгу
    '''
    return ch.add_contact(contact)


def find_contact_index(string):
    '''
    Поиск индекса контакта
    '''
    return ch.contact_search(string)


def delete_contact(index):
    '''
    Удаление контакта по инддексу
    '''
    return ch.del_contact(index)