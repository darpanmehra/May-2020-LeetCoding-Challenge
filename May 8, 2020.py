#Check If It Is a Straight Line
#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
#Example: Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
#Output: true

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #General Equation of line is Ax+By+C=0
        #Using Above, y = -(A/B)x - (C/B)
        #Slope m = (y2-y1)/(x2-x1), also m = -(A/B)
        #So, A = y1-y2, and B = x2-x1
        if len(coordinates)>2:
            A = coordinates[0][1] - coordinates[1][1]
            B = coordinates[1][0] - coordinates[0][0]
            C = -A*coordinates[0][0] - B*coordinates[0][1]
            for point in coordinates[2:]:
                if (A*point[0] + B*point[1]) + C != 0:
                    return False
        return True