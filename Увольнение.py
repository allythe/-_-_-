import numpy as np
import copy


def make_graph(h, s):
    children = {}
    parent = {}

    for i in range(len(s)):
        children.setdefault(h[i], []).append(s[i])
        parent[s[i]] = h[i]
    return children, parent


def main():
    with open('dismissal.txt') as file:
        # кол-во сотрудников и запросов
        n, q = list(map(int, file.readline().split()))
        s, h = [], []
        for i in range(n):
            cur_s, cur_h = list(map(int, file.readline().split()))
            s.append(cur_s)  # номера работников
            h.append(cur_h)  # начальники работников

        children_graph, parent_graph = make_graph(h, s)

        for i in range(q):
            children, parent = copy.deepcopy(
                children_graph), copy.deepcopy(parent_graph)

            k = int(file.readline())  # кол-во оставшихся сотрудников
            remain = list(map(int, file.readline().split()))

            to_delete = list(np.unique(s+h))
            for el in remain:
                to_delete.remove(el)
            to_delete.remove(0)

            for el in to_delete:
                par = parent[el]

                if el in children:
                    for child in children[el]:
                        parent[child] = par
                        children[par].append(child)

                    children.pop(el)
                parent.pop(el)
                children[par].remove(el)

            for k in parent.keys():
                print(k, parent[k])


if __name__ == '__main__':
    main()
