class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for _ in range(num_people)]
        can  = 1
        while candies>0:
            if candies >= can:
                ans[(can-1)%num_people] +=can
            else:
                ans[(can-1)%num_people]+=candies
            candies-=can
            can+=1
        return ans

# Approach is made by logic
# time complexity O(log(candies))