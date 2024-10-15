import time
import tracemalloc
import numpy as np

# tracemalloc.start()
array1 = np.arange(10_000_000, dtype=np.int64)
array2 = np.arange(10_000_000, dtype=np.int64)
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB;")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
# Current memory usage: 76.29412841796875 MB;
# Peak memory usage: 76.29412841796875 MB;
# pip install numpy

# tracemalloc.start()
list1 = list(range(10_000_000))
list2 = list(range(10_000_000))


# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB;")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
# Current memory usage: 762.9238739013672 MB;
# Peak memory usage: 762.9239807128906 MB;

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")

        return result

    return wrapper


@measure_time
def add_without_np():
    tracemalloc.start()
    res = [list1[i] + list2[i] for i in range(len(list1))]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Current memory usage: {current / 1024 ** 2} MB;")
    print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
    return "OK"


@measure_time
def add_np():
    tracemalloc.start()
    res = array1 + array2
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Current memory usage: {current / 1024 ** 2} MB;")
    print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
    return "OK np"


print("Start")
print(add_without_np())
print(add_np())
# Start
# Czas wykonania funkcji add_without_np: 1.0466163158416748
# OK
# Czas wykonania funkcji add_np: 0.019059419631958008
# OK np
# Current memory usage: 152.58807373046875 MB;
# Peak memory usage: 152.58807373046875 MB;
# Current memory usage: 762.9238739013672 MB;
# Peak memory usage: 762.9239807128906 MB;
# Start
# Current memory usage: 390.1395568847656 MB;
# Peak memory usage: 390.1396179199219 MB;
# Czas wykonania funkcji add_without_np: 13.424648761749268
# OK
# Czas wykonania funkcji add_np: 0.03201937675476074
# OK np
#
# Process finished with exit code 0
