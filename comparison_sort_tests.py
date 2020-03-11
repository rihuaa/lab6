"""
Test Cases for insertion and merge sort.
Generates random list to calculate algorithm runtime.

Author: Richard Hua
Section: CPE202-05
Quarter: Winter 2020

"""

import unittest
import time
import random

import comparison_sort
from comparison_sort import insertion_sort, merge_sort

""" Generating list of random numbers.
Produces a list of 10 random #'s between 1 and 10000
"""
N = 1000
random.seed(1) #generates same seq of #'s each time
alist = random.sample(range(10000000), N)
print("N: ", N)

""" Calculates the time algorithm takes to sort list.
"""
# ====== Insertion Sort =======
# Unsorted list
start_time = time.time()
slist, comps = insertion_sort(alist)
end_time = time.time()
sort_time = end_time - start_time
print("Insertion Sort -- Comps: %d" % comps)
print("Unsorted Sort Time : %f" % sort_time)
# Sorted List
start_time = time.time()
slist, comps = insertion_sort(slist)
end_time = time.time()
sort_time = end_time - start_time
print("Insertion Sort -- Comps: %d" % comps)
print("Sorted Sort Time : %f" % sort_time)

# # Sorted List
# slist = [None] * 16000
# for i in range(16000):
#     slist[i] = i
# start_time = time.time()
# slist, comps = insertion_sort(slist)
# end_time = time.time()
# sort_time = end_time - start_time
# print("Insertion Sort -- Comps: %d" % comps)
# print("Sorted Sort Time : %f" % sort_time)


# ====== Merge Sort =======
alist = random.sample(range(10000000), N)
# Unsorted list
start_time = time.time()
slist, comps = merge_sort(alist)
end_time = time.time()
sort_time = end_time - start_time
print("Merge Sort -- Comps: %d" % comps)
print("Unsorted Sort Time : %f" % sort_time)
# Sorted List
start_time = time.time()
slist, comps = merge_sort(slist)
end_time = time.time()
sort_time = end_time - start_time
print("Merge Sort -- Comps: %d" % comps)
print("Sorted Sort Time : %f" % sort_time)


# ====== Built in Python sort() using Timsort =======
alist = random.sample(range(10000000), N)
# Unsorted list
start_time = time.time()
alist.sort()
end_time = time.time()
sort_time = end_time - start_time
print("Unsorted TimSort Time : %f" % sort_time)
# Sorted List
start_time = time.time()
alist.sort()
end_time = time.time()
sort_time = end_time - start_time
print("Sorted TimSort Time : %f" % sort_time)


if __name__ == '__main__':
    unittest.main()
