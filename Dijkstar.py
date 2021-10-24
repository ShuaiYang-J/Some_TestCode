# Dijstar算法 最短路径
# 1.确定权矩阵

def djkstra(graph, start, end):
    path_set = set()    # set() 函数创建一个无序不重复元素集 
    priority_dic = {}
    for k in graph.keys():
        priority_dic[k] = [9999, False, ""] # 权重表构建为一个3维数组，分别是：最小路径代价，是否计算过最小边，最小路径
    priority_dic[start][0] = 0

    # 判断权重表中所有路点是否添加完毕
    def isSelectAll():
        ret = True
        for val in priority_dic.values():
            if not val[1]:
                ret = False
                break
        return ret

    while not isSelectAll():
        find_point = start
        find_path = start
        min_distance = 9999
        for path in path_set:
            end_point = path[-1]
            path_distance = priority_dic[end_point][0]
            if path_distance < min_distance and not priority_dic[end_point][1]:
                find_point = end_point
                find_path = path
                min_distance = path_distance
        find_distance = priority_dic[find_point][0]
        neighbors = graph[find_point]
        for k in neighbors.keys():
            p = find_path + "-" + k
            weight = find_distance + neighbors[k]
            path_set.add(p)
            if weight < priority_dic[k][0]:
                priority_dic[k][0] = weight
                priority_dic[k][2] = p
        priority_dic[find_point][1] = True

    return priority_dic[end]


if __name__ == '__main__':
    # 用于测试的图
    graph = {
                "A": {"B": 8, "D": 10, "E": 12},
                "B": {"C": 6, "F": 12},
                "C": {"F": 8},
                "D": {"E": 10, "G": 30},
                "E": {"F": 10},
                "F": {"G": 12},
                "G": {}
            }
    result = djkstra(graph, "A", "F")
    print(result)
