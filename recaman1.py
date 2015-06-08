def Recaman(N):         #Outputs Recaman's sequence with N+1 terms.
    output = 0
    result = [0]
    for x in xrange(1, N + 1):
        if (output - x) > 0 and (output - x) not in result:
            output = output - x
        else:
            output = output + x
        result.append(output)            
    return result
