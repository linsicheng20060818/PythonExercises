word=input(">")
b=""
list=[]
word=word+" "
for i in range(len(word)):
    if not word[i]==" ":
        b=b+word[i]
    else:
        if not b=="":
            list.append(b)
        b=""
for i in range(0,len(list)-1):
    if list[i]==' ':
        del list[i]
print(list)