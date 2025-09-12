class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt=0
        rem = 0
        while numBottles>0:
            cnt+=numBottles
            full  = numBottles//numExchange
            rem += (numBottles%numExchange)
            if rem>=numExchange:
                full+=(rem//numExchange)
                rem =(rem%numExchange) 
            numBottles = full
        return cnt
    
    # time complexity O(n)
    