calls=0
def count_calls():
    global calls
    calls+=1
    return

def string_info(string):
    s=(len(string),string.upper(), string.lower())
    count_calls()
    return s

def is_contains(string, list_to_search):
    string=string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string in list_to_search:
        print(True)
    else:
        print('No matches')
    count_calls()
    return(string, list_to_search)

print(string_info('карамболь'))
print(string_info('абракадабра'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
#print(is_contains('cycle', ['recycling', 'cyclic']), {is_contains('cycle', ['recycling', 'cyclic'])}" )
print(f'Функции вызваны {calls} раз')
