stringValue = str(raw_input())
substringValue = str(raw_input())
count = 0 
for i in range(0,len(stringValue)):
	if [ord(c) for c in substringValue] == [ord(c) for c in stringValue[i:i+len(substringValue)]]:
		count += 1
print count
