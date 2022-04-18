class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0 or len(matrix[0])==0: return []
        nums=[]
        row,col=len(matrix)-1, len(matrix[0])-1
        i,j=0,0
        flag=0
        for j in range(col+1):
            nums.append(matrix[i][j])
        while row>=0 and col>=0:
            if flag%4==0:
                for k in range(row):
                    i+=1
                    nums.append(matrix[i][j])
                row-=1
            elif flag%4==1:
                for k in range(col):
                    j-=1
                    nums.append(matrix[i][j])
                col-=1
            elif flag%4==2:
                for k in range(row):
                    i-=1
                    nums.append(matrix[i][j])
                row-=1
            elif flag%4==3:
                for k in range(col):
                    j+=1
                    nums.append(matrix[i][j])
                col-=1
            flag+=1
        return nums
        
        