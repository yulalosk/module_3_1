def print_params(a = 1, b = 'How do you do', c = True):

    print(a,b,c)

value_list=[[17,20], "Yuliya", 44]
values_dict={'a': 96002730390, 'b': 9600278881, 'c': 9062901967  }
print_params(*value_list)
print_params(*values_dict)
print_params(**values_dict)


def print_params4(a,b,c): # так распакованные?
    print(a,b,c)

values_list = [[47, 23], 'Конкатенация']
print_params4(*values_list, 42)

