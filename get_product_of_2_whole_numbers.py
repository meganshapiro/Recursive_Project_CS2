def get_product_of_2_whole_numbers(a, b):
    '''
    Get the product of two whole numbers
    Arguments:
        a: the first number
        b: the second number
    Returns:
        The product of a and b
    '''

    if a < b:  # if a is less than b switch the numbers
        return get_product_of_2_whole_numbers(b, a)


    elif b != 0:  # calculate b, times sum of a
        return (a + get_product_of_2_whole_numbers(a, b - 1))

    else:  # if a number is 0 return 0
        return 0


def main():
    a = 4
    b = 3
    print(get_product_of_2_whole_numbers(a, b))


if __name__ == '__main__':
    main()

