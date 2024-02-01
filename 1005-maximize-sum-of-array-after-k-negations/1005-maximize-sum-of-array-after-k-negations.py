class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        #两次贪心 1.negative number 2. smallest number

        nums.sort(key = lambda x : -abs(x))

        for i in range(len(nums)):
            if k > 0 and nums[i]< 0:
                nums[i] *= -1
                k -= 1

        # 通过判断k的奇偶数，是否改变nums[-1]
        if k % 2 != 0:
            nums[-1] *= -1
        
        return sum(nums)    

