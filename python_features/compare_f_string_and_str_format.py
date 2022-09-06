'''Compares f-string and str format.'''


def compare_f_string_and_str_format(num=123.456, width=6, decimals=1, /):
    str_1 = f'{num = :6.1f}'
    print(str_1)
    str_2 = f'{num = :{width}.{decimals}f}'
    print(str_2)

    str_3 = 'num = {0:6.1f}'.format(num)
    print(str_3)
    str_4 = 'num = {0:{1}.{2}f}'.format(num, width, decimals)
    print(str_4)


compare_f_string_and_str_format()
print()
compare_f_string_and_str_format(1.6789, 3, 2)
