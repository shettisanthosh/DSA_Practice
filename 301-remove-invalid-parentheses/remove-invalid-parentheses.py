class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        rem_l=0;rem_r=0
        for char in s:
            if char=='(':
                rem_l+=1
            elif char==')':
                if rem_l>0:
                    rem_l-=1
                else:
                    rem_r+=1
        st=set()
        n=len(s)
        def solve(i,count,rem_l,rem_r,curr):
            if count<0:
                return 
            if i==n:
                if count==0 and rem_l==0 and rem_r==0:
                    st.add("".join(curr))
                return 
            if s[i]!='(' and s[i]!=')':
                curr.append(s[i])
                solve(i+1,count,rem_l,rem_r,curr)
                curr.pop()
                return
            if s[i]=='(':
                curr.append(s[i])
                solve(i+1,count+1,rem_l,rem_r,curr)
                curr.pop()
                if rem_l>0 and (i==0 or s[i-1]!='('):
                    k=1
                    while i+k<n and s[i+k]=='(':
                        k+=1
                    for j in range(1, min(k,rem_l)+1):
                        solve(i+j,count,rem_l-j,rem_r,curr)
            elif s[i]==')':
                curr.append(s[i])
                solve(i+1,count-1,rem_l,rem_r,curr)
                curr.pop()
                if rem_r>0 and (i==0 or s[i-1]!=')'):
                    k=1
                    while i+k<n and s[i+k]==')':
                        k+=1
                    for j in range(1, min(k,rem_r)+1):
                        solve(i+j,count,rem_l,rem_r-j,curr)
        solve(0,0,rem_l,rem_r,[])
        return list(st)