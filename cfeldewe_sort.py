"""
Name: Caitlin Feldewerth
Class: CPE 202-05
Assignment: Lab 6, Selection Sort and Quick Sort
"""
def SelectionSort(lst):
    c = 0
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
            c += 1
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    print(c)

c = 0
def QuickSort(lst):
    if len(lst) <= 1:
        return lst
    pivot_idx = len(lst) // 2
    smaller, larger = [], []
    for idx, num in enumerate(lst):
        if idx != pivot_idx:
            global c
            c += 1
            (larger, smaller)[num < lst[pivot_idx]].append(num)
    return QuickSort(smaller) + [lst[pivot_idx]] + QuickSort(larger)

import random
random.seed(1)
lst_one = random.sample(range(2000), 1000)
lst_two = random.sample(range(4000), 2000)
lst_three = random.sample(range(8000), 4000)
lst_four = random.sample(range(16000), 8000)
lst_five = random.sample(range(32000), 16000)
lst_six = random.sample(range(64000), 32000)
lst_seven = random.sample(range(200000), 100000)
lst_eight = random.sample(range(1000000), 500000)

lst_nine = [x for x in range(1000)]
lst_ten = [x for x in range(2000)]
lst_eleven = [x for x in range(4000)]
lst_twelve = [x for x in range(8000)]
lst_thirteen = [x for x in range(16000)]
lst_fourteen = [x for x in range(32000)]
lst_fifteen = [x for x in range(100000)]
lst_sixteen = [x for x in range(500000)]

import time
start_time = time.time()
#call function here
QuickSort(lst_two)
end_time = time.time()
sort_time = end_time - start_time
#only print c when calling QuickSort
print(c)
print(sort_time)
