
def get_int(base, max):
    x = base
    while x < max:
        x = x + 1
        x2 = x * 2
        x3 = x * 3
        x4 = x * 4
        x5 = x * 5
        x6 = x * 6

        x_sort = sorted(str(x))
        x2_sort = sorted(str(x2))
        x3_sort = sorted(str(x3))
        x4_sort = sorted(str(x4))
        x5_sort = sorted(str(x5))
        x6_sort = sorted(str(x6))

        if x_sort == x2_sort and x_sort == x3_sort and x_sort == x4_sort and x_sort == x5_sort and x_sort == x6_sort:
            return (x, x2, x3, x4, x5, x6)

    return 'no matching numbers'

    #check first digit of x in multiples. first digit of x will always be 1.



print(get_int(1000, 16666667))


# x = 51
# b = '15'
# x_sort = sorted(str(x))
# b_sort = sorted(b)
# print(x, b, x_sort, b_sort)
# if x_sort == b_sort:
#     print('they match!')