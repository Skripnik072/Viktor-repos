def filter_lists(mylist1: list[int], mylist2: list[int]) -> list[int]:
    ''' Функция выводит список с общими числами'''
    new_list = []
    for i in mylist1:
        if i in mylist2:
            new_list.append(i)
    return new_list


print(filter_lists([1, 2, 3, 4], [3, 4, 5, 6]))
# изменения пробные внесены