def fibonacci(n):
    """
        FIBONACCI FUNCTION

        RETURN
            list of n fibonacci numbers

        ARGUMENTS
            
           n --> how many fibonacci numbers 
    """

    controller = 0
    returnable = []
    
    while controller < n:
        if controller < 2:
            returnable.append(1)
        else:
            returnable.append(returnable[-1] + returnable[-2])
        controller += 1

    return returnable