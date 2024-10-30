# def summa(n):
#     if n==0:
#         return 0
#     else:
#         return n + summa(n-1)
#
# print(summa(6))

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return(first * get_multiplied_digits(int(str_number[1:])))
    else:
        return first
print(get_multiplied_digits(40203))



