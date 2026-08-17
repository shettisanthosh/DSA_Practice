class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count=0;i=0;j=1
        while j<len(bank):
            curr=bank[i].count('1')
            nextt=bank[j].count('1')
            if curr==0:
                i+=1
                j=i+1
            elif nextt==0:
                j+=1
            else:
                count+=curr*nextt
                i=j
                j=i+1
        return count