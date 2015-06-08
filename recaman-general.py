def Recaman(m,N):       #Outputs Recaman's sequence starting a(0) = m.
    output = m
    result = [m]
    for x in xrange(1, N + 1):
        if (output - x) > 0 and (output - x) not in result:
            output = output - x
        else:
            output = output + x
        result.append(output)            
    return result
