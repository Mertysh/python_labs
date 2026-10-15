import sys

import text

txt = sys.stdin.readline()

txt = text.normalize(txt)
tokens = text.tokenize(txt)
freq = text.count_freq(tokens)
top = text.top_n(freq)

print(f'Всего слов: {len(tokens)}')
print(f'Уникальных слов: {len(freq)}')
print('Топ-5:')

for word, count in top:
    print(f'{word}:{count}')
