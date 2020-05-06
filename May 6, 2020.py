#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#You may assume that the array is non-empty and the majority element always exist in the array.
#Example:
#Input: [3,2,3], Output: 3
#Input: [2,2,1,1,1,2,2], Output: 2

class Solution:
    def majorityElement(self, nums: List[int])->int:
        majority = len(nums)/2
        nums_counter = Counter(nums)
        for key in nums_counter:
            if nums_counter[key] > majority: return key
