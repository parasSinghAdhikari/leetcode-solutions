class Solution:
    def average(self, salary) -> float:
        mini = min(salary)
        maxi  = max(salary)

        sums = 0
        for num in salary:
            if num!=mini and num!=maxi:
                sums+=num
                
        avg = sums/(len(salary)-2)
        return avg
        