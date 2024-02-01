class Solution:
    def candy(self, ratings: List[int]) -> int:
        

        allocate = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                # 注意这里应该是 allocate[i-1] + 1 而不是 allocate[i] + 1
                allocate[i] = allocate[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                allocate[i] = max(allocate[i], allocate[i+1] + 1) 

        return sum(allocate)   