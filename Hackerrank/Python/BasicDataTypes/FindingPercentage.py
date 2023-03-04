#

def ProceduralWay(StudentValues, StudentToQuery):
    Sum = 0
    n = 0
    
    for Value in StudentValues[StudentToQuery]:
        Sum += Value 
        n += 1
    
    Avg = Sum/n
    
    print("%.2f" % Avg)
    
def FunctionalWay(StudentValues, StudentToQuery):
    Avg = sum(StudentValues[StudentToQuery])/len(StudentValues[StudentToQuery])
    print("%.2f" % Avg)

if __name__ == "__main__":
    n = int(input())
    StudentValues = {}
    
    for i in range(n):
        Name, *Values = input().split(" ")
        StudentValues[Name] = list(map(float, Values))
        
    StudentToQuery = input()
    
    # remember that in competitive programming, input sanitisation is not required
    
    ProceduralWay(StudentValues, StudentToQuery)
