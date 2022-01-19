def same_in_row(text: str) -> int:
    """
    Функция находит максимальное количество идущих подряд **одинаковых** символов.

    :param text: Анализируемый текст
    :return: Максимальное количество идущих подряд **одинаковых** символов
    """
    m = 1 # макс длина цепочки
    l = 1 # начальная длина цепочки
    for i in range(0,len(text)-1):
        if text[i]== text [i+1]:
            l+=1
            m = max(l,m) # перезаписали Макс длину
        else:
            l = 1
    return(m)




class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def test_same_in_row(text, result):
    test_result = same_in_row(text)
    check = test_result == result
    if len(text) > 100:
        text = text[:45] + " ... " + text[-45:]
    print("text =", text)
    print(f"result = {result}; test_result = {test_result}")
    print(f"{bcolors.OK}Test passed{bcolors.ENDC}" if check else f"{bcolors.FAIL}Test failed{bcolors.ENDC}")


def test():
    text = "Привет!"
    result = 1
    test_same_in_row(text, result)

    text = "Доббрый вечер!"
    result = 2
    test_same_in_row(text, result)

    text = "ггаывалоРВГаргыватвмсцшвавыраррывпаллллывароимгсвггвНННВаыттвттавоооООооооооВЫвыва"
    result = 6
    test_same_in_row(text, result)

    text = "Ф"*1000
    result = 1000
    test_same_in_row(text, result)


if __name__ == "__main__":
    test()
