class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d={}
        for k in range(1,n+1):
            d[k] = []
        for i in reservedSeats:
            d[i[0]].append(i[1])

        c = 0
        for p in range(1,len(d)+1):
            #print(d[p])
            l2 = d[p]
            if 2 not in l2 and 3 not in l2 and 4 not in l2 and 5 not in l2:
                c+=1
                l2=l2+[2,3,4,5]
            if 4 not in l2 and 5 not in l2 and 6 not in l2 and 7 not in l2:
                c+=1
                l2=l2+[4,5,6,7]
            if 6 not in l2 and 7 not in l2 and 8 not in l2 and 9 not in l2:
                c+=1
                l2=l2+[6,7,8,9]
        return c
