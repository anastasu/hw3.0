def count_symbol(text: str, symbol: str) -> int:
    """
    Функция находит количество вхождений символа symbol в тексте.
    ВНИМАНИЕ! Реализовать циклом по тексту, без использования встроенной функции count

    :param text: Анализируемый текст
    :param symbol: Искомый символ
    :return: Количество вхождений символа
    """

    a = 0
    for i in text:
        if i == symbol:
            a = a+1

    return a

class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def test_count_symbol(text, symbol, result):
    test_result = count_symbol(text, symbol)
    check = test_result == result
    if len(text) > 100:
        text = text[:45] + " ... " + text[-45:]
    print("text =", text)
    print(f"symbol = {symbol}; result = {result}; test_result = {test_result}")
    print(f"{bcolors.OK}Test passed{bcolors.ENDC}" if check else f"{bcolors.FAIL}Test failed{bcolors.ENDC}")


def test():
    text = "Привет!"
    symbol = "h"
    result = 0
    test_count_symbol(text, symbol, result)

    text = "Привет!"
    symbol = "П"
    result = 1
    test_count_symbol(text, symbol, result)

    text = "AAAA"*10
    symbol = "A"
    result = 40
    test_count_symbol(text, symbol, result)

    text = "Обратный прокси-сервер (англ. reverse proxy) — тип прокси-сервера, который ретранслирует запросы клиентов " \
           "из внешней сети на один или несколько серверов, логически расположенных во внутренней сети. При этом для " \
           "клиента это выглядит так, будто запрашиваемые ресурсы находятся непосредственно на прокси-сервере.[1] В " \
           "отличие от классического прокси, который перенаправляет запросы клиентов к любым серверам в Интернете и " \
           "возвращает им результат, обратный прокси непосредственно взаимодействует лишь с ассоциированными с ним " \
           "серверами и возвращает ответ только от них. "
    symbol = "а"
    result = 29
    test_count_symbol(text, symbol, result)




if __name__ == "__main__":
    test()
