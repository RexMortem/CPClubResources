# Enter your code here. Read input from STDIN. Print output to STDOUT

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
