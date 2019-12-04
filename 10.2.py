nodes = [(2,10),(2,5),(8,4),(5,8),(7,5),(6,4),(1,2),(4,9)]
def cal_distance(node1,node2):
    return (node1[0] - node2[0])**2 + (node1[1] - node2[1])**2
def center(a):
    sum_x = sum_y = 0
    for x,y in a:
        sum_x += x
        sum_y += y

    return (sum_x / len(a), sum_y / len(a))

cluster1 = [(2,10)]
cluster2 = [(5,8)]
cluster3 = [(1,2)]

for _ in range(1000):
    center1 = center(cluster1)
    center2 = center(cluster2)
    center3 = center(cluster3)
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for node in nodes:
        min_distance = min(cal_distance(node,center1),cal_distance(node,center2),cal_distance(node,center3))
        if cal_distance(node,center1) == min_distance:
            cluster1.append(node)
        elif cal_distance(node,center2) == min_distance:
            cluster2.append(node)
        else:
            cluster3.append(node)

print((center1,center2,center3))
print(cluster1)
print(cluster2)
print(cluster3)