class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # seen = mark
        # i+1 
        # when reach to i == n
        # j ++
        # when j reach to n
        # i -- 
        # when i reach to 
        # j-- but till when which is unseen box
        # same for i--
      #   i    n
      # j [1 2 3]           2nd method-row pop, transpose, reverse --> result add in result
      #   [4 5 6]
      # m [7 8 9]
        
      #   print i  to n
      #   print j  to ij
      #   print ij to j=0
    
    
        result = []
        while matrix:
            result += matrix.pop(0)
            print(result)
            matrix = [*zip(*matrix)][::-1]
            print(matrix)
        return result
    
        
        
        
        