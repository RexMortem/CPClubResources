def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

def alternate_mutate_string(string, position, character):
    StringList = list(string)
    StringList[position] = character
    return "".join(StringList)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
