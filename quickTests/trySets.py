list1 = []
a = tuple(['a', 1])
b = tuple(['b', 2])
c = tuple(['c', 3])
d = tuple(['d', 2])
e = tuple(['e', 1])
list1.append(b)
list1.append(a)
list1.append(d)
list1.append(e)
list1.append(c)
list1=[('world', 0.10034333188799373), ('hello', 0.0)]
list1.sort(key=lambda x:x[1])
print(list1)