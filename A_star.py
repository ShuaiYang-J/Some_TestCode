# 贪心算法 路径规划--
# 1.寻找地图中目标位置 起始点信息 障碍位置信息
# 2.便利全部方向 量化每步的代价并存储走过的位置
import matplotlib.pyplot as plt
import numpy as np



def heuristic_distace(Neighbour_node,target_node):
    # 计算当前前进点和目标点之间的x-x0 y-y0绝对值 H 不用平方，三角形两边和 曼哈顿距离
    H = abs(Neighbour_node[0] - target_node[0]) + abs(Neighbour_node[1] - target_node[1])
    #  对角线距离 h = max { abs(current_cell.x – goal.x), abs(current_cell.y – goal.y) } 
    return H

def go_around(direction):
    # 可以对方向进行代价赋值
    box_length = 1
    diagonal_line = box_length * 1.4
    if (direction==0 or direction==2 or direction==6 or direction==8):
        return diagonal_line
    elif (direction==1 or direction==3 or direction==4 or direction==5 or direction==7):
        return diagonal_line

def find_coordinate(map,symble):
    #store coordinate
    result=[]
    #  enumerate(sequence, [start=0])  起始下标和参数 如果是多维列表--每次的Value为一整行A[0]
    # 提取特定标记的行列信息
    for index1,value1 in enumerate(map):
        if symble in value1:
            row = index1
            for index2, value2 in enumerate(map[index1]):
                if symble==value2:
                   column = index2
                   result.append([row, column])
    return result

map =[[".", ".", ".", "#", ".", "#", ".", ".", ".", "."],
      ["#", "#", "#", ".", ".", "#", ".", "#", ".", "#"],
      [".", "#", "#", ".", "#", ".", "#", ".", ".", "f"],
      [".", "#", "#", ".", ".", ".", ".", ".", "#", "."],
      [".", ".", ".", ".", "#", "#", ".", ".", "#", "."],
      [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
      [".", "#", ".", ".", ".", "#", "#", ".", "#", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
      [".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
      ["s", ".", ".", "#", "#", "#", ".", ".", "#", "."],
      ["#", "#", ".", ".", "#", "#", "#", ".", "#", "."],
      [".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
      [".", ".", ".", ".", "#", "#", ".", ".", "#", "."]]

#these datas are store in the form of list in a singal list

obstacle = find_coordinate(map,"#")

start_node = find_coordinate(map,"s")[0] #因为只存在一个 s
target_node = find_coordinate(map,"f")[0]
# start_node = [0,0] #因为只存在一个 s
# target_node = [12,12]
current_node = start_node
path_vertices = [start_node]
#visited_vertices should be stored in the form of a singal list
Neighbour_vertices = []

while current_node != target_node:

    x_coordinate = current_node[0]
    y_coordinate = current_node[1]
    F = []
    # 贪心算法 全部方向的运动
    Neighbour_vertices =   [[x_coordinate - 1, y_coordinate - 1],
                            [x_coordinate - 1, y_coordinate    ],
                            [x_coordinate - 1, y_coordinate + 1],
                            [x_coordinate,     y_coordinate - 1],
                            [x_coordinate    , y_coordinate    ],
                            [x_coordinate,     y_coordinate + 1],
                            [x_coordinate + 1, y_coordinate - 1],
                            [x_coordinate + 1, y_coordinate    ],
                            [x_coordinate + 1, y_coordinate + 1]]

    for index, value in enumerate(Neighbour_vertices):
        # 边界限制 range(len()) 0-(len-1)  'in'很重要
        if value[0] in range(len(map)):
            if value[1] in range(len(map)):
                # 判定是否存在障碍 障碍信息+目前走过的节点 列表+不等于数值相加 是内容扩充
               if value not in obstacle+path_vertices:
                # 未曾走过的点和不存在障碍的点排出后 计算距离（代价）
                    # F.append(heuristic_distace(value, target_node) + go_around(index))
                    F.append(heuristic_distace(value, target_node))
               else:
                    F.append(10000)
            else:
                    F.append(10000)
        else:
                    F.append(10000)
               #a very large number
    # print(F)
    if min(F)>9999:
        print("Can't Go to end")
        break
    else:
        current_node=Neighbour_vertices[F.index(min(F))]
        print(current_node)

        path_vertices.append(current_node) #不重新走
        # if current_node not in visited_vertices:
        #     visited_vertices.append(current_node)
        # else:
        #     print("there is no route between")
        #     break

# print(path_vertices)
# 可视化
# plt.scatter(0,0,marker='+')
ax = plt.gca() 
# ax.xaxis.set_ticks_position('top')  #将x轴的位置设置在顶部
# ax.invert_xaxis()  #x轴反向
# ax.yaxis.set_ticks_position('right')  #将y轴的位置设置在右边
ax.invert_yaxis()  #y轴反向

x=[]
y=[]
plt.scatter(start_node[1],start_node[0],color='b',marker='*')
plt.scatter(target_node[1],target_node[0],color='b',marker='*')
for i in range(len(obstacle)):
    plt.scatter(obstacle[i][1],obstacle[i][0],color='r',marker='+')
for i in range(len(path_vertices)):
    x.append(path_vertices[i][1])
    y.append(path_vertices[i][0])
    # plt.scatter(path_vertices[i][1],path_vertices[i][0],color='b',marker='*')
plt.plot(x,y,c='y')
plt.grid()
plt.show()
#存在问题：路径规划可能会走错路 但是从距离做判定上是最优解
