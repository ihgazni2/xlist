import xlist


#def mapfivo(ol,map_funcs,map_func_other_args_array,**kwargs):

#def mapfiv(ol,map_funcs,*other_args,**kwargs):

#def mapfio(ol,map_funcs,map_func_other_args_array,**kwargs):

#def mapfvo(ol,map_funcs,map_func_other_args_array,**kwargs):

#def mapivo(ol,map_func,map_func_other_args_array,**kwargs):

#def mapfio(ol,map_funcs,map_func_other_args_array,**kwargs):

#def mapfi(ol,map_funcs,*other_args,**kwargs):

#def mapfv(ol,map_funcs,*other_args,**kwargs):

#def mapfo(ol,map_funcs,map_func_other_args_array,**kwargs):

#def mapiv(ol,map_func,*other_args,**kwargs):
ol = [11,22,33,44,55]
def map_func(index,value,*other_args):
    return({
        "index":index,
        "value":value,
        "other_args":other_args
    })


nl = xlist.map.mapiv(ol,map_func,'x','y','z')
assert(nl==
    [
        {'index': 0, 'value': 11, 'other_args': ('x', 'y', 'z')}, 
        {'index': 1, 'value': 22, 'other_args': ('x', 'y', 'z')}, 
        {'index': 2, 'value': 33, 'other_args': ('x', 'y', 'z')}, 
        {'index': 3, 'value': 44, 'other_args': ('x', 'y', 'z')}, 
        {'index': 4, 'value': 55, 'other_args': ('x', 'y', 'z')}
    ]
)


#def mapio(ol,map_func,map_func_other_args_array,**kwargs):

#def mapvo(ol,map_func,map_func_other_args_array,**kwargs):
ol = [11,22,33,44,55]

map_func_other_args_array = [
    ['a','a','a'],
    ['b','b','b'],
    ['c','c','c'],
    ['d','d','d'],
    ['e','e','e'],
]

def map_func(value,*other_args):
    return("-".join([str(value)]+list(other_args)))

nl = xlist.map.mapvo(ol,map_func,map_func_other_args_array)
assert(nl == ['11-a-a-a', '22-b-b-b', '33-c-c-c', '44-d-d-d', '55-e-e-e'])

#def mapf(ol,map_funcs,*other_args,**kwargs):
ol = [11,22,33,44,55]
map_funcs = [
    lambda o:o+2,
    lambda o:o-2,
    lambda o:o*2,
    lambda o:o/2,
    lambda o:o%2
]
nl = xlist.map.mapf(ol,map_funcs,100)
assert(nl == [102, 98, 200, 50.0, 0])

#def mapi(ol,map_func,*other_args,**kwargs):

from xlist.map import mapi
ol = [11,22,33,44,55]
def map_func(index,p0,p1):
    return(p0+str(index) + p1)

nl = xlist.map.mapi(ol,map_func,'<','>')
assert(nl == ['<0>', '<1>', '<2>', '<3>', '<4>'])
assert(id(nl) != id(ol))
nl = xlist.map.mapv(ol,map_func,'<','>',deepcopy=False)
assert(id(nl) == id(ol))

#def mapv(ol,map_func,*other_args,**kwargs):
from xlist.map import mapv
ol = [11,22,33,44,55]
def map_func(value,p0,p1):
    return(p0+str(value) + p1)

nl = xlist.map.mapv(ol,map_func,'<','>')
assert(nl == ['<11>', '<22>', '<33>', '<44>', '<55>'])
assert(id(nl) != id(ol))
nl = xlist.map.mapv(ol,map_func,'<','>',deepcopy=False)
assert(id(nl) == id(ol))

#def mapo(ol,map_func,map_func_other_args_array,**kwargs):

from xlist.map import mapv
ol = [1,2,3,4,5]
map_func_other_args_array = [
    ['a','a','a'],
    ['b','b','b'],
    ['c','c','c'],
    ['d','d','d'],
    ['e','e','e'],
]
def map_func(*other_args):
    return("-".join(other_args))

nl = xlist.map.mapo(ol,map_func,map_func_other_args_array)
assert(nl == ['a-a-a', 'b-b-b', 'c-c-c', 'd-d-d', 'e-e-e'])



#def mapiv_with_dual(ol,map_func,index_map_func,map_func_other_args,index_map_func_other_args,**kwargs):

#def for_eachfivo(ol,for_each_funcs,for_each_func_other_args_array):
#def for_eachfiv(ol,for_each_funcs,*other_args):
#def for_eachfio(ol,for_each_funcs,for_each_func_other_args_array):
#def for_eachfvo(ol,for_each_funcs,for_each_func_other_args_array):
#def for_eachivo(ol,for_each_func,for_each_func_other_args_array):
#def for_eachfio(ol,for_each_funcs,for_each_func_other_args_array):
#def for_eachfi(ol,for_each_funcs,*other_args):
#def for_eachfv(ol,for_each_funcs,*other_args):
#def for_eachfo(ol,for_each_funcs,for_each_func_other_args_array):
#def for_eachiv(ol,for_each_func,*other_args):
ol = [11,22,33,44,55]
def map_func(index,value,*other_args):
    return({
        "index":index,
        "value":value,
        "other_args":other_args
    })


xlist.map.for_eachiv(ol,map_func,'x','y','z')
assert(ol==
    [
        {'index': 0, 'value': 11, 'other_args': ('x', 'y', 'z')}, 
        {'index': 1, 'value': 22, 'other_args': ('x', 'y', 'z')}, 
        {'index': 2, 'value': 33, 'other_args': ('x', 'y', 'z')}, 
        {'index': 3, 'value': 44, 'other_args': ('x', 'y', 'z')}, 
        {'index': 4, 'value': 55, 'other_args': ('x', 'y', 'z')}
    ]
)


#def for_eachio(ol,for_each_func,for_each_func_other_args_array):
#def for_eachvo(ol,for_each_func,for_each_func_other_args_array):
#def for_eachf(ol,for_each_funcs,*other_args):
#def for_eachi(ol,for_each_func,*other_args):
#def for_eachv(ol,for_each_func,*other_args):
#def for_eacho(ol,for_each_func,for_each_func_other_args_array):
#def for_eachiv_with_dual(ol,for_each_func,index_for_each_func,for_each_func_other_args,index_for_each_func_other_args):

#def intlize(ol):
from xlist.map import intlize
ol = ['11','22']
nl = intlize(ol)
assert(nl == [11,22])
#def strlize(ol):
from xlist.map import strlize
ol = [11,22]
nl = strlize(ol)
assert(nl == ['11','22'])


