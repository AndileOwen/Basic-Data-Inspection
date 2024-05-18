def bubble_sort(data):
    
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
    return data

def insertion_sort(data):
    
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def heapify(data, n, i):
    
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child is larger than root
    if left < n and data[i] < data[left]:
        largest = left

    # See if right child is larger than largest so far
    if right < n and data[largest] < data[right]:
        largest = right

    # Swap and continue heapifying if root is not largest
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heap_sort(data):
    n = len(data)

    # Build a maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # Swap
        print(f"Iteration {n - i}: {data}")  # Display each iteration
        heapify(data, i, 0)

def binary_search(data, target):
    
    low = 0
    high = len(data) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Check if target is present at mid
        if data[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif data[mid] < target:
            low = mid + 1

        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, the target was not present
    return -1

def linear_search(data, target):
    
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Sample data (replace with your elements)
data = [10, 7, 26, 43, 3, 13, 11]

# Bubble Sort
print("Bubble Sort:", bubble_sort(data.copy()))  # Copy to avoid modifying original list

# Insertion Sort
print("Insertion Sort:", insertion_sort(data.copy()))

# Heap Sort (Visualization)
print("Heap Sort (Iterations):")
heap_sort(data.copy())

# Binary Search (replace target with your value)
target = 13
result = binary_search(data, target)
if result != -1:
    print("Binary Search: Element found at index", result)
else:
    print("Binary Search: Element not found")

# Linear Search (replace target with your value)
target = 22  # Add closing parenthesis here