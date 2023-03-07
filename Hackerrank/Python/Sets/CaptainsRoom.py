# There's a way to do this using Counter module
# There is a way to do this with list comprehension (hint: count(x) in an array gives you number of occurrences of x in array)
# There is a way to do this mathematically involving the sum of the set, and the sum of the list

K = int(input())
RoomNumbers = map(int, input().split())

OneOccurrenceSet = set()
MoreOccurencesSet = set()

for x in RoomNumbers:
    if x in OneOccurrenceSet:
        MoreOccurencesSet.add(x)
    else:
        OneOccurrenceSet.add(x)
        
print((OneOccurrenceSet.difference(MoreOccurencesSet)).pop())
