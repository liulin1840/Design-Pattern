# -*- coding:utf-8 -*-
__author__ = 'liulin'

def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    print(lists)
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

data_list=[2,3,6,4,2,4,7]
quick_sort(data_list,0,len(data_list)-1)
print(data_list)