import random
import time
import matplotlib.pyplot as plt

# Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate random array and measure runtime
def measure_runtime(data_sizes, sorting_function):
    runtimes = []
    for size in data_sizes:
        # Generate random data
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        # Measure sorting time
        start_time = time.time()
        sorting_function(arr)
        end_time = time.time()
        
        runtimes.append(end_time - start_time)
    return runtimes

# Main program
data_sizes = [1000, 5000, 10000, 15000, 20000]
sorting_algorithms = [bubble_sort, selection_sort, insertion_sort]
sorting_names = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']

# Measure runtimes for each sorting algorithm
all_runtimes = {}
for sort_name, sort_func in zip(sorting_names, sorting_algorithms):
    all_runtimes[sort_name] = measure_runtime(data_sizes, sort_func)

# Plot the results
plt.figure(figsize=(12, 8))
for sort_name, runtimes in all_runtimes.items():
    plt.plot(data_sizes, runtimes, marker='o', label=sort_name)

plt.title('Sorting Algorithm Runtimes')
plt.xlabel('Data Size')
plt.ylabel('Runtime (seconds)')
plt.legend()
plt.grid(True)
plt.show()
