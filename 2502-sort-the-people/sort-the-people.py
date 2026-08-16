class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={key:value for key,value in zip(heights,names)}
        i=0
        for key in sorted(d,reverse=True):
            names[i]=d[key]
            i+=1
        return names