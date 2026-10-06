""" Задание 1. Анализ текста """

def main():
    """ Самая главная функция """
    input_string = ( "Python это мощный и простой язык программирования. "
    "Python популярен в веб-разработке и data science.")

    words_list = input_string.replace(".", "").replace(",", "").split()
    words_dict = {}

    for word in words_list:
        words_dict[word] = [len(word), words_list.count(word)]

    max_len = max(words_dict, key=lambda k: words_dict[k][0])
    max_occurrences = max(words_dict, key=lambda k: words_dict[k][1])

    print(f"Всего слов: {len(words_dict)}") # считает количество уникальных слов
    print(f"Самое частое слово: {max_occurrences} ({words_dict[max_occurrences][1]} раза)")
    print(f"Самое длинное слово: {max_len}")

if __name__ == '__main__':
    main()
