import numpy as np


def make_graph(h, s):
    children = {}
    parent = {}

    for i in range(len(s)):
        children.setdefault(h[i], []).append(s[i])
        parent[s[i]] = h[i]
    return children, parent


s = [1, 3, 4, 5, 2]  # номера работников
h = [2, 5, 3, 0, 5]  # начальники работников
remain = [3, 5]  # какие работники должны остаться
children, parent = make_graph(h, s)

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

print(parent)
