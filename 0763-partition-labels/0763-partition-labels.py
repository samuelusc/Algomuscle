class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = [0] * 26
        res = []
        for i in range(len(s)):
            hashmap[ord(s[i]) - ord('a')] = i
        print(hashmap)


        left, right = 0, 0
        for i in range(len(s)):
            right = max(right, hashmap[ord(s[i])-ord("a")])

            if right == i:
                #return the size of the part +1
                res.append(right - left + 1)
                left = i+1


        return res
