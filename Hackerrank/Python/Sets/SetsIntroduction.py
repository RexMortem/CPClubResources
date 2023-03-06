def average(array):
    # your code goes here
    Set = set(array) # eliminates duplicates
    
    return sum(Set)/len(Set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
