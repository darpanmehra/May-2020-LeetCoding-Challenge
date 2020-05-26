"""
Question: Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic ={0:0}
        count = max_length = 0
        for i,num in enumerate(nums,1):
            if num == 0:
                count -=1
            else:
                count +=1
            if count in dic:
                max_length = max(max_length, i - dic[count])
            else:
                dic[count] = i
        return max_length