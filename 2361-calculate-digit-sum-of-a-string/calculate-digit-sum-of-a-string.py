class Solution:
    def digitSum(self, s: str, k: int) -> str:
        curr=[int(c) for c in s]
        while len(curr)>k:
            nxt=[]
            for i in range(0,len(curr),k):
                total=sum(curr[i:i+k])
                nxt.extend(int(d) for d in str(total))
            curr=nxt
        return "".join(map(str,curr))