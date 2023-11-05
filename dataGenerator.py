import random

def generateDataset():
    dataset = {}
    dataset['sorted_small'] = sortedData(500)
    dataset['reversed_small'] = reversedData(500)
    dataset['random_small'] = randomData(500)

    dataset['sorted_medium'] = sortedData(5000)
    dataset['reversed_medium'] = reversedData(5000)
    dataset['random_medium'] = randomData(5000)

    dataset['sorted_large'] = sortedData(50000)
    dataset['reversed_large'] = reversedData(50000)
    dataset['random_large'] = randomData(50000)

    return dataset


def randomData(n):
    res = []
    for i in range(0, n):
        res.append(random.randint(0, 100000))
    return res

def sortedData(n):
    return randomData(n).sort()

def reversedData(n):
    return randomData(n).sort(reverse=True)
