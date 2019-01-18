# 第四题 

# 当前位置的下一步总共有多少中可能性
def next_steps(loc,i):
    locs=loc[:]
    if i==1:
        locs[0],locs[1]=loc[0]-2,loc[1]+1
    elif i==2:
        locs[0],locs[1]=loc[0]-1,loc[1]+2
    elif i==3:
        locs[0],locs[1]=loc[0]+1,loc[1]+2
    elif i==4:
        locs[0],locs[1]=loc[0]+2,loc[1]+1
    elif i==5:
        locs[0],locs[1]=loc[0]+2,loc[1]-1
    elif i==6:
        locs[0],locs[1]=loc[0]+1,loc[1]-2
    elif i==7:
        locs[0],locs[1]=loc[0]-1,loc[1]-2
    elif i==8:
        locs[0],locs[1]=loc[0]-2,loc[1]-1
    return locs


def run_step(m, n):
    # 分别表示上一层、当前层、下一层
    levels=[[],[[0,0]],[]]

    step_num=1

    flag=True
    while flag:
        flag=False
        for loc in levels[1]:
            for i in range(1,9):
                # 到达对角线
                if next_steps(loc,i)==[m,n]:
                    return step_num

                elif next_steps(loc,i)[0]>=0 and next_steps(loc,i)[1]>=0 and next_steps(loc,i)[0]<=m and next_steps(loc,i)[1]<=n \
                    and next_steps(loc,i) not in levels[0] and next_steps(loc,i) not in levels[1] and next_steps(loc,i) not in levels[2]:
                    levels[2].append(next_steps(loc,i))
                    flag=True

        step_num += 1
        del levels[0]
        levels.append([])
    return -1


result = run_step(8, 8)
print(result)
