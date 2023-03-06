def SwapCharacter(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()

def swap_case(s): # procedural way 
    s2 = ""
    
    for x in s:
        s2 += SwapCharacter(x)
        
    return s2

def swap_case_functional(s): # functional way 
    return "".join(map(SwapCharacter, s))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
