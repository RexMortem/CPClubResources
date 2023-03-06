# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
English = set(map(int, input().split()))
input()
French = set(map(int, input().split()))

print(len(English.intersection(French)))
