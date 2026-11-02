class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sublist= len(matrix[0])
        flat=sum(matrix,[])
        left=0
        right=len(flat)-1

        while left<=right:
            middle=(left+right)//2
            if target==flat[middle]:
                return True
            elif flat[middle]>target:
                right=middle-1
            else:
                left=middle+1
        return False
        