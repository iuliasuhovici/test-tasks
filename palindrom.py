'''
def is_palindrom(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

print(is_palindrom('racecar'))
print(is_palindrom('hello'))
'''
'''
def reverse(array):
    array = array[::-1]
    return array

print(reverse([1,2,3,4,5]))'
'''

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort([2,6,3,8,1,0]))