# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    N = int(input())
    CS = set()
    
    for i in range(N):
        CS.add(input())
        
    print(len(CS))
