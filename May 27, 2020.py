""""
Possible Bipartition
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
""""


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        bag = [[] for i in range(N + 1)]
        visited = [-1] * (N + 1)
        count = 0
        for dislike in dislikes:
            bag[dislike[0]].append(dislike[1])
            bag[dislike[1]].append(dislike[0])

        for i in range(1, N + 1):
            if visited[i] == -1 and len(bag[i]) > 0:
                if not self.visit(0, i, bag, visited):
                    return False

        return True

    def visit(self, curLevel, i, bag, visited):
        if visited[i] >= 0:
            return (curLevel - visited[i]) % 2 == 0

        visited[i] = curLevel
        for des in bag[i]:
            if not self.visit(curLevel + 1, des, bag, visited):
                return False
        return True