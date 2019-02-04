def listid_sonastikuks(arr1, arr2):
    sonastik = {}
    for i in range(len(arr1)):
        sonastik[arr1[i]] = arr2[i]
    print(sonastik)
    return sonastik


listid_sonastikuks([1, 2], [3, 4])
# {1: 3, 2: 4}

listid_sonastikuks(['ATI', 'KAMA'], [
                   'Arvutiteaduse instituut', 'Kasutatav masintõlge'])
# {'KAMA': 'Kasutatav masintõlge', 'ATI': 'Arvutiteaduse instituut'}

listid_sonastikuks([], [])
# {}

listid_sonastikuks([0, 1, 0], ['a', 'b', 'c'])
# {0: 'c', 1: 'b'}
