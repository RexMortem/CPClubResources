def SwapCharacter(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()

def swap_case(s): # unfortunately, no easy way to form strings from map
    s2 = ""
    
    for x in s:
        s2 += SwapCharacter(x)
        
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
