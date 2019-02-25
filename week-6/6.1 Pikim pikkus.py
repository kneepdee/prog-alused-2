def pikim_pikkus(suvalise_sügavusega_järjend):
    pikima_järjendi_pikkus = len(suvalise_sügavusega_järjend)
    for element in suvalise_sügavusega_järjend:
        if isinstance(element, list):
            if pikim_pikkus(element) > pikima_järjendi_pikkus:
                pikima_järjendi_pikkus = pikim_pikkus(element)
    return pikima_järjendi_pikkus


print(pikim_pikkus([1, 2, 3]))
# 3
print(pikim_pikkus([[[1, 2, 3]]]))
# 3

print(pikim_pikkus([[], [3, [4, 5], [2, 3, 4, 5, 3, 3],
                         [7], 5, [1, 2, 3], [3, 4]], [1, 2, 3, 4, 5]]))
# 7

print(pikim_pikkus([[], []]))
# 2

print(pikim_pikkus([]))
# 0

print(pikim_pikkus([[[[[]]]]]))
# 1
