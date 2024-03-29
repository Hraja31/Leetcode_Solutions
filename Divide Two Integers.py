class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        neg=0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if dividend<0 or divisor<0:
            if dividend<0 and divisor < 0:
                neg = 0
            else:
                neg=1
        a = abs(dividend)
        b = abs(divisor)
        for i in range(31,-1,-1):
            if b << i <= a :
                a-=b<<i
                ans+= 1<<i
        return ans if neg == 0 else -1*ans
