class Solution(object):
    def longestCommonPrefix(self, strs):
        s = strs[0]
        for i in strs:
            temp = s
            s = ""
            l = min(len(temp),len(i))
            for j in range(0,l):
                if temp[j] == i[j]:
                    s = s+temp[j]
                else:
                    break
        return s
            
