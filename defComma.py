def cc(list):
    if not list:
        print("empty list")
    elif len(list) == 1:
        print(f"{str(list[0])}")
    else:
        x = ", ".join(list[:-1])
        print(f"{x} and {list[-1]}")
lista = ['a', 'b', 'c']
cc(lista)