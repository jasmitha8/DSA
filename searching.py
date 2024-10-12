from sorting import HeapSort


def linearSearch(nums, key):
    """
    T: O(n)
    """
    for idx, num in enumerate(nums):
        if num == key:
            return idx
    return -1

def binarySearch(nums, key):
    """
    T: O(logn)
    """
    # For binary search, the array has to be sorted
    nums = HeapSort(nums)

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            r = mid - 1
        else:
            l = mid + 1
    return -1


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22]
    print(linearSearch(arr, 25))
    print(binarySearch(arr, 25))
