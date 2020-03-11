"""
CPE202
Riley C. Smith
Lab 6
"""
import time
import random

def bubble_sort(alist):
    """Sorts a list of integers using bubble sort and returns the number of comparisons made
    Args:
        alist (lst): list of integers
    Returns:
        int: the number of comparisons made by the sorting algorithm
    Author:
        Riley Smith
    """
    comp = 0
    for i in alist:
        for j in range(len(alist) - 1):
            comp += 1
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    return comp

def bubble_sort2(alist):
    """Sorts a list of integers using bubble sort and returns the number of comparisons made. This
        bubble sort will stop when a pass finishes with no swaps.
    Args:
        alist (lst): list of integers
    Returns:
        int: the number of comparisons made by the sorting algorithm
    Author:
        Riley Smith
    """
    swap_count = 0
    comp = 0
    for i in alist:
        for j in range(len(alist) - 1):
            comp += 1
            if alist[j] > alist[j+1]:
                swap_count += 1
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
        if swap_count == 0:
            return comp
        swap_count = 0
    return comp

def heap_sort(alist):
    """Sorts a list of integers using heapify + heap sort and returns the number of comparisons made
    Args:
        alist (lst): list of integers
    Returns:
        int: the total number of comparisons made throughout the heap sort algorithim
    Author:
        Riley Smith
    """
    end = len(alist) - 1
    comp = 0
    for i in range(len(alist)):  # from 0 to len(lst)
        comp = heapify(alist, len(alist), len(alist) - i - 1, comp)
        alist[0], alist[end] = alist[end], alist[0]
        end -= 1
    return comp

def heapify(alist, length, index, comp):
    """Sorts a list into a max heap
    Args:
        alist (lst): list of integers to be heapified
        length (int): length of the list of integers
        index (int): index of the subtree to be heapified
        comp (comp): total number of comparisons in the function
    Returns:
        int: the number of comparisons made within the recursive heapify pass
    Author:
        Riley Smith
    """
    left_ind = 2 * index + 1
    right_ind = 2 * index + 2
    biggest = index
    if left_ind < length:
        comp += 1
        if alist[left_ind] > alist[index]:
            biggest = left_ind
    if right_ind < length:
        comp += 1
        if alist[right_ind] > alist[left_ind]:
            biggest = right_ind
    if index != biggest:
        alist[index], alist[biggest] = alist[biggest], alist[index]
        comp = heapify(alist, length, biggest, 0) + comp
        return comp + 1
    return comp + 3
