# -*- coding: utf-8 -*-
"""Механический гейт сайта: классы без стилей, битые ссылки, пустые страницы."""
import re, glob, os, sys

css = open('site.css', encoding='utf-8').read()
css_classes = set(re.findall(r'\.([a-zA-Z][\w-]*)', css))

pages = sorted(glob.glob('**/index.html', recursive=True)) + ['404.html']
used, bad_cls, links = set(), set(), set()
for f in pages:
    h = open(f, encoding='utf-8').read()
    for m in re.findall(r'class="([^"]+)"', h):
        for c in m.split():
            used.add(c)
    for m in re.findall(r'href="([^"]+)"', h):
        links.add((f, m))

orphan = sorted(c for c in used if c not in css_classes)
print('КЛАССЫ БЕЗ СТИЛЕЙ:', len(orphan), orphan if orphan else '')

# внутренние ссылки
BASE = '/ira-shkola/'
broken = []
for f, href in sorted(links):
    if href.startswith(('http', 'mailto:', 'tel:', '#')):
        continue
    if not href.startswith(BASE):
        broken.append((f, href, 'без базового пути'))
        continue
    rel = href[len(BASE):].split('?')[0]
    target = rel if rel else 'index.html'
    if target.endswith('/'):
        target += 'index.html'
    if not os.path.exists(target):
        broken.append((f, href, 'нет файла'))
print('БИТЫХ ССЫЛОК:', len(broken))
for b in broken[:20]:
    print('   ', b)

# «появится здесь» и заглушки
stub = re.compile(r'появится здесь|готовится|следующими волнами|прототип|уточнить|TODO|заглушка', re.I)
st = [(f, m.group(0)) for f in pages for m in [stub.search(open(f, encoding='utf-8').read())] if m]
print('ЗАГЛУШЕК:', len(st), st[:5])

# вес страниц
small = [(f, os.path.getsize(f)) for f in pages if os.path.getsize(f) < 9000]
print('ЛЁГКИХ СТРАНИЦ (<9КБ):', len(small), small[:5])

# один h1 на страницу
for f in pages:
    n = len(re.findall(r'<h1[ >]', open(f, encoding='utf-8').read()))
    if n != 1:
        print('  H1 не один:', f, n)

# смешение кириллицы и латиницы внутри слова (опечатка при правках)
import html as _h
mix = []
for f2 in pages:
    h = open(f2, encoding='utf-8').read()
    m = re.search(r'<main>(.*?)</main>', h, re.S)
    if not m:
        continue
    t = _h.unescape(re.sub(r'<[^>]+>', ' ',
        re.sub(r'<(script|style|svg).*?</\1>', '', m.group(1), flags=re.S)))
    for w in re.findall(r'\S*[А-Яа-яЁё]+[A-Za-z]+\S*|\S*[A-Za-z]+[А-Яа-яЁё]+\S*', t):
        mix.append((f2, w))
print('СЛОВ СО СМЕШЕНИЕМ АЛФАВИТОВ:', len(mix), mix[:5])

# уникальность title и description
import collections
tt, dd = collections.Counter(), collections.Counter()
for f in pages:
    h = open(f, encoding='utf-8').read()
    tt[re.search(r'<title>(.*?)</title>', h, re.S).group(1)] += 1
    dd[re.search(r'name="description" content="(.*?)"', h, re.S).group(1)] += 1
print('ДУБЛЕЙ TITLE:', sum(v - 1 for v in tt.values() if v > 1),
      [k for k, v in tt.items() if v > 1][:3])
print('ДУБЛЕЙ DESCRIPTION:', sum(v - 1 for v in dd.values() if v > 1),
      [k[:60] for k, v in dd.items() if v > 1][:3])
