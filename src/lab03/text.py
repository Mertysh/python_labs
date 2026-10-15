import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str: #Приводит текст к стандартному виду
    text = re.sub(r'[\t\r\n]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    return text


def tokenize(text: str) -> list[str]: #Рабивает текст на слова
    return re.findall(r'\w+(?:-\w+)*', text, flags=re.UNICODE)


def count_freq(tokens: list[str]) -> dict[str, int]: #Подсчитывает количество слов
    freq = {}

    for w in tokens:
        if w in freq:
            freq[w] = freq[w] + 1
        else:
            freq[w] = 1    

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]: #Возвращает n самых частых строк
    if n <= 0:
        return []

    items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

    return items[:n]


if __name__ == '__main__':
    print(normalize('ПрИвЕт\nМИр\t'))
    print(normalize('ёжик, Ёлка'))
    print(normalize('Hello\r\nWorld'))
    print(normalize('  двойные   пробелы  '))
    print(tokenize('привет, мир!'))
    print(tokenize('hello,world!!!'))
    print(tokenize('по-настоящему круто'))
    print(tokenize('2025 год'))
    print(tokenize('emoji 😀 не слово'))

    freq = count_freq(['a', 'b', 'a', 'c', 'b', 'a'])
    print(freq)
    print(top_n(freq, 2))

    freq2 = count_freq(['bb', 'aa', 'bb', 'aa', 'cc'])
    print(freq2)
    print(top_n(freq2, 2))
