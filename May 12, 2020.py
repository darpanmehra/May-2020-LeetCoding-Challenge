#Single Element in a Sorted Array
#You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
#Examples:
#Input: [1,1,2,3,3,4,4,8,8], Output: 2
#Input: [3,3,7,7,10,11,11], Output: 10

class Solution:
    def singleNonDuplicate(self, nums: List[int])->int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if mid%2 == 0:
                if nums[mid] != nums[mid+1]:
                    right = mid
                else:
                    left = mid + 2
            else:
                if nums[mid] == nums[mid-1]:
                    left = mid+1
                else:
                    right = mid
        return nums[left]