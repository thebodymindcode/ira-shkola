# -*- coding: utf-8 -*-
"""Сборка сайта школы Ирины Волковой."""
import sys, os, json, shutil
sys.path.insert(0, 'scripts')
from engine import BASE, VERSION, DOMAIN
from layout import JS, INDEXING, page
from theme import CSS
import pages_main, pages_kursy, pages_kursy2, pages_zhurnal, pages_info

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
pages_kursy2.besy(articles)
pages_kursy2.nastavnichestvo()
pages_kursy2.taro()
pages_zhurnal.zhurnal(articles)
pages_zhurnal.razdel('oberegi', articles)
pages_zhurnal.razdel('nechist', articles)
pages_info.ob_irine()
pages_info.vopros_otvet()
pages_info.kontakty()
pages_info.politika()
pages_info.ne_nashlos()

for i, a in enumerate(articles):
    same = [x for x in articles if x['kind'] == a['kind'] and x['slug'] != a['slug']]
    sosedi = (same + articles)[i % max(1, len(same)):][:3] or same[:3]
    pages_zhurnal.statya(a, sosedi)

# карта сайта
paths = ['', 'shkola/', 'kursy/', 'kursy/gekata/', 'kursy/runy/', 'kursy/besy/',
         'kursy/nastavnichestvo/', 'taro/', 'zhurnal/', 'oberegi/', 'nechist/',
         'ob-irine/', 'vopros-otvet/', 'kontakty/', 'politika/'] + \
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
