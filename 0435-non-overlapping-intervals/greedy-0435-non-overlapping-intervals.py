class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],x[1]))
        count = 0

        # 设定第一个比较对象
        pre_end = intervals[0][1]
        for i in range(1, len(intervals)):
            
            if intervals[i][0] < pre_end:
                count += 1
                pre_end = min(pre_end, intervals[i][1])
            # 更新 pre_end
            else:
                pre_end = intervals[i][1]

        
        return count
