# Permutation in String
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo", Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo", Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1) # target
        s2_length = len(s2) # search string
        s1 = Counter(s1)
        window = None
        for i in range(0,s2_length-s1_length+1):
            if i == 0:
                window = s2[:s1_length]
            else:
                window[s2[i-1]] -=1
                window[s2[i+s1_length-1]] +=1
            if len(window - s1) == 0:
                return True
        return False