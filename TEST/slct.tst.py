import xlist


import xlist.slct

#xlist.slct.some
#def some(ol,*indexes):
#def some_keeping_order(ol,*indexes):
ol = [10,11,12,13,14,15,16]
subl = xlist.slct.some(ol,2,5)
assert(subl == [12,15])

#xlist.slct.not_some
#def not_some(ol,*indexes):
ol = [10,11,12,13,14,15,16]
subl = xlist.slct.not_some(ol,2,5)
assert(subl == [10, 11, 13, 14, 16])


#
#def car(ol):
assert(xlist.slct.car(ol) == 10)
#def cdr(ol):
assert(xlist.slct.cdr(ol) == [11, 12, 13, 14, 15, 16])
#def head(ol):
assert(xlist.slct.head(ol) == 10)
#def tail(ol):
assert(xlist.slct.tail(ol) == [11, 12, 13, 14, 15, 16])
#def init(ol):
assert(xlist.slct.init(ol) == [10, 11, 12, 13, 14, 15])
#def last(ol):
assert(xlist.slct.last(ol) == 16)
#def preceding(ol,index):
assert(xlist.slct.preceding(ol,3) == [10, 11, 12])
#def following(ol,index):
assert(xlist.slct.following(ol,3) == [14, 15, 16])
#def range(ol,si,ei):
assert(xlist.slct.via_range(ol,1,3) == [11,12])
#def odds(ol):
assert(xlist.slct.odds(ol) == [11,13,15])
#def evens(ol):
assert(xlist.slct.evens(ol) == [10, 12, 14, 16])
#def interval(ol,interval,**kwargs):
assert(xlist.slct.interval(ol,3) == [10, 13, 16])



