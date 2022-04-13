class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[int(i) for i in range(1,n**2+1)]
        #print(mat)
        ans=[[0 for i in range(n)] for j in range(n)]
        top,bottom=0,n-1
        left,right=0,n-1
        index=0
        while(True):
            if left>right: break
            for i in range(left,right+1):
                ans[top][i]=mat[index]
                index+=1
            top+=1
            if top>bottom: break
            for i in range(top,bottom+1):
                ans[i][right]=mat[index]
                index+=1
            right-=1
            
            if left > right: break
            for i in range(right,left-1,-1):
                ans[bottom][i]=mat[index]
                index+=1
            bottom-=1
            
            if top>bottom: break
            for i in range(bottom,top-1,-1):
                ans[i][left]=mat[index]
                index+=1
            left+=1
            
            
        return ans
        