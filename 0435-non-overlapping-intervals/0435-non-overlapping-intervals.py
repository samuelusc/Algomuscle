class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda interval: (interval[0],interval[1]))

        pre_end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] >= pre_end:
                pre_end = intervals[i][1]
            

            else:
                count += 1
                pre_end = min(intervals[i][1],pre_end)

        return count