class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0,0 
        for bill in bills:
            if bill == 5:
                five += 1

            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            
            # 在20情况下，要优先使用10+5 其次5*3
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                
                elif five > 2:
                    five -= 3

                else:
                    return False
        return True