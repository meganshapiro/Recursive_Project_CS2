def get_fibonacci(n):
    '''
    Arguments: 
        n: number value taken from main and changed in function
        get_fibonacci: recalls function from within the function
    Takes:
        number variable from main
    Returns:
        sends edited product back to main
    '''
    if n == 0:
        return 0
            
    if n == 1:
        return 1
    
    else:
        return get_fibonacci(n-1)+get_fibonacci(n-2)