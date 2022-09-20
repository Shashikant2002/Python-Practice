# a = {4,2,3,1,5,1,5}
# print(a)

b = set()
print(type(b))
b.add((1,5,8))
b.add(7)
b.add(1)

print(len(b))

b.remove(1)
b.pop()
print(b)