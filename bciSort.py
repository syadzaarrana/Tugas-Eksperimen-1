import math

def bciSort(a):
    sl = 0
    sr = len(a) - 1
    left, right = sl, sr

    while sl < sr:
        mid = (sr - sl) // 2
        swap(a, sr, sl + mid)

        if a[sl] == a[sr]:
            if isAllEqual(a, sl, sr) == -1:
                return
        
        if a[sl] > a[sr]:
            swap(a, sl, sr)
        
        if (sr - sl) >= 100:
            for i in range(sl + 1, (math.floor((sr - sl) ** 0.5))):
                if a[sr] < a[i]:
                    swap(a, sr, i)
                elif a[sl] > a[i]:
                    swap(a, sl, i)
        
        x = sl + 1
        
        lc = a[sl]
        rc = a[sr]

        while x < sr:
            current = a[x]
            if current >= rc:
                a[x] = a[sr - 1]
                insertRight(a, current, sr, right)
                sr -= 1
            elif current <= lc:
                a[x] = a[sl + 1]
                insertLeft(a, current, sl, left)
                sl += 1
                x += 1
            else:
                x += 1
            
        sl += 1
        sr -= 1
    return a

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def isAllEqual(a, sl, sr):
    for i in range(sl + 1, sr):
        if a[i] != a[sl]:
            swap(a, i, sl)
            return i
    return -1

def insertLeft(a, current, sl, left):
    j = sl
    while j >= left and current < a[j]:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = current

def insertRight(a, current, sr, right):
    j = sr
    while j <= right and current > a[j]:
        a[j - 1] = a[j]
        j += 1
    a[j - 1] = current
