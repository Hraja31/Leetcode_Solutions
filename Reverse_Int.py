class Solution(object):
    def reverse(self, x):
        s = str(abs(x))
        y =int(s[::-1])
        if abs(y)>=pow(2,31):
            y=0
        elif x<0:
            y = y*-1
        return y
