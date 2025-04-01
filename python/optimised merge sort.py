import random
import time
import matplotlib.pyplot as plt

# Optimized Merge Sort Implementation
def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, temp, low, mid, high):
    i, j, k = low, mid + 1, low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(low, high + 1):
        arr[i] = temp[i]

def merge_sort_optimized(arr, temp, low, high, threshold=10):
    if high - low < threshold:
        insertion_sort(arr, low, high)
    elif low < high:
        mid = (low + high) // 2
        merge_sort_optimized(arr, temp, low, mid, threshold)
        merge_sort_optimized(arr, temp, mid + 1, high, threshold)
        merge(arr, temp, low, mid, high)

def hybrid_merge_sort(arr):
    temp = [0] * len(arr)
    merge_sort_optimized(arr, temp, 0, len(arr) - 1, threshold=10)

# Hybrid Quick Sort (Quick Sort + Insertion Sort)
def insertion_sort_quick(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def hybrid_quick_sort(arr, low, high, threshold=10):
    if high - low < threshold:
        insertion_sort_quick(arr, low, high)
    elif low < high:
        pi = partition(arr, low, high)
        hybrid_quick_sort(arr, low, pi - 1, threshold)
        hybrid_quick_sort(arr, pi + 1, high, threshold)

# Benchmarking and Plotting
def measure_runtime(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    return time.time() - start_time

if __name__ == "__main__":
    # Algorithms to test
    algorithms = {
        "Hybrid Merge Sort": hybrid_merge_sort,
        "Hybrid Quick Sort": lambda arr: hybrid_quick_sort(arr, 0, len(arr) - 1, threshold=10),
    }

    # Data sizes
    input_sizes = [1000, 5000, 10000, 15000, 20000]
    results = {name: [] for name in algorithms}

    # Benchmark each algorithm
    for size in input_sizes:
        print(f"Testing size: {size}")
        test_array = [random.randint(1, 1000) for _ in range(size)]
        for name, algo in algorithms.items():
            runtime = measure_runtime(algo, test_array.copy())
            results[name].append(runtime)

    # Plot results
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(input_sizes, times, label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime vs Input Size for Sorting Algorithms")
    plt.legend()
    plt.grid()
    plt.show()
