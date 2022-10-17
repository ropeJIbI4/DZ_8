def check_M(string, n) -> int:
    '''
     Выбор пункта меню.
    
    '''
    try:
        num = int(input(string))
        if n == 1:
            if num < 1 or num > 5:
                print('Некорректный ввод!')
                return check_M(string, n)
        elif n == 2:
            if num < 1 or num > 6:
                print('Некорректный ввод!')
                return check_M(string, n) 
        elif n == 3:
            if num < 1 or num > 2:
                print('Некорректный ввод!')
                return check_M(string, n) 
        return num
    except ValueError:
        print('Некорректный ввод!')
        return check_M(string, n)


def check_NC(string):
    '''
      Ввод имени. 
        
    '''
    name = input(string)

    if len(name) > 15:
        print('Недопустимое количество символов!')
        return check_NC(string)
    elif len(name) == 0:
        print('Вы ввели пустую строку!')
        return check_NC(string)
    elif name.isalpha(): return name.title() 
    else: 
        print('Некорректный ввод!')
        return check_NC(string) 


def check_NT(string):
    '''
     Ввод номера телефона.
      
    '''
    try:
        num_N = input(string)
        if len(num_N) > 11 or len(num_N) < 5: 
            print('Некорректный ввод!')
            return check_NT(string)
        num_tel = int(num_N)
        return(num_tel)
    except ValueError:
        print('Некорректный ввод!')
        return check_NT(string)