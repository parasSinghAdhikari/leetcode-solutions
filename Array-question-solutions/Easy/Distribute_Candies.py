class Solution:
    def distributeCandies(self, candyType) -> int:
        n =len(set(candyType))
        if len(candyType)//2 >= n:
            return n 
        return len(candyType)//2
        

        