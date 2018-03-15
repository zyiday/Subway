#-*- encoding=utf-8 -*-
import os

Subway_Map = {}
name_to_id = {}
id_to_name = {}
id_to_line = {}
cost = {}
parents = {}
visited = []

def dij_findnode(cost):
    minDist = 99999
    node = None
    for i in Subway_Map.keys():
        if (cost[i] < minDist) and (i not in visited):
            minDist = cost[i]
            node = i
    return node

def print_path(start, end):
    if end == start:
        print id_to_name[start]
    else:
        print_path(start, parents[end])
        print id_to_name[end]

def dijkstra():
    start_name = raw_input("start:")
    start = name_to_id[start_name]
    visited.append(start)
    station_num = len(Subway_Map)
    for i in range(station_num):
        cost[i] = 99999
    for i in Subway_Map[int(start)].keys():
        cost[i] = Subway_Map[start][i]
        parents[i] = start

    node = dij_findnode(cost)

    while node is not None:
        for i in Subway_Map[node]:  # 所有node结点的邻居结点
            newcost = cost[node] + Subway_Map[node][i]
            if newcost < cost[i]:
                parents[i] = node
                cost[i] = newcost
        visited.append(node)
        node = dij_findnode(cost)

    end_name = raw_input("end:")
    end = name_to_id[end_name]

    print_path(start, end)


def create_map():
    data_dir = "data"
    files = os.listdir(data_dir)

    station_num = -1

    for file in files:
        #file_name = file.decode('gbk').encode('utf-8')
        f = open('data/' + file, 'r')
        line = f.readline()[:-1]
        line_data = line.split('\t')
        station = line_data[0].split('——')
        #print file[:-4].decode('gbk').encode('utf-8')

        if station[0] not in name_to_id:
            station_num = station_num + 1
            name_to_id[station[0]] = station_num
            id_to_name[station_num] = station[0]
            id_to_line[station_num] = file[:-4]

        while line:
            distance = int(line_data[1][:-3])

            if station[1] not in name_to_id:
                station_num = station_num + 1
                name_to_id[station[1]] = station_num
                id_to_name[station_num] = station[1]
                id_to_line[station_num] = file[:-4]

            if name_to_id[station[0]] not in Subway_Map:
                adj_dict = {}
                adj_dict[name_to_id[station[1]]] = distance
                Subway_Map[name_to_id[station[0]]] = adj_dict
            else:
                Subway_Map[name_to_id[station[0]]][name_to_id[station[1]]] = distance

            if name_to_id[station[1]] not in Subway_Map:
                adj_dict = {}
                adj_dict[name_to_id[station[0]]] = distance
                Subway_Map[name_to_id[station[1]]] = adj_dict
            else:
                Subway_Map[name_to_id[station[1]]][name_to_id[station[0]]] = distance

            line = f.readline()[:-1]
            line_data = line.split('\t')
            station = line_data[0].split('——')

        '''
        print "______________________"
        for a in Subway_Map:
            print a,Subway_Map[a]
        print "______________________"
        return
        '''
    '''
    print "______________________"
    for a in Subway_Map:
        print a, Subway_Map[a]
    print "______________________"
    '''

if __name__ == '__main__':
    create_map()
    dijkstra()
    