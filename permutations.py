'''
import itertools

def permutations(arr):
    return list(itertools.permutations(arr))

print(permutations([1,2,3]))'
'''
'''
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return mid

print(binary_search([1,7,3,0,9], 9))
'''
'''
def quick_sort(arr):
    if len (arr) <= 1:
        return arr
    
    pivot = arr[len(arr)// 2]
    left = [x for x in arr if x < pivot ] #генератор списка
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot ] #генератор списка

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([6,2,8,4,0]))
'''

# Merge sort

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([6,2,7,4,9,0]))
