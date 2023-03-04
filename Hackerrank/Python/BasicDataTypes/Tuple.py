if __name__ == '__main__': # unfortunately, the problem is broken and only works in PyPy 3
    n = int(input())
    integer_list = map(int, input().split())
    
    print(hash(tuple(integer_list)))
