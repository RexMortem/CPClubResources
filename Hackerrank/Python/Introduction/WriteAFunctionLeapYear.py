def is_leap(year):
    leap = False
    
    # Write your logic here
    # Note that order matters for these if statements!
    
    if (year % 400) == 0:
        leap = True
    elif (year % 100) == 0:
        pass # or leap = False
    elif (year % 4) == 0:
        leap = True
    
    return leap # need to understand returning probably

year = int(input())
