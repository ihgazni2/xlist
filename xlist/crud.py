from .cmmn import inplace_wrapper

@inplace_wrapper
def append(ol,ele,**kwargs):
    ol.append(ele)
    return(ol)


@inplace_wrapper
def push(ol,ele,**kwargs):
    ol.append(ele)
    return(ol)


@inplace_wrapper
def append_some(ol,*eles,**kwargs):
    return(extend(ol,list(eles),**kwargs))


@inplace_wrapper
def prepend(ol,ele,**kwargs):
    new = [ele]
    new.extend(ol)
    return(new)


@inplace_wrapper
def extend(ol,nl,**kwargs):
    ol.extend(nl)
    return(ol)

@inplace_wrapper
def prextend(ol,nl,**kwargs):
    nl.extend(ol)
    return(nl)

@inplace_wrapper
def prepend_some(ol,*eles,**kwargs):
    return(prextend(ol,list(eles),**kwargs))


@inplace_wrapper
def unshift(ol,*eles,**kwargs):
    return(prextend(ol,list(eles),**kwargs))


@inplace_wrapper
def concat(*arrays,**kwargs):
    new = []
    length = arrays.__len__()
    for i in range(0,length):
        array = arrays[i]
        new.extend(array)
    return(new)

@inplace_wrapper
def cons(head_ele,l,**kwargs):
    return(prepend(l,head_ele,**kwargs))


