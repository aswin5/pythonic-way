n = int(int(raw_input()))
width = len("{0:b}".format(n))
for i in xrange(1,n+1):
  print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)




# for i in range(1,18):
# 	value = [i, format(i, 'o'), format(i, 'x'), format(i, 'b')]
# 	print '  '.join(str(x) for x in value)