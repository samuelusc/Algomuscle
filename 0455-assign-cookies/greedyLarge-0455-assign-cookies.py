class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 按降序分配最大的饼干给胃口最大的孩子
        g.sort()
        s.sort()
        s_index = len(s) - 1
        count = 0
        # 注意这里的循环顺序不能颠倒
        # 例如 g[1,2,7,10] s[1,3,5,9]
        for i in range(len(g)-1, -1, -1):
            if s_index>=0 and s[s_index] >= g[i]:
                s_index -= 1
                count += 1
  
        return count
        

            

