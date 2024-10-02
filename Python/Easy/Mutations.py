def mutate_string(string, position, character):
    mod = string[:position] + character + string[position + 1:]
    return mod