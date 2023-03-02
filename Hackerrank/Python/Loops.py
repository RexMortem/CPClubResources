# Requires knowledge of for loops OR while loops
# while loops are better for beginners as it builds logical thinking
# for loops are faster to write in this case 

def WhileLoop(n):
    i = 0
    
    while i < n:
        print(i*i) # one way of doing the square
        i += 1 # useful syntax to cover
        
        
def ForLoop(n):
    for i in range(n):
        print(i**2) # power way of doing the square 

if __name__ == '__main__':
    n = int(input())
    
    WhileLoop(n)
