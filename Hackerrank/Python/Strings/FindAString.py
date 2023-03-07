def count_substring(string, sub_string):
    n = 0
    p = 0
    
    while p < len(string):
        i = string.find(sub_string, p)
        
        if i == -1:
            break 
        
        p = i + 1
        n += 1 
    
    return n

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
