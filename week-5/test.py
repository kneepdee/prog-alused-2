def print_alla_ules(n):
    if n <= 0:
        print("Põhi!")
    else:
        print(n)
        print_alla_ules(n - 2)
        print(n - 1)

print_alla_ules(5)