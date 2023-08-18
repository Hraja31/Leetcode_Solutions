class Solution:
    def interchangeableRectangles(self, r: List[List[int]]) -> int:
        c=0
        for i in range(len(r)):
            r[i] = r[i][0]/r[i][1]
        d = {}
        for i in r:
            d[i] = d.get(i,0)+1
        for i in d.values():
            if(i>1):
                c+=i*(i-1)/2
        return int(c)
