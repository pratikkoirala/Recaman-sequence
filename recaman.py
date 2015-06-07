def Recaman(n):
    output = 0
    counter = 1
    result = []
    while output != n:
        result.append(output)
        if (output - counter) > 0 and (output - counter) not in result:
            output = output - counter
        else:
            output = output + counter
        counter += 1
    result.append(n)
    return result
    
    
