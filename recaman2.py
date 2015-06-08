def Recaman(N):         //Returns recaman sequence starting with 0 and ending in N.
    output = 0
    counter = 1
    result = []
    while output != N:
        result.append(output)
        if (output - counter) > 0 and (output - counter) not in result:
            output = output - counter
        else:
            output = output + counter
        counter += 1
    result.append(N)
    return result
    
    
