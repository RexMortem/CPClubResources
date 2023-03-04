def OptimalSolution(x,y,z,n):
    List = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k != n)] # Using fundamentals of list comprehension, fast 
    
    print(List)

def OverComplicatedSolution(x,y,z,n):
    List = [[i//((y+1)*(z+1)), (i % ((y+1)*(z+1)))//(z+1), (i % ((y+1)*(z+1)))%(z+1)] for i in range((x+1)*(y+1)*(z+1)) if ((i//((y+1)*(z+1))) + (i % ((y+1)*(z+1)))//(z+1)+  (i % ((y+1)*(z+1)))%(z+1)) != n] # derived from numbers, and getting digits from the numbers (e.g. base 2 is x=1,y=1,z=1)

    print(List)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    OptimalSolution(x,y,z,n)
