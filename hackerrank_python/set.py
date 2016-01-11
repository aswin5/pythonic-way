# myset = {1,2}
# for item in myset:
#     print item
a = int(raw_input())
myset1 = set(map(int,raw_input().split(" ")))
b = int(raw_input())
myset2 = set(map(int,raw_input().split(" ")))
answer = myset1.symmetric_difference(myset2)
values=sorted(answer)
for item in values:
    print item
# print "".join(set(x) for x in xrange(len(answer)) )