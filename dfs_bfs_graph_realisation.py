import numpy as np
import queue


def incidence_matrix():
    print('введите количество вершин в графе')
    n = int(input())
    graph = np.zeros((n, n))

    print('введите количество ребер в графе')
    m = int(input())

    for i in range(m):
        print(f'введите {i} ребро графа')

        print(f'введите u ')
        u = int(input())

        print(f'введите v ')
        v = int(input())
        graph[u, v] = 1
    return graph


def incidence_list():
    graph = {}
    print('введите количество ребер в графе')
    m = int(input())

    for i in range(m):
        print(f'введите {i} ребро графа')

        print(f'введите u ')
        u = int(input())

        print(f'введите v ')
        v = int(input())
        graph.setdefault(u, set()).add(v)

    return graph


def dfs(v, graph, colors):
    print(f'я в {v} вершине')

    if v in graph.keys():
        colors[v] = 'gray'
        for children in graph[v]:
            if colors[children] == 'white':
                dfs(children, graph, colors)
            if colors[children] == 'gray':
                print('цикл найден!')
            colors[v] = 'black'


def bfs(v, graph, size):
    vis = np.zeros(size)
    q = queue.Queue()
    q.put(v)

    while not q.empty():
        v = q.get()
        print(f'я в {v} вершине')

        vis[v] = 1
        if v in graph.keys():
            for children in graph[v]:

                if vis[children] == 0:
                    vis[children] = 1
                    q.put(children)


print('введите количество вершин в графе')
size = int(input())

print(f'представление графа в виде списков смежности ')

graph = incidence_list()
print(graph)

colors = ['white']*size

print('bfs')
bfs(list(graph.keys())[0], graph, size)

print('dfs')
dfs(list(graph.keys())[0], graph, colors)
