class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_r=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=max_r
            max_r=max(max_r,current)
        return arr
