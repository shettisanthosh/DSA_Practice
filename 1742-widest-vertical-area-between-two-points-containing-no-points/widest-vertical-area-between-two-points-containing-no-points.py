class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr=[]
        for i in range(len(points)):
            arr.append(points[i][0])
        arr.sort()
        maxx=0
        for i in range(1,len(arr)):
            maxx=max(maxx,(arr[i]-arr[i-1]))
        return maxx