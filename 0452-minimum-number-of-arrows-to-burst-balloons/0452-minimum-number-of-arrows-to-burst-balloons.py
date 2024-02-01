class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x: (x[0],x[1]))
        # 对于第一个或第一组重叠气球至少需要一箭
        count = 1

        for i in range(len(points)-1):
            if points[i][1] < points[i + 1][0]:
                count += 1
            
            else:
                points[i+1][1] = min(points[i][1], points[i+1][1])

        
        return count

