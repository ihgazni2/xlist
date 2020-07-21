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
- def from_one_list(ol,*args,**kwargs):


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
- def el2iteml(el,k):
- def el2attrl(el,attr):
- def reduce_left(ol,callback,initialValue):
- def reduce_right(ol,callback,initialValue):


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
- def lngth_lt(ol,lngth):
- def lngth_le(ol,lngth):
- def lngth_eq(ol,lngth):
- def lngth_ge(ol,lngth):
- def lngth_gt(ol,lngth):

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
- def vil_dict_after_vtrans(l,*other_args,trans_func=lambda r:r):


sarr
~~~~
- def fltrv_via_loose_in(arr,k):
- def is_loose_in(arr,k):
- def fltrv_via_loose_contain(arr,k):
- def is_loose_contain(arr,k):
- def fltrv_via_regex_match(arr,regex):
- def is_regex_match(arr,regex):
- def lcstr(s0,s1):


getset
~~~~~~
- def get_via_pl(ol,pathlist):
- def get_via_pl2(pathlist,ol):
- def get_via_sibseqs(ol,*sibseqs):
- def set_via_pl(ol,pathlist,value):
- def set_via_sibseqs(ol,value,*sibseqs):
- def del_via_pl(ol,pathlist):
- def del_via_sibseqs(ol,*sibseqs):
- def set_via_il_vl(ol,indexes,values):
- def set_via_ivlist(ol,*iv_tuples):
- def pl_to_bracket_str(path_list):
- def bracket_str_to_pl(gs):

crud
~~~~
- def append(ol,ele,**kwargs):
- def push(ol,ele,**kwargs):
- def append_some(ol,*eles,**kwargs):
- def prepend(ol,ele,**kwargs):
- def extend(ol,nl,**kwargs):
- def prextend(ol,nl,**kwargs):
- def prepend_some(ol,*eles,**kwargs):
- def unshift(ol,*eles,**kwargs):
- def concat(*arrays,**kwargs):
- def cons(head_ele,l,**kwargs):
- def insert(ol,start_index,ele,**kwargs):
- def insert_some(ol,start_index,*eles,**kwargs):
- def insert_many(ol,eles,locs,**kwargs):
- def insert_section(ol,sec,loc,**kwargs):
- def insert_sections_some(ol,*secs,**kwargs):
- def insert_sections_many(ol,secs,locs,**kwargs):
- def repeat_every(l,times):
- def apadding(l,lngth,val):
- def prepadding(l,lngth,val):
- def pop(ol,index,**kwargs):
- def shift(ol,**kwargs):
- def cond_pop(ol,index,**kwargs):
- def pop_range(ol,start_index,end_index,**kwargs):
- def pop_some(ol,*indexes,**kwargs):
- def another_pop_some(l,*seqs):
- def rm_fst(ol,value,**kwargs):
- def rm_fst_not(ol,value,**kwargs):
- def rm_lst(ol,value,**kwargs):
- def rm_lst_not(ol,value,**kwargs):
- def rm_which(ol,value,which,**kwargs):
- def rm_which_not(ol,value,which,**kwargs):
- def rm_some(ol,value,*seqs,**kwargs):
- def rm_some_not(ol,value,*seqs,**kwargs):
- def rm_all(ol,value,**kwargs):
- def rm_all_not(ol,value,**kwargs):
- def rm_many(ol,values,seqs,**kwargs):
- def rm_many_not(ol,values,seqs,**kwargs):
- def reverse(ol,**kwargs):
- def splice(ol,start,deleteCount,*eles,**kwargs):
- def interleave(*arrays,**kwargs):
- def deinterleave(ol,gnum):
- def split(ol,value,*whiches,**kwargs):
- def repl_some(ol,value,*indexes,**kwargs)
- def repl_some_eq(ol,src_value,dst_value,*seqs,**kwargs):
- def repl_fst_eq(ol,src_value,dst_value,**kwargs):
- def repl_lst_eq(ol,src_value,dst_value,**kwargs):
- def repl_which_eq(ol,src_value,dst_value,which,**kwargs):
- def repl_all_eq(ol,src_value,dst_value,**kwargs):
- def cond_repl_some(ol,cond_func,dst_value,*seqs,**kwargs):
- def cond_repl_which(ol,cond_func,dst_value,which,**kwargs):
- def cond_repl_fst(ol,cond_func,dst_value,**kwargs):
- def cond_repl_lst(ol,cond_func,dst_value,**kwargs):
- def cond_repl_all(ol,cond_func,dst_value,**kwargs):



range
~~~~~
- def compress(ol):
- def decompress(cl):
- def spanize(break_points,length):
- def fullfill_spans(spans,lngth):
- def get_supplement_of_spans(spans,lngth):
- def get_span_loc(spans,word_loc):
- def broke_via_seqs(ol,break_points):
- def broke_via_some(ol,*break_points):
- def where_index_interval(ol,value):
- def where_value_interval(ol,value):
- def upper_bound(ol,value):
- def lower_bound(ol,value):
- def chunk(ol,interval):


two
~~~
- def comprise(list1,list2,**kwargs):
- def diff_indexes(l1,l2):
- def diff_values(l1,l2):
- def same_indexes(l1,l2):
- def same_values(l1,l2):
- def intersection(ol1,ol2):
- def shorter(ol1,ol2):
- def longer(ol1,ol2):
- def ordered_intersection(ol1,ol2):
- def fullinfo_intersection(ol1,ol2,**kwargs):
- def union(ol1,ol2):
- def difference(ol1,ol2):
- def fst_cmmn_val_index(l0,l1,**kwargs):
- def fst_cmmn_val(l0,l1,**kwargs):



pair
~~~~
- def find_lst_ipair_when_fstltsnd(arr):
- def find_lst_vpair_when_fstltsnd(arr):
- def find_lst_ipair_when_fstgtsnd(arr):
- def find_lst_vpair_when_fstgtsnd(arr):



util
~~~~
- def fcp(ol):
- def max_length(ol):
- def entries(ol):
- def includes(ol,value):
- def to_str(ol):
- def to_src(ol):
- def every(ol,test_func,*args,**kwargs):
- def any(ol,test_func,*args,**kwargs):
- def combinations(arr,*args):

cmmn
~~~~
- def deepcopy_wrapper(func):
- def keep_ptr_replace(ol,nl):
- def inplace_wrapper(func):
- def identity(obj):
- def dflt_kwargs(k,dflt,**kwargs):


rand
~~~~
- def rand_some_indexes(si,ei,n,**kwargs):
- def rand_sub(arr,*args,**kwargs):


nest
~~~~
- class ListTree():
- ltree.ancestlize(           
- ltree.ancestor_paths(       
- ltree.ancestors(            
- ltree.cond_search(          
- ltree.depth                 
- ltree.desc                  
- ltree.descendant_paths(     
- ltree.descendants(          
- ltree.dig(                  
- ltree.flatWidth             
- ltree.flatten(              
- ltree.followingSibPaths(    
- ltree.followingSibs(        
- ltree.following_sib_paths(  
- ltree.following_sibs(       
- ltree.include(              
- ltree.lcin(                 
- ltree.lcin_path(            
- ltree.level(                
- ltree.list                  
- ltree.loc(                  
- ltree.loc2path(             
- ltree.locpath_mapping       
- ltree.lsib(                 
- ltree.lsib_path(            
- ltree.maxLevelWidth         
- ltree.nextSibPath(          
- ltree.nextSibling(          
- ltree.parent(               
- ltree.parent_path(          
- ltree.path(                 
- ltree.path2loc(             
- ltree.pathloc_mapping       
- ltree.precedingSibPaths(    
- ltree.precedingSibs(        
- ltree.preceding_sib_paths(  
- ltree.preceding_sibs(       
- ltree.prevSibPath(          
- ltree.prevSibling(          
- ltree.rcin(                 
- ltree.rcin_path(
- ltree.rsib(
- ltree.rsib_path(
- ltree.search(
- ltree.showlog
- ltree.showroute(
- ltree.sib_paths(
- ltree.sibs(
- ltree.someSibPaths(
- ltree.someSibs(
- ltree.some_sib_paths(
- ltree.some_sibs(
- ltree.son_paths(
- ltree.sons(
- ltree.total
- ltree.trace
- ltree.tree(
- ltree.whichSib(
- ltree.whichSibPath(
- ltree.which_sib(
- ltree.which_sib_path(

License
=======

- MIT
