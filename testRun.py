import time, tracemalloc
import dataGenerator, bciSort, countingSort

def testRun(dataset):
    print("--------------------------------------")

    for key in dataset:
        data = dataset.get(key)
        name = key.split("_")
        print(" ".join(name).upper() + " DATASET\n")

        start_bcis = time.time()
        bciSort.bciSort(data)
        end_bcis = time.time()

        tracemalloc.start()
        bciSort.bciSort(data)
        mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print("BCIS Time: %.2f ms" % ((end_bcis - start_bcis) * 1000))
        print("Peak BCIS Memory: %.2f bytes" % (mem[1]))
        print()

        start_cs = time.time()
        countingSort.countingSort(data)
        end_cs = time.time()

        tracemalloc.start()
        countingSort.countingSort(data)
        mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print("CS Time: %.2f ms" % ((end_cs - start_cs) * 1000))
        print("Peak CS Memory: %.2f bytes" % (mem[1]))

        print("--------------------------------------")

dataset = dataGenerator.generateDataset()
testRun(dataset)
