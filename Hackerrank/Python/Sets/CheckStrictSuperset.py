# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(input().split())
N = int(input())

IsStrictSuperset = True

for i in range(N):
    x = set(input().split())
    
    if not (A.issuperset(x) and (A != x)) :
        IsStrictSuperset = False
        break
    
print(IsStrictSuperset)
