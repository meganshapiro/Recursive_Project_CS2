def get_factorial(n):
    """
    Get the factorial of a number
    Arguments:
        n: the number
    Returns:
        The factorial of the number
    """

    if n == 0:
        return 1  # the factorial of 0 is 1
    else:
        return n * get_factorial(n - 1)  # find the factorial, ex: 5! = 5*4*3*2*1


def main():
    num = 5
    print(get_factorial(num))


if __name__ == '__main__':
    main()

