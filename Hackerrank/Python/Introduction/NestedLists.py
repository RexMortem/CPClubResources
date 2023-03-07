if __name__ == '__main__':
    Names = []
    Scores = []
    
    n = int(input())
    
    for _ in range(n):
        Names.append(input())
        Scores.append(float(input()))
        
    Smallest = min(Scores)
    SecondSmallestValue = 999999
    SecondSmallestIndexes = None
    
    i = 0
    
    while i < len(Scores):
        Score = Scores[i]
        
        if Score > Smallest:
            if Score == SecondSmallestValue:
                SecondSmallestIndexes.append(i)
            elif Score < SecondSmallestValue:
                SecondSmallestIndexes = [i]
                SecondSmallestValue = Score
                
        i += 1
        
    Output = [Names[i] for i in SecondSmallestIndexes]
    Output.sort()
    
    for x in Output:
        print(x)
