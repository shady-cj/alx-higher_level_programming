#!/usr/bin/python3
"""
Contains a function thats finds a peak in a
list of unsorted integers
"""


def findPeakRecursive(nums, lo, hi):
    """
    Using recursion to effectively search
    for the peak element using the divide and
    conquer algorithm
    """
    mid = (lo + hi) // 2
    left = mid - 1
    right = mid + 1
    if left < 0 and nums[mid] >= nums[right]:
        return mid
    elif right >= len(nums) and nums[mid] >= nums[left]:
        return mid
    elif nums[mid] >= nums[left] and nums[mid] >= nums[right]:
        return mid

    if lo == hi:
        return None
    searchLeft = findPeakRecursive(nums, lo, mid)
    searchRight = findPeakRecursive(nums, mid + 1, hi)
    if searchLeft is None:
        return searchRight
    else:
        return searchLeft


def find_peak(list_of_integers):
    """
    Implementing the find_peak function
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    index = findPeakRecursive(list_of_integers, 0, len(list_of_integers) - 1)
    if index is not None:
        return list_of_integers[index]
    return None
