class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        n_list = list(str(n))
        
        # 从后向前list(size, x + 1 = 实际停止位置， -1)
        for i in range(len(n_list)-1,0,-1):
            if n_list[i-1] > n_list[i]:
                n_list[i-1] = str(int(n_list[i-1]) - 1)
                n_list[i:] = "9" * (len(n_list) - i)

        #最后除了拼接成string 还需要转成 integer
        return int("".join(n_list))