def send_email (message, recipient, sender = "university.help@gmail.com"):
    # if ("@" in recipient and (check_end( recipient, ".com") or
    #                          check_end( recipient,  ".ru") or
    #                          check_end( recipient, ".net")) and
    #                          (check_end( sender, ".com") or
    #                          check_end( sender, ".ru") or
    #                          check_end( sender, ".net"))) :
    if ("@" in recipient and check_end_2(recipient) and
                         check_end_2(sender)):
        if recipient == sender:
            print_ = (f'Нельзя отправить письмо самому себе')
        elif sender != "university.help@gmail.com":
            print_ = (f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса '
                       f'{sender} на адрес {recipient}.')
        else:
            print_ = (f'Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print_ = (f'Невозможно отправить c адреса {sender} на адрес {recipient}')
    return print(print_)
# def check_end(check_mail,  str_):
#     res = False
#     if check_mail.endswith(str_):
#         res = True
#         return res
def check_end_2(check_mail_2):
    res = False
    list_ =['.com', '.ru', '.net']
    for i in list_:
        if check_mail_2.endswith(i):
            res = True
            break
    return res

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
