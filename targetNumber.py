# 1 способ медленный
'''
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print (two_sum([2, 7, 9 , 11, 5], 9))
'''
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("hello","world"))
print(is_anagram("listen","silent"))