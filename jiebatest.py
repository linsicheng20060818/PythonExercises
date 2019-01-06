# -*- coding: utf-8 -*-
import jieba
a=input(">")
print(", ".join(jieba.lcut(a)))
print(", ".join(jieba.lcut(a,cut_all=True)))
list1=jieba.cut_for_search(a)
print(', '.join(list1))