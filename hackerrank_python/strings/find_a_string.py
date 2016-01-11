# stringValue = str(raw_input())
# substringValue = str(raw_input())
stringValue = str(raw_input())
substringValue = str(raw_input())
count = 0 
for i in range(0,len(stringValue)):
	if [ord(c) for c in substringValue] == [ord(c) for c in stringValue[i:i+len(substringValue)]]:
		count += 1
print count
# print valueSubStringValue


# asciiValue.append(ord(c) for c in stringValue)
# print asciiValue

# for i in range(0,len(stringValue)):
# 	print [ord(c) for c in (stringValue[i])]
# 	if cmp([ord(c) for c in (stringValue[i:len(substringValue)])],[ord(c) for c in (substringValue)]):
# 		count += 1
# print count

# print [ord(c) for c in (stringValue[1:len(substringValue)])]

# for i in range(0,len(stringValue)):
# 	if ord(substringValue) == ord(stringValue[i:len(substringValue)])
# 	count += 1
# print count