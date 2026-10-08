""" Задание 3. Сравнение поиска """

def liner(data_list, target):
    """ линейный поиск """
    iter_num = 0
    for item in data_list:
        iter_num += 1
        if item == target:
            return iter_num
    return None

def binar(data_list, target):
    """ бинарный поиск """
    min_elem = 0
    max_elem = len(data_list) - 1
    iter_num = 0

    while min_elem <= max_elem:
        middle = (max_elem + min_elem) // 2
        iter_num += 1
        if data_list[middle] == target:
            return iter_num
        if data_list[middle] < target:
            min_elem = middle + 1
        else:
            max_elem = middle - 1
    return None

def print_results(liner_result, binar_result, target):
    """ Выводит сообщения о результатах"""
    if liner_result and binar_result:
        print(f"Количество итераций линейного поиска для {target} элемента: {liner_result}")
        print(f"Количество итераций бинарного поиска для {target} элемента: {binar_result}")

    else:
        if not liner_result:
            print("Линейный поиск ничего не вернул")
        if not binar_result:
            print("Бинарный поиск ничего не вернул")

def main():
    """ 
        При линейном поиске в упорядоченном списке в худшем 
          случае количество итераций при поиске будет равно 
          длине списка. Если в упорядоченном массиве из 1000 элементов
          надо найти 1000й элемент, поиск будет идти последовательно:
          0 - 1 - 2 - 3 ... 1000: 1000 итераций
        При бинарном поиске в упорядоченном списке на каждой итерации 
          отсекается половина списка. Если в упорядоченном массиве из 1000 
          элементов надо найти 1000й элемент, поиск будет отсекать сразу
          половину оставшихся элементов:
          500 - 750 - 875 - 938 ... 1000: ~10 итераций
          Но если в упорядоченном массиве из 1000 элементов надо найти 1й,
          поиск также начнётся с середины и будет отсекать половину оставшихся 
          элементов:
          500 - 250 - 125 - ... 1: 9 итераций
          Линейный поиск справится с такой задачей за 1 итерацию
    """
    data = list(range(1, 1001))
    target_min = 1
    target_max = 1000

    liner_result = liner(data, target_max)
    binar_result = binar(data, target_max)

    print_results(liner_result, binar_result, target_max)

    liner_result = liner(data, target_min)
    binar_result = binar(data, target_min)

    print_results(liner_result, binar_result, target_min)


if __name__ == '__main__':
    main()
