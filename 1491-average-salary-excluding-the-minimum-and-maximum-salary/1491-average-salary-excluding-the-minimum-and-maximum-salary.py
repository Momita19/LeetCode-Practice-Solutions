
class Solution:
    def average(self, salary: List[int]) -> float:
        sum_n = 0
        maxSalary = -1
        minSalary = max(salary)
        for i in range(0, len(salary)):
            sum_n = sum_n + salary[i]

            maxSalary = max(salary[i], maxSalary)
            minSalary = min(salary[i], minSalary)
       
        return (sum_n - minSalary - maxSalary)/(len(salary)-2)
        
        
        