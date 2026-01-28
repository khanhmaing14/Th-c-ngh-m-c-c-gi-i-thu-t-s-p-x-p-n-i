import numpy as np
import time
import sys
sys.setrecursionlimit(10**7)


N = 1000000  # số phần tử mỗi dãy
datasets = []

# 1 Dãy số thực tăng dần
arr1 = np.linspace(0.0, 1000000.0, N)
datasets.append(arr1)

# 2 Dãy số thực giảm dần
arr2 = arr1[::-1]
datasets.append(arr2)

# 3 dãy số thực ngẫu nhiên
for _ in range(3):
    arr = np.random.rand(N)*1000000    
    datasets.append(arr)

# 5 dãy số nguyên ngẫu nhiên
for _ in range(5):
    arr = np.random.randint(0, 1000000, size=N)
    datasets.append(arr)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = arr[arr < pivot]
    middle = arr[arr == pivot]
    right = arr[arr > pivot]
    return np.concatenate((quicksort(left), middle, quicksort(right)))

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return np.array(result)

def numpy_sort(arr):
    return np.sort(arr)

def measure_time(sort_func, arr):
    data = arr.copy()
    start = time.perf_counter()
    result = sort_func(data)
    end = time.perf_counter()
    return end - start

sort_algorithms = {
    "QuickSort": quicksort,
    "HeapSort": heapsort,
    "MergeSort": mergesort,
    "NumPy Sort": numpy_sort
}

for i, data in enumerate(datasets):
    print(f"\nDãy {i+1}:")
    for name, func in sort_algorithms.items():
        try:
            t = measure_time(func, data)
            print(f"{name}: {t:.2f} giây")
        except Exception as e:
            print(f"{name}: lỗi ({e})")

