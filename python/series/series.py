def slices(series, length):
    if len(series) < length:
        raise ValueError("Length is greater than series length")

    if length <= 0:
        raise ValueError("Length cannot be zero or negative")

    if len(series) == 0:
        raise ValueError("Series cannot be empty")
    
    result = list()
    
    times = len(series) + 1 - length

    for i in range(times):
        e = i + length
        r = series[i:e]
        result.append(r)
    
    return result
