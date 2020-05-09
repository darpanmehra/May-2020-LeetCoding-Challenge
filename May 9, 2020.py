#Valid Perfect Square
#Given a positive integer num, write a function which returns True if num is a perfect square else False.
#Note: Do not use any built-in library function such as sqrt.
#Example 1: Input: 16, Output: true
#Input: 14, Output: false

#Binary Search Method
class Solution:
    def ifPerfectSquare(self, num: int)->bool:
        left = 0
        right = num
        while left <= right:
            mid = left + (right-left)//2
            if mid*mid == num: return True
            elif mid*mid > num: right = mid-1
            else: left = mid+1
        return False