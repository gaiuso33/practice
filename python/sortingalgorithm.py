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


# Test the hybrid Quick Sort
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5, 4, 2, 3, 6]
    hybrid_quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
