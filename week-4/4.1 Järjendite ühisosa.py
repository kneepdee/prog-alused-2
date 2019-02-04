def yhisosa(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    yhisosa = []
    return list(set1 & set2)

print(yhisosa([1, 2], [2, 3]))
print(yhisosa(['ich', 'du', 'er', 'sie', 'es'], ['wir', 'ihr', 'sie', 'Sie']))
print(yhisosa([], [1, 1]))
print(yhisosa([1, 1, 1], [1, 1]))