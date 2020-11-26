def fibonacci(n):
    controller = 0
    returnable = []
    
    while controller < n:
        if controller < 2:
            returnable.append(1)
        else:
            returnable.append(returnable[-1] + returnable[-2])
        controller += 1

    return returnable