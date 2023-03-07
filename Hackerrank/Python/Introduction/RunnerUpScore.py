if __name__ == '__main__': # a lot of different ways to do it 
    n = int(input())
    arr = list(map(int, input().split()))
    
    Greatest = max(arr)
    
    Others = [x for x in arr if x != Greatest]
    
    print(max(Others))

