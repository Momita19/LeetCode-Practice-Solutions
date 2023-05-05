class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        count =0
       
        for i in range(k):
            if s[i] in vowels:
                count += 1
        count_max = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            count_max = max(count_max, count)
        return count_max
            
        