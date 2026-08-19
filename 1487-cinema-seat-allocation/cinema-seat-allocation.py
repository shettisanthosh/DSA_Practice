class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows={}
        for row,seat in reservedSeats:
            rows.setdefault(row,set()).add(seat)
        ans=(n-len(rows))*2
        for reserved in rows.values():
            left=all(seat not in reserved for seat in range(2,6))
            right=all(seat not in reserved for seat in range(6,10))
            if left and right:
                ans+=2
            elif left or right or all(i not in reserved for i in range(4,8)):
                ans+=1
        return ans