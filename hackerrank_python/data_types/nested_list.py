n = int(input())
marks = []
for _ in range(0,n):
    marks.append([raw_input(),float(raw_input())])

second_higest_mark= sorted(list(set([name for mark, name in marks])))[1]
print '\n'.join(a for a, b in sorted(marks) if b==second_higest_mark)


# from operator import itemgetter
# n = int(raw_input())
# marks = []
# for i in xrange(n):
# 	marks.append([raw_input(),float(input())])
#
# marks_after_sort = sorted(marks, key= lambda marks:marks[1])
#
# print marks_set


# code from the hackerrank forum
# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([raw_input(), float(input())])
#
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
