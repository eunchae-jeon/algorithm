def practice():
    arr = [4, 5, 2, 6, 7, 1, 0]
    # print(bubble_sort(arr))
    # print(selection_sort(arr))
    # print(insert_sort(arr))
    # print(shell_sort(arr))
    # print(quick_sort(arr))
    # print(heap_sort(arr))
    print(merge_sort(arr))
    pass

def bubble_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        min_i = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

def insert_sort(arr):
    arr = arr[:]
    for i in range(len(arr)-1):
        for j in range(i+1, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

def shell_sort(arr):
    arr = arr[:]
    interval = len(arr)//2
    while interval >= 1:
        for i in range(len(arr)):
            interval_sort(arr, i, interval)
        interval //= 2
    return arr

def interval_sort(arr, begin, interval):
    position = begin
    key = arr[position]
    while position - interval >= 0 and arr[position-interval] > key:
        arr[position] = arr[position-interval]
        position -= interval
    arr[position] = key

def quick_sort(arr):
    arr = arr[:]
    quick(arr, 0, len(arr)-1)
    return arr

def quick(arr, begin, end):
    left, right = begin, end
    mid = (left + right) // 2
    pivot = arr[mid]
    while left <= right:
        while arr[left] < pivot:#무한루프인 경우 없음
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    if begin < right:
        quick(arr, begin, right)
    if left < end:
        quick(arr, left, end)
        
def heap_sort(arr):
    arr = arr[:]
    #heapify
    for i in range(len(arr)//2-1, -1, -1):
        heapify(arr, i, len(arr))
    for i in range(len(arr)-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

def heapify(arr, i, n):
    mx = i
    l, r = i*2+1, i*2+2
    if i*2+1 >= n:
        return
    if i*2+1 < n:
        if arr[l] > arr[mx]:
            mx = l
    if i*2+2 < n:
        if arr[r] > arr[mx]:
            mx = r
    if mx != i:
        arr[i], arr[mx] = arr[mx], arr[i]
        heapify(arr, mx, n)
    return

def merge_sort(arr):
    arr = arr[:]
    merge(arr, 0, len(arr)-1)
    return arr

def merge(arr, begin, end):
    if begin >= end: return
    mid = (begin + end) // 2
    
    merge(arr, begin, mid)
    merge(arr, mid+1, end)
    
    left = begin
    right = mid+1
    merged = []
    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            merged.append(arr[left])
            left += 1
        else:
            merged.append(arr[right])
            right += 1
    if left > mid:
        merged.extend(arr[right:end+1])
    else:
        merged.extend(arr[left:mid+1])
    
    for i in range(len(merged)):
        arr[begin+i] = merged[i]




if __name__ == "__main__":
    practice()
