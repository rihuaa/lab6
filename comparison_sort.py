"""Contains code for insertion and merge sort.

CPE202

Instructions:
    Complete this file by writing python3 code.

"""


def insertion_sort(alist):
    """Takes a list of integers and performs insertion sort.

    Args:
        alist (list): a list of integers

    Returns:
        int: the number of comparisons performed in the sort
    """
    size = len(alist)
    comps = 0
    for i in range(1, size):
        j = i
        while j > 0 and alist[j - 1] > alist[j]:
            alist[j- 1], alist[j] = alist[j], alist[j - 1]
            j = j - 1
            comps += 1
        comps += 1
    return alist, comps

def merge_sort(alist, comps = 0):
    """sort a list of items in ascending order using the merge sort algorithm.
         Note:
         This version of the merge sort produce many copies of the list and
         therefore not very efficient in terms of the space complexity.
         Args:
            items (list) : a list of integers or strings
         Returns:
            list : a copy of the original list with items sorted in acending order.
    """
    if len(alist) <= 1:
        return alist, comps
    m = len(alist) // 2
    left, comps = merge_sort(alist[:m], comps)
    right, comps = merge_sort(alist[m:], comps)
    return merge(left, right, comps)

    # if the length of the items list <= 1, return the items list
    #     compute the midpoint
    #     left = merge_sort(items[:midpoint])
    #     right = merge_sort(items[midpoint:])
    #     return merge(left, right)

def merge(left, right, comps):
    """merge two list into one as sorting items in ascending order.

    Args:
        left (list) : the left part of a list to be merged
        right (list) : the right part of a list to be merged

    Returns:
        list : a merged and sorted list
    """
    merged = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        comps += 1
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    # if there are leftover in the left list:
    #     append all the leftover to the merged
    # if there are leftover in the right list:
    #     append all the leftover to the merged
    while left_idx < len(left):
        merged.append(left[left_idx])
        comps += 1
        left_idx += 1
    while right_idx < len(right):
        merged.append(right[right_idx])
        comps += 1
        right_idx += 1
    return merged, comps
