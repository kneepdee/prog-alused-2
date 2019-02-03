def symbolite_sagedus(str):
    sagedused = {}
    for letter in str:
        if letter in sagedused:
            sagedused[letter] += 1
        else:
            sagedused[letter] = 1
    return sagedused


print(symbolite_sagedus('suitsupääsuke'))