# -*- coding: utf-8 -*-
"""Извлекает ТОЛЬКО видимое тело <main> страницы: то, что читает человек."""
import re, html, sys, os
PAGES = {'index.html':'glavnaya','shkola/index.html':'shkola','kursy/index.html':'kursy',
 'kursy/gekata/index.html':'gekata','kursy/runy/index.html':'runy','kursy/besy/index.html':'besy',
 'kursy/nastavnichestvo/index.html':'nastavnichestvo','taro/index.html':'taro',
 'zhurnal/index.html':'zhurnal','oberegi/index.html':'oberegi','nechist/index.html':'nechist',
 'ob-irine/index.html':'ob-irine','vopros-otvet/index.html':'vopros-otvet',
 'kontakty/index.html':'kontakty','politika/index.html':'politika'}
out = sys.argv[1] if len(sys.argv) > 1 else '/tmp/ira-teksty'
os.makedirs(out, exist_ok=True)
vse = []
for f, name in PAGES.items():
    h = open(f, encoding='utf-8').read()
    m = re.search(r'<main>(.*?)</main>', h, re.S)
    h = m.group(1) if m else h
    h = re.sub(r'<svg.*?</svg>', '', h, flags=re.S)
    h = re.sub(r'<(h1|h2|h3|h4|p|li|summary|div)[^>]*>', '\n', h)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', h)).replace('\xa0', ' ')
    t = '\n'.join(re.sub(r'[ \t]+', ' ', l).strip() for l in t.split('\n') if l.strip())
    open(f'{out}/{name}.txt', 'w', encoding='utf-8').write(t)
    vse.append(f'=== {name} ===\n{t}')
open(f'{out}/ВСЁ.txt', 'w', encoding='utf-8').write('\n\n'.join(vse))
print('страниц:', len(PAGES), '| знаков:', sum(len(v) for v in vse))
