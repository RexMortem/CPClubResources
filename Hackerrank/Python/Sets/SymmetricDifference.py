# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
A = set(map(int, input().split()))
input()
B = set(map(int, input().split()))

# multiple ways of achieving this, I will do union of differences 

DifferenceInts = A.difference(B).union(B.difference(A))
DifferenceInts = sorted(DifferenceInts)

for x in DifferenceInts:
    print(x)
