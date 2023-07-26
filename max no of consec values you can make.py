class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ss=1
        for i in coins:
            if i>ss:
                break
            else:
                ss=ss+i
        return ss
