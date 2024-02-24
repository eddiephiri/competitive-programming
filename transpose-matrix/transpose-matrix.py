class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        N = len(matrix)
        for col in range(len(matrix[0])):
            l = []
            for row in range(len(matrix)):
                l.append(matrix[row][col])
            res.append(l)
        
        return res