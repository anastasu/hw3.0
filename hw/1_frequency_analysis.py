def frequency_analysis(text: str) -> dict:
    """
    Функция проводит частотный анализ текста.

    :param text: Анализируемый текст
    :return: Словарь вида {"a":102,"b":213, ..}
    """
    D = {}

    for i in range (len(text)):
        if text[i] in D:
            D[text[i]]+=1
        else:
            D[text[i]]=1
    return (D)


class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


def test_frequency_analysis(text, result):
    test_result = frequency_analysis(text)
    check = test_result == result
    if len(text) > 100:
        text = text[:45] + " ... " + text[-45:]
    print("text =", text)
    print(f"result = {result}; test_result = {test_result}")
    print(f"{bcolors.OK}Test passed{bcolors.ENDC}" if check else f"{bcolors.FAIL}Test failed{bcolors.ENDC}")


def test():
    text = "Привет!"
    result = {
        "П": 1,
        "р": 1,
        "и": 1,
        "в": 1,
        "е": 1,
        "т": 1,
        "!": 1
    }
    test_frequency_analysis(text, result)

    text = "П"*1000
    result = {
        "П": 1000
    }
    test_frequency_analysis(text, result)

    text = "Обратный прокси-сервер (англ. reverse proxy) — тип прокси-сервера, который ретранслирует запросы клиентов " \
           "из внешней сети на один или несколько серверов, логически расположенных во внутренней сети. При этом для " \
           "клиента это выглядит так, будто запрашиваемые ресурсы находятся непосредственно на прокси-сервере.[1] В " \
           "отличие от классического прокси, который перенаправляет запросы клиентов к любым серверам в Интернете и " \
           "возвращает им результат, обратный прокси непосредственно взаимодействует лишь с ассоциированными с ним " \
           "серверами и возвращает ответ только от них. "
    result = {'О': 1, 'б': 4, 'р': 41, 'а': 29, 'т': 36, 'н': 32, 'ы': 12, 'й': 7, ' ': 73, 'п': 14, 'о': 43, 'к': 18,
              'с': 34, 'и': 35, '-': 3, 'е': 50, 'в': 26, '(': 1, 'г': 4, 'л': 18, '.': 4, 'r': 3, 'e': 3, 'v': 1,
              's': 1, 'p': 1, 'o': 1, 'x': 1, 'y': 1, ')': 1, '—': 1, ',': 5, 'у': 6, 'з': 8, 'ш': 3, 'д': 8, 'ь': 4,
              'ч': 3, 'ж': 1, 'х': 3, 'П': 1, 'э': 2, 'м': 9, 'я': 5, '[': 1, '1': 1, ']': 1, 'В': 1, 'ю': 1, 'И': 1,
              'щ': 2, 'ц': 1}
    test_frequency_analysis(text, result)


if __name__ == "__main__":
    test()
