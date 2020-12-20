"""This script solves traveling salesman problem via dijkstra algorithm """
import re
import sys
from heapq import heappop, heappush


def dijkstra(start, goal, graph):
    """
    :param start: starting point
    :param goal:  destination point
    :param graph: matrix of routes
    :return: visited points, cost of optimal route
    """
    queue = []
    # put the initial vertex in the priority queue
    heappush(queue, (0, start))
    # form a dictionary of visited vertices
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break
        # we take out the vertex with the lowest price
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            # new_ cost is cost of moving for each adjacent vertices to the current vertex
            new_cost = cost_visited[cur_node] + neigh_cost
            # if the vertex is absent in cost_visited or the price is less
            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                # put such vertex to the queue & update the cost of the path to it
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                # save where you came from
                visited[neigh_node] = cur_node
    return visited, cost_visited


#  define quantity of cities
quantity_cities = input('Enter, please, a quantity of cities > ')
if quantity_cities.isdigit() is False:
    print('Error. The quantity of cities should be a number. Abnormal end')
    sys.exit(1)
cities_amount = int(quantity_cities)
if cities_amount > 9999:
    print('Error. The quantity of cities should be less 10000. Abnormal end')
    sys.exit(2)
city_matrix = {}
city_names = {}

# matrix of routes definition
for i in range(1, cities_amount + 1):
    city = input('Enter, please, a city name > ')
    if re.match(r'[a-zA-Z]+', city) is None:
        print('Error. The name of city can contain only letters. Abnormal end')
        sys.exit(3)
    if len(city) > 9:
        print('Error. The length of name of city should be less 10 letters. Abnormal end')
        sys.exit(4)
    neighbors = input('Enter, please, the number of neighbors of city ' + city + ' > ')
    if neighbors.isdigit() is False:
        print('Error. The number of neighbors should be a number. Abnormal end')
        sys.exit(5)
    neighbors_count = int(neighbors)
    city_matrix[str(i)] = []
    city_names[str(i)] = city
    for j in range(1, neighbors_count + 1):
        neighbor_ind, route_cost = input('Enter,please, index of city connected to ' + city +
                                         ' and transportation cost >').split()
        if neighbor_ind.isdigit() is False:
            print('Error. The index of city should be a number. Abnormal end')
            sys.exit(6)
        if route_cost.isdigit() is False:
            print('Error. The route_cost should be a number. Abnormal end')
            sys.exit(7)
        temp_dic = (int(route_cost), neighbor_ind)
        city_matrix[str(i)].append(temp_dic)

# setting quantity of paths which should be researched
number_paths = input('Enter, please, how many routes do you want to research >')
if number_paths.isdigit() is False:
    print('Error. The quantity of routes should be a number.  Abnormal end')
    sys.exit(6)
paths_quantity = int(number_paths)

paths_def = {}
for i in range(1, paths_quantity+1):
    print('\nRoute No ' + str(i))
    for j in range(1, len(city_names) + 1):
        print('Index '+str(j)+'. '+city_names[str(j)] + '. ', end='')
    paths_def[i] = {}
    paths_def[i]['from'] = input('\nIndex of city of start >')
    paths_def[i]['to'] = input('Index of city of finish >')

for i in range(1, paths_quantity+1):
    start_point = paths_def[i]['from']
    destination_point = paths_def[i]['to']
    matrix = city_matrix
    visited_points, visited_cost = dijkstra(start_point, destination_point, matrix)
    current_point = destination_point
    route_cost = visited_cost[current_point]
    print('\n Route № '+str(i) + ' optimal cost = ', route_cost)
