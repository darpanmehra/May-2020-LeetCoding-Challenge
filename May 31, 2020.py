"""
Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row = len(word1)
        column = len(word2)
        table = [[0]*(column+1) for _ in range(row+1)]
        for i in range(column+1):
            table[0][i] = i
        for j in range(row+1):
            table[j][0] = j
        for i in range(1,row+1):
            for j in range(1,column+1):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = 1 + min(table[i-1][j],table[i][j-1],table[i-1][j-1])
        return table[-1][-1]