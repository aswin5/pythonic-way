value = raw_input()
answer = {'alnum':False, 'alpha':False, 'digit':False, 'lower':False, 'upper':False}
for x in xrange(5):
    for i in xrange(len(value)):
        if answer['alnum']==False:
            answer['alnum']=value[i].isalnum()
        if answer['alpha']==False:
            answer['alpha']=value[i].isalpha()
        if answer['digit']==False:
            answer['digit']=value[i].isdigit()
        if answer['lower']==False:
            answer['lower']=value[i].islower()
        if answer['upper']==False:
            answer['upper']=value[i].isupper()

print answer['alnum']
print answer['alpha']
print answer['digit']
print answer['lower']
print answer['upper']