#Remove K Digits
#Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
#Note:
#The length of num is less than 10002 and will be ≥ k.
#The given num does not contain any leading zero.
#Examples:
#Input: num = "1432219", k = 3, Output: "1219"
#Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
#Input: num = "10200", k = 1, Output: "200"
#Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k>0 and stack and stack[-1] > digit:
                stack.pop()
                k-=1
            stack.append(digit)
        return ''.join(stack[:-k or None]).lstrip("0") or "0"