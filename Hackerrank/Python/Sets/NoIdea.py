# Enter your code here. Read input from STDIN. Print output to STDOUT

input() # discard integers because not needed 
Array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

Happiness = 0

for Element in Array:
    if Element in A:
        Happiness += 1
        
    if Element in B:
        Happiness -= 1

print(Happiness)
