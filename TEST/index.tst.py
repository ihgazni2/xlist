#def uniform_index(index,lngth):
from xlist.index import uniform_index
assert(uniform_index(0,3),0)
assert(uniform_index(-1,3),2)
assert(uniform_index(-4,3),0)
assert(uniform_index(-3,3),0)
assert(uniform_index(5,3),3)

from xlist.index import *
ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
#def index_fst(ol,value):
assert(index_fst(ol,'a')==1)
#def index_fst_not(ol,value):
assert(index_fst_not(ol,'a')==0)
#def index_lst(ol,value):
assert(index_lst(ol,'a') ==9)
#def index_lst_not(ol,value):
assert(index_lst_not(ol,'a') ==10)
#def index_which(ol,value,which):
#def index_which_not(ol,value,which):
#def indexes_all(ol,value):
#def indexes_all_not(ol,value):
#def indexes_some(ol,value,*seqs):
#def indexes_some_not(ol,value,*seqs):
#def indexes_fst_slice(ol,value):
assert(indexes_fst_slice(ol,'a') == [1,2])
#def indexes_fst_not_slice(ol,value):
assert(indexes_fst_not_slice(ol,'a') == [0])
#def indexes_lst_slice(ol,value):
#def indexes_lst_not_slice(ol,value):
#def indexes_which_slice(ol,value):
#def indexes_which_not_slice(ol,value):
#def indexes_some_slices(ol,value,*seqs):
#def indexes_some_not_slices(ol,value,*seqs):
#def indexes_all_slices(ol,value):
assert(indexes_all_slices(ol,'a') == [[1, 2], [5], [7, 8, 9]])
#def indexes_all_not_slices(ol,value):
