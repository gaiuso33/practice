import time
import random
import matplotlib.pyplot as plt

# Hybrid Quick Sort with Insertion Sort
def insertion_sort(arr, low, high):
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
        insertion_sort(arr, low, high)
    elif low < high:
        pivot_index = partition(arr, low, high)
        hybrid_quick_sort(arr, low, pivot_index - 1, threshold)
        hybrid_quick_sort(arr, pivot_index + 1, high, threshold)


# Standard Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Measure runtime of sorting algorithms
def measure_runtime(algorithms, input_sizes, threshold=10):
    runtimes = {algo.__name__: [] for algo in algorithms}

    for size in input_sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        for algo in algorithms:
            temp_arr = arr.copy()
            start_time = time.time()
            if algo.__name__ == "hybrid_quick_sort":
                algo(temp_arr, 0, len(temp_arr) - 1, threshold=threshold)
            elif algo.__name__ == "quick_sort":  # Quick Sort returns a new list
                algo(temp_arr)
            else:
                algo(temp_arr)
            end_time = time.time()
            runtimes[algo.__name__].append(end_time - start_time)

    return runtimes


# Plot runtimes
def plot_runtimes(runtimes, input_sizes):
    plt.figure(figsize=(10, 6))
    for algo, times in runtimes.items():
        plt.plot(input_sizes, times, label=algo)

    plt.title("Runtime vs Sorting Algorithm")
    plt.xlabel("Input Size")
    plt.ylabel("Runtime (seconds)")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    # Sorting algorithms to compare
    algorithms = [hybrid_quick_sort, quick_sort, merge_sort]

    # Input sizes
    input_sizes = [100, 500, 1000, 2000, 5000, 10000]

    # Measure runtimes with a threshold of 10 for Hybrid Quick Sort
    runtimes = measure_runtime(algorithms, input_sizes, threshold=10)

    # Plot runtimes
    plot_runtimes(runtimes, input_sizes)
