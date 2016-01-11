N, M = map(int,raw_input().split()) 
for i in xrange(0,N/2):
	print ('.|.'*i).rjust((M-2)/2, '-')+'.|.'+('.|.' *i).ljust((M-2)/2, '-')
print 'WELCOME'.center(M,'-')
for i in reversed(xrange(0,N/2)):
	print ('.|.'*i).rjust((M-2)/2, '-')+'.|.'+('.|.'*i).ljust((M-2)/2, '-')
    # print ('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')
# print 'WELCOME'.center(M,'-')
# for i in reversed(xrange(0,N/2)): 
#     print ('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')


# midValue = '.|.'
# mulValue = 1
# for i in xrange(n):
# 	if i <n/2:
# 		valueofMid = midValue*mulValue
# 		mulValue += 2
# 		print valueofMid.center(m,'-')
# 	if i == n/2:
# 		print 'welcome'.center(m,'-')
# 	if i > n/2:
# 		mulValue -= 2
# 		valueofMid = midValue*mulValue
# 		print valueofMid.center(m,'-')