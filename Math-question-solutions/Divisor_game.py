#We'll use the mathematical property of optimal play:
#Even number advantage: When n is even, Alice can always choose x=1 (which divides any number), leaving Bob with an odd number
#Odd number disadvantage: When n is odd, all its divisors are odd, so Alice must subtract an odd number, leaving Bob with an even number
#Optimal strategy: Alice wins when she can force Bob into losing positions (odd numbers)
#Pattern recognition: Since the game follows optimal play, Alice wins if and only if she starts with an even number 

class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2==0:
            return True 
        return False