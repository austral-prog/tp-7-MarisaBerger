def index_of_by_index(word, list1, index):
    for i in range(len(list1)):
        if i >= index:
            if list1[i] == word:
                return i 
    newlist = list1[index]
    if word not in newlist:
        return -1
        


def index_of_empty(list2):
    for i in range(len(list2)): 
        index = 0 
        if list2[i] == "":
            return i 
        index += 1
    if "" not in list2:
        return -1


def index_of(word, list3):
    index = 0
    for element in list3:
        if list3[index] == word:
            return index 
        index +=1
    if word not in list3:
            return -1 



def put(word, list4):
    for i in range(len(list4)):
        index = 0
        if list4[i] == "":
            list4[i] = word 
            index += 1
            return i 
    if "" not in list4:
        return -1 



def remove(word, list5):
    if word in list5:
        index = 0
        for i in range(len(list5)):
            if list5[i] == word:
                list5[i] = ""
                index += 1
        return index
    else:
        return 0 


