# approach 1 brute force approach 
# find all the odd length subarrays then sum of that add to total 
# time complexity O(n^2)


class Solution:
    def sumOddLengthSubarrays(self, arr)-> int:
        total = 0
        for i in range(len(arr)):
            total +=arr[i]
            j = i+3
            while j <=len(arr):
                total+=sum(arr[i:j])
                j+=2
        return total
    
# appraoch 2 :optimized 
# 1 2 3 4 5 subarray length 1
# 1 2 X X X subarray length 2
# X 2 3 X X subarray length 2
# X X 3 4 X subarray length 2
# X X X 4 5 subarray length 2
# 1 2 3 X X subarray length 3
# X 2 3 4 X subarray length 3
# X X 3 4 5 subarray length 3
# 1 2 3 4 X subarray length 4
# X 2 3 4 5 subarray length 4
# 1 2 3 4 5 subarray length 5

# 5 8 9 8 5 total times each index was added, k = (i + 1) * (n - i)
# 3 4 5 4 3 total times in odd length array with (k + 1) / 2
# 2 4 4 4 2 total times in even length array with k / 2s

# time complexity O(n)
class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        sums= 0
        n = len(arr)
        for i in range(n):
            k = (i+1)*(n-i)
            sums+=arr[i]*((k+1)//2)
        return sums
