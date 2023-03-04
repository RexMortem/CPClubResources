# just follow the instructions for command implementations
# knowing while loop/range structures -> useful
# knowing how to parse inputs/strings (using split)

if __name__ == '__main__':
    N = int(input())
    List = []
    
    i = 0
    
    while i < N:
        Inp = input().split(" ")
        
        Instruction = Inp[0]
        Arguments = [int(Inp[i+1]) for i in range(len(Inp)-1)]
        
        if Instruction == "insert":
            List.insert(Arguments[0], Arguments[1])
        elif Instruction == "print":
            print(List)
        elif Instruction == "remove":
            List.remove(Arguments[0])
        elif Instruction == "append":
            List.append(Arguments[0])
        elif Instruction == "sort":
            List.sort()
        elif Instruction == "pop":
            List.pop()
        elif Instruction == "reverse":
            List.reverse()
            
        i += 1
