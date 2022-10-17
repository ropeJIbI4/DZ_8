import cheat as ch
import UI as ui
import linecache as lin 
import logger as lg


def button_click():
    while True:
        ch.output_menu_console('telephone_menu_start.txt') 
        num_menu_1 = ui.get_menu_item(1) 
        lg.logging.info('Кожаный выбрал в telephone_menu_start: ' + str(num_menu_1))

        if num_menu_1 == 1:
            ch.output_list_contacts_console() 
            lg.logging.info('Вывод всех контактов Кожаного (telephone_contact.csv) в консоль')  
            input('Кожаный для продолжения работы нажми: "enter"')
            

        if num_menu_1 == 2:  
            '''
             Получения данных от пользователя и добавление в список

            '''
            list_contact = []  

            name = ui.get_name('Кожаный должен ввеcти имя: ')
            list_contact.append(name)
            patronymic = ui.get_name('Кожаный должен ввести отчество: ')
            list_contact.append(patronymic)
            surname = ui.get_name('Кожаный должен ввести фамилию: ')
            list_contact.append(surname)
            ch.output_menu_console('telephone_type.txt')  
            num_menu_2 = ui.get_menu_item(2)  
            num_menu_2 = ui.convert_type(num_menu_2)  
            list_contact.append(num_menu_2)
            num_tel = ui.get_number('Кожаный должен ввести номер телефона: ')
            list_contact.append(num_tel)
            comment = ui.get_name('Кожаный должен ввести комментарий: ')
            list_contact.append(comment)
            
            ui.add_contact(list_contact)  
            lg.logging.info('Добавлен контакт Кожаного в telephone_contact.csv: ' + str(list_contact))


        if num_menu_1 == 3: 
            find_name = ui.get_name('Кожаный введи поисковое слово (например имя контакта): ')
            contact_index = ui.find_contact_index(find_name)
            if contact_index == None:  
                input('Кожаный для продолжения работы нажми: "enter"')
                continue
            elif contact_index >= 0:  
                print(lin.getline('telephone_contacts.csv', contact_index + 1))  
                input('Кожаный для продолжения работы нажми: "enter"')
            lg.logging.info('Кожаный искал контакт: ' + str(find_name))

        if num_menu_1 == 4:  
            find_name = ui.get_name('Кожаный введи поисковое слово (имя контакта): ')
            contact_index = ui.find_contact_index(find_name)  
            if contact_index == None:  
                input('Кожаный для продолжения работы нажми: "enter"')
                continue
            elif contact_index >= 0: 
                ch.output_menu_console('telephone_delete_contact.txt')  
                print(lin.getline('telephone_contacts.csv', contact_index + 1)) 
                num_menu_3 = ui.get_menu_item(3)
                lg.logging.info('Кожаный выбрал в telephone_delete_contact: ' + str(num_menu_3))
                if num_menu_3 == 2: 
                    ui.delete_contact(contact_index)
                    print('Контакт Кожаного удалён!')
                    lg.logging.info('Кожаный удалил контакт с индексом: ' + str(contact_index))
                    input('Кожаный для продолжения работы нажми: "enter"')
                elif num_menu_3 == 1:  
                    print('Кожаный-Удаление отменено!')
                    input('Кожаный для продолжения работы нажми: "enter"')

        if num_menu_1 == 5:  
            lg.logging.info('Кожаный вышел из программы-Пока кожанный!)')
            return False 