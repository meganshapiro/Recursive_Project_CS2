def get_summation(n):
    '''
    Arguments: 
        n: number value taken from main and changed in function
        get_summation: recalls function from within the function
    Takes:
        number variable from main
    Returns:
        sends edited product back to main
    '''
    if n == 0:
        return 0
    
    else:
        return n+get_summation(n-1)

