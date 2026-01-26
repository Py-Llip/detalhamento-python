c = {frozenset([1, 2]), frozenset([1,2,3,4,5])}
print(c)
for i in c:
    print(c | i)