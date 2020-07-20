

#xlist.init.init
from xlist.init import init
ol = init(5)
assert(ol == [None, None, None, None, None])
d = {}
ol = init(5,d)
assert(id(d) != id(ol[0]))
ol = init(5,d,deepcopy=False)
assert(id(d) == id(ol[0]))



#xlist.init.from_range
from xlist.init import from_range
ol = from_range(1,8,3)
assert(ol == [1,4,7])




#xlist.init.fill
from xlist.init import fill
ol = [0,1,2,3,4,5]
nl = fill(ol,999,1,3)
assert(nl == [0, 999, 999, 3, 4, 5])
assert(id(nl) != id(ol))
nl = fill(ol,999,1,3,deepcopy=False)
assert(id(nl) == id(ol))


#xlist.init.lfrom
from xlist.init import lfrom
ol = [0,1,2,3,4,5]
nl = lfrom(ol,lambda el:el*2)
assert(nl == [0, 2, 4, 6, 8, 10])

def map_func(value,index,*args):
    return(args[0]+str(index)+':'+str(value)+args[1])

nl = lfrom(ol,map_func,'<','>')
assert(nl == ['<0:0>', '<1:1>', '<2:2>', '<3:3>', '<4:4>', '<5:5>'])

def map_func(value,**kwargs):
    return(kwargs['name']+':'+str(value))

nl = lfrom(ol,map_func,name='value')
assert(nl == ['value:0', 'value:1', 'value:2', 'value:3', 'value:4', 'value:5'])



#xlist.init.of
from xlist.init import of
nl = of(1,2,3,4)
assert(nl == [1,2,3,4])



