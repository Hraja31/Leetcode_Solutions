class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        c = capacity
        s=0
        for i in range(n):
            a = plants[i]
            if c>=a:
                c-=a
                s+=1
            else:
                c=capacity-a
                s+= (2*i)+1
        return s
