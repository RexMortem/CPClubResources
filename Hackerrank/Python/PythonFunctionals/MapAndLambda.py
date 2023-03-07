cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    Numbers = [0, 1]
    
    if n == 1:
        return [0]
    elif n == 0:
        return []
    
    i = 2
    
    while i < n:
        Numbers.append(Numbers[i-1] + Numbers[i-2])
        i += 1 
        
    return Numbers
        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
