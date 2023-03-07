# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(T):
    input()
    A = set(map(int, input().split()))
    input()
    B = set(map(int, input().split()))
    
    if A.issubset(B):
        print(True)
    else:
        print(False)
    
