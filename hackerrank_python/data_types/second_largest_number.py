n = int(raw_input())
value= []
value = map(int, raw_input().split(" "))
largestValue = max(value)
while max(value) == largestValue:
    value.remove(largestValue)
print max(value)