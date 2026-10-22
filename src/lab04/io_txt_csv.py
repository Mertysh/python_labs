from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str: # Функция читает файл и возвращает его содержимое одной строкой
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None: # Создать или перезаписать CSV с разделителем-запятой
    p = Path(path)
    rows = list(rows)

    if len(rows) != 0:
        first_len = len(rows[0])
        for i in rows:
            if len(i) != first_len:
                raise ValueError('Все строки должны иметь одинаковую длину')

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


if __name__ == '__main__':
    print(read_text('data/lab04/input.txt', encoding= 'utf-8'))
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")
