def fib_2(n):
    '''
    This calculates the nth Fibonacci number.
    '''
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib_2(n - 1) + fib_2(n - 2)