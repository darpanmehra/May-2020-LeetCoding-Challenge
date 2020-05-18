# Find All Anagrams in a String
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.
# Example 1:
# Input: s: "cbaebabacd" p: "abc"
# Output: [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
# Input: s: "abab" p: "ab"
# Output: [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        output = []
        p = Counter(p)
        window = None
        for i in range(0, s_len-p_len+1):
            if i == 0:
                window = s[:p_len]
            else:
                window[s[i-1]] -=1
                window[s[i+p_len-1]] +=1
            if len(window - p) == 0:
                output.append(i)
        return output