import time
import random


def choose_pivot_index(arr, low, high, strategy):
    '''Return pivot index between low and high based on strategy.'''
    if strategy == "First Element":
        return low
    elif strategy == "Last Element":
        return high
    elif strategy == "Median Element":
        mid = (low + high) // 2
        candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        candidates.sort(key=lambda x: x[0])
        return candidates[1][1]
    elif strategy == "Random":
        return random.randint(low, high)
    return low


def quicksort_with_steps(arr, strategy="First Element"):
    """
    Performs in-place quicksort on arr, logging each swap and partition step.
    Returns (sorted_array, steps, elapsed_time).
    """
    steps = []
    start_time = time.time()

    # Record initial state
    steps.append(arr.copy())

    def partition(low, high):
        pivot_idx = choose_pivot_index(arr, low, high, strategy)
        # Move pivot to end
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        steps.append(arr.copy())
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(arr.copy())
                i += 1
        # Place pivot in its final spot
        arr[i], arr[high] = arr[high], arr[i]
        steps.append(arr.copy())
        return i

    def quicksort_rec(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_rec(low, pi - 1)
            quicksort_rec(pi + 1, high)

    quicksort_rec(0, len(arr) - 1)
    elapsed_time = time.time() - start_time
    return arr, steps, elapsed_time

