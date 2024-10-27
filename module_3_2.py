def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if ("@" not in recipient or "@" not in sender or not any(sender.endswith(ext) for ext in ['.com', '.ru', '.net'])
            or not any(recipient.endswith(ext) for ext in ['.com', '.ru', '.net'])):
    #if all(substr not in recipient for substr in ext):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender==recipient:
        print(f"Нельзя отправить письмо самому себе! {sender} на адрес {recipient}")
        return
    if sender=='university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
    return recipient, sender
send_email('привет','yulalosk@rambler.ru')
send_email('привет','university.help@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.kz', sender='urban.teacher@mail.ru')