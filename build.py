# -*- coding: utf-8 -*-
"""Сборка сайта школы Ирины Волковой."""
import sys, os, json, shutil
sys.path.insert(0, 'scripts')
from engine import BASE, VERSION, DOMAIN
from layout import JS, INDEXING, page
from theme import CSS
sys.path.insert(0, 'content')
import pages_main, pages_kursy, pages_kursy2, pages_zhurnal, pages_info, pages_karty, pages_kviz, pages_kursy3
from arkany import ARKANY

articles = json.load(open('content/articles.json', encoding='utf-8'))
ob = [a for a in articles if a['kind'] == 'oberegi']
ne = [a for a in articles if a['kind'] == 'nechist']

# статика
open('site.css', 'w', encoding='utf-8').write(CSS)
open('site.js', 'w', encoding='utf-8').write(JS)
open('.nojekyll', 'w').write('')

# страницы
pages_main.glavnaya(ne[1:2] + ob[2:3] + ne[11:12])
pages_kursy.shkola()
pages_kursy.kursy_katalog()
pages_kursy2.gekata()
pages_kursy2.runy()
pages_kursy3.besy_nastoyashchie(articles)
pages_kursy3.grimuar()
pages_kursy2.nastavnichestvo()
pages_kursy2.taro()
pages_zhurnal.zhurnal(articles)
pages_zhurnal.razdel('oberegi', articles)
pages_zhurnal.razdel('nechist', articles)
pages_info.ob_irine()
pages_info.vopros_otvet()
pages_info.kontakty()
pages_info.politika()
pages_info.lunnyj_krug()
pages_kviz.kviz()
pages_info.slovar()
pages_info.ne_nashlos()
pages_karty.hab()
for i, a in enumerate(ARKANY):
    pages_karty.stranica(a, ARKANY[i - 1] if i > 0 else None,
                         ARKANY[i + 1] if i + 1 < len(ARKANY) else None)

for i, a in enumerate(articles):
    same = [x for x in articles if x['kind'] == a['kind'] and x['slug'] != a['slug']]
    sosedi = (same + articles)[i % max(1, len(same)):][:3] or same[:3]
    ryad = ob if a['kind'] == 'oberegi' else ne
    j = ryad.index(a)
    pages_zhurnal.statya(a, sosedi,
                         ryad[j - 1] if j > 0 else None,
                         ryad[j + 1] if j + 1 < len(ryad) else None)

# карта сайта
paths = ['', 'shkola/', 'kursy/', 'kursy/gekata/', 'kursy/runy/', 'kursy/besy/',
         'kursy/nastavnichestvo/', 'kursy/grimuar/', 'taro/', 'karty/', 'zhurnal/', 'oberegi/', 'nechist/',
         'ob-irine/', 'luna/', 'kviz/', 'slovar/', 'vopros-otvet/', 'kontakty/', 'politika/'] + \
        [f'karty/{a["slug"]}/' for a in ARKANY] + \
        [f'zhurnal/{a["url"]}/' for a in articles]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">'.replace('sitemap.org', 'sitemaps.org')]
for p in paths:
    pr = '1.0' if p == '' else ('0.9' if p.count('/') <= 1 else '0.7')
    sm.append(f'<url><loc>{DOMAIN}/{p}</loc><priority>{pr}</priority></url>')
sm.append('</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write('\n'.join(sm))

open('robots.txt', 'w', encoding='utf-8').write(
    ('User-agent: *\nAllow: /\n' if INDEXING else 'User-agent: *\nDisallow: /\n') +
    f'Sitemap: {DOMAIN}/sitemap.xml\n')

shutil.copy('__404__/index.html', '404.html')
shutil.rmtree('__404__')
print('страниц собрано:', len(paths), '| версия', VERSION)
