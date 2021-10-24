#连通域问题 20211020面试题
# 要注意循环函数的设计 各边界条件的设计 --减少循环复杂度

def check(i,j,A):
    row=len(A)
    if row!=0:
        col=len(A[0])
        if i<0 or i>row-1 or j<0 or j>col-1:
            pass
        else:
            if A[i][j]==1:
                A[i][j]=-1
                check(i-1,j,A)
                check(i+1,j,A)
                check(i,j-1,A)
                check(i,j+1,A)
    else:
        pass

A=[[0,1,1,0],
   [0,0,0,0],
   [1,0,1,0]]
row=len(A)
col=len(A[0])
count=0
for i in range(row):
    for j in range(col):
        if A[i][j]==1:
            count=count+1
            check(i,j,A)
        else:
            continue

print(count)
