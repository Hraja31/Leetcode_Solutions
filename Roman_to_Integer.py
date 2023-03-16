class Solution(object):
    def romanToInt(self, s):
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        l = len(s)
        num = 0
        skip = False
        for i in range(0,l):
            if skip == False:
                if i == l-1:
                    num = num+dict[s[i]]
                    print(i)
                elif dict[s[i]]>=dict[s[i+1]]:
                    num = num + dict[s[i]]
                elif dict[s[i]]<dict[s[i+1]]:
                    num = num + dict[s[i+1]] - dict[s[i]]
                    skip = True
            else:
                skip = False
            print(num)
        return num
