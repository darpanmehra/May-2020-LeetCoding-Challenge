#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#Examples:
#1. s = "leetcode", return 0.
#2. s = "loveleetcode", return 2.

#Using 2 for loops
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = Counter(s)
        val = ''
        i = 0
        for keys in s_dict:
            if s_dict[keys] == 1:
                val = keys
                break
        if val == '':
            return -1
        for element in s:
            if element == val:
                return i
            i += 1


#Using 1 Loop
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = Counter(s)
        for index, element in enumerate(s):
            if s_dict[element] == 1: return index; break
        return -1
