def countingSort(a):
    n = len(a)
    k = max(a)
    
    b = [0] * n
    c = [0] * (k + 1)

    for i in range(0, n):
        c[a[i]] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    for j in range(n - 1, -1, -1):
        b[c[a[j]] - 1] = a[j]
        c[a[j]] -= 1
    
    return b
