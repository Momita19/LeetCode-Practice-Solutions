class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j =0
        string = []
        while i< len(word1) or j< len(word2):
            if i<len(word1):
                string += word1[i]
                i += 1
            if j <len(word2):
                string += word2[j]
                j += 1
        return ''.join(string)
            
        
        
        