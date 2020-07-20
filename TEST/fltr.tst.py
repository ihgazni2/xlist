#def fltrfivo(ol,fltr_funcs,fltr_func_other_args_array):

#def fltrfiv(ol,fltr_funcs,*other_args):

#def fltrfio(ol,fltr_funcs,fltr_func_other_args_array):

#def fltrfvo(ol,fltr_funcs,fltr_func_other_args_array):

#def fltrivo(ol,fltr_func,fltr_func_other_args_array):

#def fltrfio(ol,fltr_funcs,fltr_func_other_args_array):

#def fltrfi(ol,fltr_funcs,*other_args):

#def fltrfv(ol,fltr_funcs,*other_args):

#def fltrfo(ol,fltr_funcs,fltr_func_other_args_array):

#def fltriv(ol,fltr_func,*other_args):
from xlist.fltr import fltriv
ol = [11,22,33,44,55,66]
nl = fltriv(ol,lambda i,v:(i%3!=0) and  (v%3!=1))
assert(nl == [33,66])


#def fltrio(ol,fltr_func,fltr_func_other_args_array):

#def fltrvo(ol,fltr_func,fltr_func_other_args_array):


#def fltrf(ol,fltr_funcs,*other_args):
from xlist.fltr import fltrf
ol = [11,22,33]
fltr_funcs = [
    lambda a,b,c:a>0,
    lambda a,b,c:b==0,
    lambda a,b,c:c<0
]
nl = fltrf(ol,fltr_funcs,2,2,-2)
assert(nl == [11,33])



#def fltri(ol,fltr_func,*other_args):
from xlist.fltr import fltri
ol = [11,22,33,44,55,66]
nl = fltri(ol,lambda i:i%3==0)
assert(nl == [11,44])


#def fltrv(ol,fltr_func,*other_args):
from xlist.fltr import fltrv
ol = [11,22,33,44,55,66]
nl = fltrv(ol,lambda r:r%2==0)
assert(nl == [22, 44, 66])



#def fltro(ol,fltr_func,fltr_func_other_args_array):

#def fltriv_with_dual(ol,fltr_func,index_fltr_func,fltr_func_other_args,index_fltr_func_other_args):
