class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st=[]
        N=len(s)
        S=list(s)
        for i in range(N):
            if S[i]=='(':
                st.append(i)
            elif S[i]==')':
                if st: st.pop()
                else: S[i]=""
        for j in st:
            S[j]=""
        return "".join(S)