# -*- coding: utf-8 -*-
"""try:
    import jieba
except:
    print("please install jieba first.")
    input("press any key to continue")
    quit()"""
def chchat(a):
    import jieba
    v=False
    '''if a=="quit" or a=="exit" or a=="退出" or a=="再见":
        import os
        exit()'''
    list1=jieba.lcut(a)#jieba分词
    #print(list1)
    i=0
    b=""
    r=0
    if list1[i]=="你好":#如果是打招呼，直接输出
       return(a)
    else:
        ni=[]
        wo=[]
        for i in range(len(list1)):#判断 '你'和'我'
            if list1[i]=="你":
                 ni.append(i)
            if list1[i]=="我":
                 wo.append(i)
            if list1[i]=="几":
                import random
                v=True
        for r in range(len(ni)):#'你'换成'我'
            list1[r]="我"
        for i in range(len(wo)):#'我'换成'你'
            list1[i]="你"
        for i in range(len(list1)):
            b=b+list1[i]
        if v==True:
            return(random.randint(-10,2000))
        else:
            return((b.replace("吗","").replace("?","!")).replace("？","！"))