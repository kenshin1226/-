# 0=[-1,3,-1,-1,-1,5,-1,-1]
# 1=[3,-1,4,-1,-1,5,-1,-1]
# 2=[-1,4,-1,2,1,-1,-1,-1]
# 3=[-1,-1,2,-1,-1,-1,-1,3]
# 4=[-1,-1,1,-1,-1,2,2,3,-1]
# 5=[5,5,-1,-1,2,-1,3,-1]
# 6=[-1,-1,-1,-1,3,3,-1,3]
# 7=[-1,-1,-1,3,-1,-1,3,-1]
aaa=[[-1,3,-1,-1,-1,5,-1,-1],
    [3,-1,4,-1,-1,5,-1,-1],
    [-1,4,-1,2,1,-1,-1,-1],
    [-1,-1,2,-1,-1,-1,-1,3],
    [-1,-1,1,-1,-1,2,3,-1],
    [5,5,-1,-1,2,-1,3,-1],
    [-1,-1,-1,-1,3,3,-1,3],
    [-1,-1,-1,3,-1,-1,3,-1]]
kiroku=[999,999,999,999,999,999,999,999]
kiroku[0]=0
memo=[999,999,999,999,999,999,999,999]#どこからきたかをメモする
memo[0]=0
kitaka=[0,0,0,0,0,0,0,0]
kitaka[0]=1

for i in range(8):
    if aaa[0][i]>0:
        print(aaa[0][i],i)
        if aaa[0][i]+kiroku[0]<kiroku[i]:#記録を塗り替えた場合に記録とメモを書き換える
            kiroku[i]=aaa[0][i]+kiroku[0]
            memo[i]=0
print(f"{kiroku=}")
for i in range(8):
    if aaa[1][i]>0:
        if aaa[1][i]+kiroku[1]<kiroku[i]:#記録を塗り替えた場合に記録とメモを書き換える
            kiroku[i]=aaa[1][i]+kiroku[1]
            print(f"{i=}{kiroku[i]=}")
            memo[i]=0
print(f"{kiroku=}")

        
#tunagu(0,1)

