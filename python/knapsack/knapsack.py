def maximum_value(max_weight, items):
    W = max_weight
    n = len(items)
    w = [None]
    v = [None]
    w += [i['weight'] for i in items]
    v += [i['value'] for i in items]
    m = []
    m += [[0] * (W+1)]

    for i in range(1, n+1):
        m += [m[i-1][:]]
        for j in range(W+1):
            if w[i] <= j:
                m[i][j] = max(m[i-1][j], m[i-1][j-w[i]] + v[i])
    return m[n][W]