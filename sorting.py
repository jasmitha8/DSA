def BubbleSort(nums):
    """
    T: O(n^2)
    S: O(1)

    Bubble up the highest value
    """
    n = len(nums)
    for i in range(n):  # 0, 1, 2, 3, 4
        noSwap = True
        for j in range(n-i-1):  # i=0 -> [0,1,2,3], i=1 -> [0,1,2], i=2 -> [0,1], i=3 -> [0]
            # Swapping the biggest number all the way up
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                noSwap = False
        if noSwap:
            break       # The array is already sorted and doesn't need any more swaps
    return nums
        

def SelectionSort(nums):
    """
    T: O(n^2)
    S: O(1)
    
    Select the minimum index in the remaining array and substitute
    """
    for i in range(len(nums)):
        # Loop to get the minimum most value
        minIdx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minIdx]:
                minIdx = j
    
        # Replace the ith value with lowest value found in nums
        nums[i], nums[minIdx] = nums[minIdx], nums[i]
    return nums


def InsertionSort(nums):
    """
    T: Best-case O(n) when nums is already sorted
        Average or worst-case O(n^2) if the list is random order or reverse order respectively
    S: O(1)

    Insert a number bigger than key one index above
    """
    for i in range(1, len(nums)):
        key, j = nums[i], i-1
        
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        
        # While loop exited because key is the biggest value
        nums[j+1] = key
    return nums


def MergeSort(nums):
    """
    T: O(nlogn)
    S: O(n)

    Merge the single split arrays
    """
    def merge(left, right):
        l, r = 0, 0
        result = []

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        
        # Appending the remaining left and right arrays
        result.extend(left[l:])
        result.extend(right[r:])
        return result

    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    sortedLeft = MergeSort(left)
    sortedRight = MergeSort(right)

    return merge(sortedLeft, sortedRight)


def QuickSort(nums, low, high):
    """
    T: O(nlogn)
    S: O(n)

    Quick sort = pivot
    """
    def getPivot(subNums, l, h):
        pivot = subNums[h]
        i = l - 1   # To hold index of the next smallest element after pivot

        for j in range(l, h):
            if nums[j] < pivot:
                i += 1      # Update the index of the next smallest element to hold the new minimum value
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]   # Swapping the pivot with arr[i+1] since i has the next smallest element for pivot

        return i + 1    # Updated index of pivot

    if low < high:
        pivotIdx = getPivot(nums, low, high)
        QuickSort(nums, low, pivotIdx - 1)
        QuickSort(nums, pivotIdx + 1, high)

        return nums


def HeapSort(nums):
    """
    T: O(nlogn)
    S: O(logn)

    Builds a max heap and sends the root to the end of the array
    """
    def heapify(arr, n, i):
        """
        Return max heap
        """
        largest = i
        l = 2*i + 1     # left child
        r = 2*i + 2     # right child

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        
        if largest != i:    # If largest is not root
            arr[largest], arr[i] = arr[i], arr[largest]
            heapify(arr, n, largest)
    
    # Build a max heap
    for i in range(len(nums)//2, -1, -1):
        heapify(nums, len(nums), i)

    # The 0th index of the array contains the biggest number
    for i in range(len(nums)-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]     # Send the root to the end of the array because max
        heapify(nums, i, 0)     # Heapify the remaining array

    return nums


def OtherSort():
    print("Bucket Sort")
    print("Radix sort")


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22]
    print(BubbleSort(arr))
    print(SelectionSort(arr))
    print(InsertionSort(arr))
    print(MergeSort(arr))
    print(QuickSort(arr, 0, 4))
    print(HeapSort(arr))
    print(OtherSort())
