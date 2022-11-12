def delete(list_, index=None):
    if index is None or index == -1:
        index = -1
        list_ = list_[:index]
    else:
        list_ = list_[:index] + list_[index + 1:]
    return list_
print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))