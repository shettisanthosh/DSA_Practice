class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            var=[]
            for i in range(0,len(s),k):
                var.append(str(sum(int(c) for c in s[i:i+k])))
            s="".join(var)
        return s