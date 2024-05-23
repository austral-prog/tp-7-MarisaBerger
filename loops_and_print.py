def enumerate_list(list_1):
    lista2 = []
    index=0
    for element in list_1:
        if element != "":
            lista2.append(f"{index}. {element}")
            index += 1
    return lista2

   

def enumerate_backwards(list_2):
    lista1 = []
    index = 0
    for element in list_2:
        if element != "":
            lista1.append(f"{index}. {element[::-1]}")
            index += 1
    return lista1
