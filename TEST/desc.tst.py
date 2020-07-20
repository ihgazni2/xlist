#def vil_dict(l):
from xlist.desc import vil_dict
ol = [11,22,33,11,44,55]
assert(vil_dict(ol) == {11: [0, 3], 22: [1], 33: [2], 44: [4], 55: [5]})

#def ivdict(ol):
from xlist.desc import ivdict
ol = [11,22,33,11,44,55]
assert(ivdict(ol) =={0: 11, 1: 22, 2: 33, 3: 11, 4: 44, 5: 55})



#def vidict(arr):
from xlist.desc import vidict
assert(vidict(ol) == {11: 3, 22: 1, 33: 2, 44: 4, 55: 5})

#def mirror_dict(arr):
from xlist.desc import mirror_dict
md = mirror_dict(ol)
assert(md == {0: 11, 11: 3, 1: 22, 22: 1, 2: 33, 33: 2, 3: 11, 4: 44, 44: 4, 5: 55, 55: 5})

#def table(l,**kwargs):
from xlist.desc import table
tbl = table(ol)
assert(tbl = [{'index': 0, 'value': 11}, {'index': 1, 'value': 22}, {'index': 2, 'value': 33}, {'index': 3, 'value': 11}, {'index': 4, 'value': 44}, {'index': 5, 'value': 55}])




