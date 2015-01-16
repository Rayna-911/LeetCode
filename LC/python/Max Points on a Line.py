# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    #k = inf; (1,2) and (1,2)
    def maxPoints(self, points):
        if len(points)<3:
            return len(points)
            
        res = 0
        for i in range(len(points)):
            slop = {"inf":0}
            same = 1
            for j in range(len(points)):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    slop["inf"] += 1
                elif  points[i].x != points[j].x:
                    k = 1.0 * (points[i].y - points[j].y)/(points[i].x - points[j].x)
                    if k in slop:
                        slop[k] += 1
                    else:
                        slop[k] = 1
                else:
                    same += 1
            res = max(res,max(slop.values())+same)
        return res
