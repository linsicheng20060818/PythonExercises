# -*- coding: utf-8 -*-
def Enfc0(a):
    import jieba
    list1=jieba.lcut(a)
    list2=[]
    for i in range(len(list1)):
        if list1[i]!=" ":
            list2.append(list1[i])
    return(list2)