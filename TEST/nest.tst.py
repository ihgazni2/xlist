from xdict.jprint import pobj
from xdict.jprint import pdir
from xlist.nest import ListTree
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
>>> ltree
[1, [4], 2, [3, [5, 6]]]
 1, [4], 2, [3, [5, 6]]
     4       3, [5, 6]
                 5, 6
>>> ltree.tree()
[0]
[1]
[1][0]
[2]
[3]
[3][0]
[3][1]
[3][1][0]
[3][1][1]
[[0], [1], [1, 0], [2], [3], [3, 0], [3, 1], [3, 1, 0], [3, 1, 1]]
>>>

>>> ltree.flatten()
[1, 4, 2, 3, 5, 6]
>>>

