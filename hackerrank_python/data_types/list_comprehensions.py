X,Y,Z,N = (int(input()) for _ in range(4))
print([[a,b,c] for a in range(X+1) for b in range(Y+1) for c in range(Z+1) if a+b+c != N])
# X = int(raw_input())
# Y = int(raw_input())
# Z = int(raw_input())
# N = int(raw_input())
#
# value =[]
# for x in range(0,X+1):
#     for y in range(0,Y+1):
#         for z in range(0,Z+1):
#             if x+y+z != N:
#                 value.append([x,y,z])
#
# print(value)