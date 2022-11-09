def get_sum_of_numbers_digits(n):
    """
    Add together a number's digits
    Arguments:
        n: the number
    Returns:
        sum: the sum of the number's digits
    """
    sum = 0
    for digit in str(n):  # for each digit of the number
        sum += int(digit)  # add together the digits
    return sum


def main():
    n = 12
    print(get_sum_of_numbers_digits(n))


if __name__ == '__main__':
    main()
