def extendList(val,list=[]):
    list.append(val)
    return list


list1=extendList(10) # list1=[10] 坑点
list2=extendList(123,[]) #list2=[123]
list3=extendList('a') # list1和list3的内存地址是同一个 [10,'a']
print("list1=%s"%list1)
print("list2=%s"%list2)
print("list3=%s"%list3)