import sys
from collections import Counter

from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, top_n


def frequencies_from_text(text: str) -> dict[str, int]: # Нормализует текст и считает количество слов
    tokens = tokenize(normalize(text))

    return Counter(tokens) 


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]: # Сортирует слова по частоте поубыванию, если частота одинаковая, то по алфавиту
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


def main(input_path = "data/lab04/input.txt", output_path = "data/lab04/report.csv", encoding = "utf-8"): # Обрабатывает текст из input.txt и записывает в report.csv
    try:
        text = read_text(input_path, encoding=encoding)
    except FileNotFoundError:
        print('Файл не найден')
        sys.exit(1)
    text_frequencies_from_text = frequencies_from_text(text)
    text_sorted_word_count = sorted_word_counts(text_frequencies_from_text)

    write_csv(text_sorted_word_count, output_path, header=('word', 'count'))

    print("Всего слов:", sum(text_frequencies_from_text.values()))
    print("Уникальных слов:", len(text_frequencies_from_text))
    print("Топ-5:")
    for word, count in top_n(text_frequencies_from_text, 5):
        print(f"{word}:{count}")

if __name__ == '__main__':
    main()
