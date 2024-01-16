class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 用dictionary, {key: a+b value: count}
        hashmap = {}

        for a in nums1:
            for b in nums2:
                #如果a+b已经在hashmap中则返回count+1，否则返回 0 + 1
                hashmap[a+b] = hashmap.get(a+b, 0) + 1

        #initialize complement number of c+d
        count = 0
        
        for c in nums3:
            for d in nums4:
                target= -(c+d)
                # not hashmap.get(target, 0) + 1
                # 累计球 c+d 补数的数量
                # 如果有多个c+d 则会每个这样的组合都会被考虑在内
                count += hashmap.get(target, 0)

        return count
