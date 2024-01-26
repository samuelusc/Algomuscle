class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 按降序分配最大的饼干给胃口最大的孩子
        g.sort()
        s.sort()
        s_index = len(s) - 1
        count = 0
        for i in range(len(g)-1, -1, -1):
            while s_index>=0 and s[s_index] >= g[i]:
                s_index -= 1
                count += 1
                # 得跳出内循环
                break


        return count
        

            

