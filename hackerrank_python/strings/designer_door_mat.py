N, M = map(int,raw_input().split()) 
for i in xrange(0,N/2):
	print ('.|.'*i).rjust((M-2)/2, '-')+'.|.'+('.|.' *i).ljust((M-2)/2, '-')
print 'WELCOME'.center(M,'-')
for i in reversed(xrange(0,N/2)):
	print ('.|.'*i).rjust((M-2)/2, '-')+'.|.'+('.|.'*i).ljust((M-2)/2, '-')
