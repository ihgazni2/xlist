.. contents:: Table of Contents
   :depth: 5


*xlist*
------------

- list utils

Installation
============

    ::
    
        $ pip3 install xlist

Usage
=====
    
    ::
        


APIS
====


slct
~~~~
- def some(ol,*indexes):
- def some_keeping_order(ol,*indexes):
- def not_some(ol,*indexes):
- def car(ol):
- def cdr(ol):
- def head(ol):
- def tail(ol):
- def init(ol):
- def last(ol):
- def preceding(ol,index):
- def following(ol,index):
- def via_range(ol,si,ei):
- def odds(ol):
- def evens(ol):
- def interval(ol,interval,**kwargs):


init
~~~~
- def init(lngth,*args,**kwargs):
- def from_range(si,ei,step=1):
- def fill(ol,value,si=None,ei=None,**kwargs):
- def lfrom(obj,*args,**kwargs):
- def of(*eles):

index
~~~~~
- def uniform_index(index,lngth):
- def index_fst(ol,value):
- def index_fst_not(ol,value):
- def index_lst(ol,value):
- def index_lst_not(ol,value):
- def index_which(ol,value,which):
- def index_which_not(ol,value,which):
- def indexes_all(ol,value):
- def indexes_all_not(ol,value):
- def indexes_some(ol,value,*seqs):
- def indexes_some_not(ol,value,*seqs):
- def indexes_fst_slice(ol,value):
- def indexes_fst_not_slice(ol,value):
- def indexes_lst_slice(ol,value):
- def indexes_lst_not_slice(ol,value):
- def indexes_which_slice(ol,value):
- def indexes_which_not_slice(ol,value):
- def indexes_some_slices(ol,value,*seqs):
- def indexes_some_not_slices(ol,value,*seqs):
- def indexes_all_slices(ol,value):
- def indexes_all_not_slices(ol,value):

map
~~~
- def mapfivo(ol,map_funcs,map_func_other_args_array):
- def mapfiv(ol,map_funcs,*other_args):
- def mapfio(ol,map_funcs,map_func_other_args_array):
- def mapfvo(ol,map_funcs,map_func_other_args_array):
- def mapivo(ol,map_func,map_func_other_args_array):
- def mapfio(ol,map_funcs,map_func_other_args_array):
- def mapfi(ol,map_funcs,*other_args):
- def mapfv(ol,map_funcs,*other_args):
- def mapfo(ol,map_funcs,map_func_other_args_array):
- def mapiv(ol,map_func,*other_args):
- def mapio(ol,map_func,map_func_other_args_array):
- def mapvo(ol,map_func,map_func_other_args_array):
- def mapf(ol,map_funcs,*other_args):
- def mapi(ol,map_func,*other_args):
- def mapv(ol,map_func,*other_args):
- def mapo(ol,map_func,map_func_other_args_array):
- def mapiv_with_dual(ol,map_func,index_map_func,*map_func_other_args,*index_map_func_other_args):
- def for_eachfivo(ol,for_each_funcs,for_each_func_other_args_array):
- def for_eachfiv(ol,for_each_funcs,*other_args):
- def for_eachfio(ol,for_each_funcs,for_each_func_other_args_array):
- def for_eachfvo(ol,for_each_funcs,for_each_func_other_args_array):
- def for_eachivo(ol,for_each_func,for_each_func_other_args_array):
- def for_eachfio(ol,for_each_funcs,for_each_func_other_args_array):
- def for_eachfi(ol,for_each_funcs,*other_args):
- def for_eachfv(ol,for_each_funcs,*other_args):
- def for_eachfo(ol,for_each_funcs,for_each_func_other_args_array):
- def for_eachiv(ol,for_each_func,*other_args):
- def for_eachio(ol,for_each_func,for_each_func_other_args_array):
- def for_eachvo(ol,for_each_func,for_each_func_other_args_array):
- def for_eachf(ol,for_each_funcs,*other_args):
- def for_eachi(ol,for_each_func,*other_args):
- def for_eachv(ol,for_each_func,*other_args):
- def for_eacho(ol,for_each_func,for_each_func_other_args_array):
- def for_eachiv_with_dual(ol,for_each_func,index_for_each_func,*for_each_func_other_args,*index_for_each_func_other_args):
- def intlize(ol):
- def strlize(ol):  

fltr
~~~~
- def fltrfivo(ol,fltr_funcs,fltr_func_other_args_array):
- def fltrfiv(ol,fltr_funcs,*other_args):
- def fltrfio(ol,fltr_funcs,fltr_func_other_args_array):
- def fltrfvo(ol,fltr_funcs,fltr_func_other_args_array):
- def fltrivo(ol,fltr_func,fltr_func_other_args_array):
- def fltrfio(ol,fltr_funcs,fltr_func_other_args_array):
- def fltrfi(ol,fltr_funcs,*other_args):
- def fltrfv(ol,fltr_funcs,*other_args):
- def fltrfo(ol,fltr_funcs,fltr_func_other_args_array):
- def fltriv(ol,fltr_func,*other_args):
- def fltrio(ol,fltr_func,fltr_func_other_args_array):
- def fltrvo(ol,fltr_func,fltr_func_other_args_array):
- def fltrf(ol,fltr_funcs,*other_args):
- def fltri(ol,fltr_func,*other_args):
- def fltrv(ol,fltr_func,*other_args):
- def fltro(ol,fltr_func,fltr_func_other_args_array):
- def fltriv_with_dual(ol,fltr_func,index_fltr_func,*fltr_func_other_args,*index_fltr_func_other_args):


find
~~~~
- def find_fst_iv(ol,test_func,*args):
- def find_fst_v(ol,test_func,*args):
- def find_fst_i(ol,test_func,*args):
- def find_fst_not_iv(ol,test_func,*args):
- def find_fst_not_v(ol,test_func,*args):
- def find_fst_not_i(ol,test_func,*args):
- def find_lst_iv(ol,test_func,*args):
- def find_lst_i(ol,test_func,*args):
- def find_lst_v(ol,test_func,*args):
- def find_lst_not_iv(ol,test_func,*args):
- def find_lst_not_i(ol,test_func,*args):
- def find_lst_not_v(ol,test_func,*args):
- def find_which_iv(ol,test_func,which,*args):
- def find_which_i(ol,test_func,which,*args):
- def find_which_v(ol,test_func,which,*args):
- def find_which_not_iv(ol,test_func,which,*args):
- def find_which_not_i(ol,test_func,which,*args):
- def find_which_not_v(ol,test_func,which,*args):
- def find_some_iv(ol,test_func,*seqs,**kwargs):
- def find_some_i(ol,test_func,*seqs,**kwargs):
- def find_some_v(ol,test_func,*seqs,**kwargs):
- def find_some_not_iv(ol,test_func,*seqs,**kwargs):
- def find_some_not_i(ol,test_func,*seqs,**kwargs):
- def find_some_not_v(ol,test_func,*seqs,**kwargs):
- def find_all_iv(ol,test_func,*args):
- def find_all_i(ol,test_func,*args):
- def find_all_v(ol,test_func,*args):
- def find_all_not_iv(ol,test_func,*args):
- def find_all_not_i(ol,test_func,*args):
- def find_all_not_v(ol,test_func,*args):
- def find_fst_gt_iv(ol,value):
- def find_fst_gt_i(ol,value):
- def find_fst_gt_v(ol,value):
- def find_lst_gt_iv(ol,value):
- def find_lst_gt_i(ol,value):
- def find_lst_gt_v(ol,value):
- def find_which_gt_iv(ol,value):
- def find_which_gt_i(ol,value):
- def find_which_gt_v(ol,value):
- def find_some_gt_iv(ol,value,*seqs):
- def find_some_gt_i(ol,value,*seqs):
- def find_some_gt_v(ol,value,*seqs):
- def find_all_gt_iv(ol,value):
- def find_all_gt_i(ol,value):
- def find_all_gt_v(ol,value):
- def find_fst_lt_iv(ol,value):
- def find_fst_lt_i(ol,value):
- def find_fst_lt_v(ol,value):
- def find_lst_lt_iv(ol,value):
- def find_lst_lt_i(ol,value):
- def find_lst_lt_v(ol,value):
- def find_which_lt_iv(ol,value):
- def find_which_lt_i(ol,value):
- def find_which_lt_v(ol,value):
- def find_some_lt_iv(ol,value,*seqs):
- def find_some_lt_i(ol,value,*seqs):
- def find_some_lt_v(ol,value,*seqs):
- def find_all_lt_iv(ol,value):
- def find_all_lt_i(ol,value):
- def find_all_lt_v(ol,value):
- def find_fst_eq_iv(ol,value):
- def find_fst_eq_i(ol,value):
- def find_fst_eq_v(ol,value):
- def find_lst_eq_iv(ol,value):
- def find_lst_eq_i(ol,value):
- def find_lst_eq_v(ol,value):
- def find_which_eq_iv(ol,value):
- def find_which_eq_i(ol,value):
- def find_which_eq_v(ol,value):
- def find_some_eq_iv(ol,value,*seqs):
- def find_some_eq_i(ol,value,*seqs):
- def find_some_eq_v(ol,value,*seqs):
- def find_all_eq_iv(ol,value):
- def find_all_eq_i(ol,value):
- def find_all_eq_v(ol,value):



desc
~~~~
- def vil_dict(l):
- def ivdict(ol):
- def vidict(arr):
- def mirror_dict(arr):
- def table(l,**kwargs):



util
~~~~
- def fcp(ol):

cmmn
~~~~
- def deepcopy_wrapper(func):
- def keep_ptr_replace(ol,nl):
- def inplace_wrapper(func):
- def identity(obj):
- def dflt_kwargs(k,dflt,**kwargs):


License
=======

- MIT
