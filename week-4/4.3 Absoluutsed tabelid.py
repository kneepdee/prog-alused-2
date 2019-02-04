from copy import deepcopy

def absoluutne_tabel(arr):
  new_arr = deepcopy(arr)
  for i in range(len(new_arr)):
    for j in range(len(new_arr[i])):
      new_arr[i][j] = abs(new_arr[i][j])
  return new_arr

def absolutiseeri_tabel(arr):
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      arr[i][j] = abs(arr[i][j])

tabel = [[1, -2], [-3, 4]]
print(absoluutne_tabel(tabel))
# [[1, 2], [3, 4]]

print(tabel)
# [[1, -2], [-3, 4]]

 

# tabel = [[1, -2], [-3, 4]]
# absolutiseeri_tabel(tabel)

# print(tabel)
# [[1, 2], [3, 4]]