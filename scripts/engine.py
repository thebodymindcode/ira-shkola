# -*- coding: utf-8 -*-
"""Движок сайта школы Ирины Волковой: шаблон, стили, типографика."""
import re

BASE = '/ira-shkola/'
VERSION = '2026082048'
DOMAIN = 'https://thebodymindcode.github.io/ira-shkola'
TITLE_SITE = 'Школа Ирины Волковой'
TG = 'https://t.me/ira_volkova_life'
IG = 'https://www.instagram.com/theiravolkova/'

NB = ' '

MENU = [
    ('Главная', ''),
    ('Школа', 'shkola/'),
    ('Курсы', 'kursy/'),
    ('Таро', 'taro/'),
    ('Ведьмин дневник', 'zhurnal/'),
    ('Об Ирине', 'ob-irine/'),
    ('Контакты', 'kontakty/'),
]

FOOTER_LINKS = [
    ('Главная', ''), ('Школа', 'shkola/'), ('Курсы', 'kursy/'),
    ('Чёрный Гримуар', 'kursy/grimuar/'), ('Бесы', 'kursy/besy/'),
    ('Геката', 'kursy/gekata/'), ('Руны', 'kursy/runy/'),
    ('Наставничество', 'kursy/nastavnichestvo/'), ('Таро', 'taro/'),
    ('Обереги дома', 'oberegi/'), ('Нечисть', 'nechist/'), ('Ведьмин дневник', 'zhurnal/'),
    ('Об Ирине', 'ob-irine/'), ('Вопросы', 'vopros-otvet/'), ('Контакты', 'kontakty/'),
]

# ---------------------------------------------------------------- типографика
SHORT = ('и в во на не но с со к ко о об от до за из у я по для при над под без'
         ' же ли бы то а как что чем их его её').split()
NUMWORDS = ('один одна одно два две три четыре пять шесть семь восемь девять десять'
            ' одиннадцать двенадцать двадцать тридцать сорок пятьдесят сто').split()

def typo(t):
    """Неразрывные пробелы: короткие слова, числительные, число с единицей."""
    if not t:
        return t
    # число + слово (12 знаков, 4 ступени)
    t = re.sub(r'(\d+)\s+(?=[а-яёa-z])', r'\1' + NB, t)
    # короткие предлоги и союзы клеим к следующему слову
    def glue(m):
        return m.group(1) + m.group(2) + NB
    pat = r'(^|[\s(«,.;:!?])(' + '|'.join(SHORT) + r')\s+'
    for _ in range(3):
        t = re.sub(pat, glue, t, flags=re.IGNORECASE)
    return t

def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))

# ---------------------------------------------------------------- иконки
# Иконки в духе алхимической гравюры: двойной контур, точки-звёзды, орнамент.
ICONS = {
 'klyuch': '<circle cx="7.4" cy="7.4" r="3.6"/><circle cx="7.4" cy="7.4" r="1.3"/>'
           '<path d="M10 10 19.6 19.6"/><path d="M16.4 16.4l2.6-2.6"/><path d="M13.6 13.6l1.9-1.9"/>'
           '<path d="M19.6 19.6l1.2 1.2"/>',
 'luna': '<path d="M20.4 14.8A8.6 8.6 0 1 1 9.2 3.6a6.7 6.7 0 0 0 11.2 11.2Z"/>'
         '<path d="M17.6 6.4l.5 1.4 1.4.5-1.4.5-.5 1.4-.5-1.4-1.4-.5 1.4-.5Z"/>'
         '<circle cx="6.6" cy="17.4" r=".7"/>',
 'svecha': '<path d="M12 2.4c2 2.1 3 3.6 3 4.9a3 3 0 1 1-6 0c0-1.3 1-2.8 3-4.9Z"/>'
           '<path d="M10.8 7.4a1.2 1.2 0 0 0 2.4 0"/>'
           '<rect x="8.6" y="11.6" width="6.8" height="9.4" rx="1.3"/>'
           '<path d="M8.6 14.6h6.8M8.6 17.6h6.8"/>',
 'kniga': '<path d="M12 6.2C10.2 4.8 8.3 4.2 5.9 4.2H3.5v13.4h2.4c2.4 0 4.3.6 6.1 2"/>'
          '<path d="M12 6.2c1.8-1.4 3.7-2 6.1-2h2.4v13.4h-2.4c-2.4 0-4.3.6-6.1 2z"/>'
          '<path d="M12 6.2v15.4"/><path d="M6 8.4h3.2M6 11.2h3.2M14.8 8.4H18M14.8 11.2H18"/>',
 'karta': '<rect x="8.8" y="3.4" width="10.4" height="14.6" rx="1.8"/>'
          '<rect x="10.8" y="5.6" width="6.4" height="10.2" rx="1"/>'
          '<path d="M7.6 5.6 4.4 6.8l3.6 9.8"/><path d="M14 8.6v4.2m-2.1-2.1h4.2"/>',
 'runa': '<rect x="4.8" y="2.6" width="14.4" height="18.8" rx="2.2"/>'
         '<rect x="7" y="4.8" width="10" height="14.4" rx="1.2" opacity=".45"/>'
         '<path d="M9.6 7.4v9.2M9.6 10.8l4.6-3.4M9.6 13.2l4.6 3.4"/>',
 'dom': '<path d="M3.2 11.6 12 4l8.8 7.6"/><path d="M5.8 10.2V20.4h12.4V10.2"/>'
        '<path d="M10 20.4v-5.6h4v5.6"/><path d="M12 4V2.2"/>'
        '<path d="M11.2 2.2h1.6M8.6 13h1.4M14 13h1.4"/>',
 'ogon': '<path d="M12 21.4c3.8 0 6.4-2.5 6.4-6 0-4.3-4.3-6-3.7-11.1C11.4 6 8.9 8.6 8.9 11.2c0 1.4.5 2.4.5 3 0 1-.8 1.8-1.7 1.1-.9-.6-1.2-2-1.2-2.8-1 1.5-1.3 2.7-1.3 4 0 3.2 2.6 5.4 6.8 5.4Z"/>'
        '<path d="M12 18.6c1.3 0 2.2-.9 2.2-2.1 0-1.5-1.5-2.1-1.3-3.9-1.2.9-2 1.9-2 2.9 0 1.5.4 1.6.4 2 0 .6-.4.9-.8.6"/>',
 'krug': '<circle cx="12" cy="12" r="8.8"/><circle cx="12" cy="12" r="5.4" opacity=".5"/>'
         '<circle cx="12" cy="12" r="2"/>'
         '<path d="M12 3.2v1.8M12 19v1.8M3.2 12h1.8M19 12h1.8"/>'
         '<path d="M5.8 5.8l1.3 1.3M16.9 16.9l1.3 1.3M18.2 5.8l-1.3 1.3M7.1 16.9l-1.3 1.3"/>',
 'ruka': '<path d="M8.6 11.4V5.4a1.7 1.7 0 0 1 3.4 0v5.2"/>'
         '<path d="M12 9.6a1.7 1.7 0 0 1 3.4 0V12"/>'
         '<path d="M15.4 11a1.7 1.7 0 0 1 3.4 0v4c0 3.6-2.6 6.4-6.4 6.4-2.6 0-4-1.2-5.4-3.2l-2.6-3.8a1.7 1.7 0 0 1 2.6-2.1l1.6 1.7"/>'
         '<circle cx="12.6" cy="15.4" r="1.6" opacity=".55"/>',
 'glaz': '<path d="M2.2 12S6.2 5.2 12 5.2 21.8 12 21.8 12 17.8 18.8 12 18.8 2.2 12 2.2 12Z"/>'
         '<circle cx="12" cy="12" r="3.2"/><circle cx="12" cy="12" r="1.1"/>'
         '<path d="M12 2.8v1.4M4.2 5.4l1 1M19.8 5.4l-1 1M12 19.8v1.4"/>',
 'chas': '<path d="M6.6 2.8h10.8M6.6 21.2h10.8"/>'
         '<path d="M7.8 2.8v3.4c0 2.1 4.2 3.7 4.2 5.8s-4.2 3.7-4.2 5.8v3.4"/>'
         '<path d="M16.2 2.8v3.4c0 2.1-4.2 3.7-4.2 5.8s4.2 3.7 4.2 5.8v3.4"/>'
         '<path d="M9.6 6.4h4.8M9.6 17.6h4.8"/><circle cx="12" cy="12" r=".9"/>',
 'nit': '<path d="M2.8 11.4c2.6 0 3.4-3.6 6-3.6s3.4 3.6 6 3.6 3.4-3.6 6-3.6"/>'
        '<path d="M7.2 12.4c0 3 1.9 5 4.8 5s4.8-2 4.8-5"/>'
        '<circle cx="12" cy="14.6" r="1.5"/>',
 'sol': '<path d="M12 2.8 20 7.4v9.2L12 21.2 4 16.6V7.4Z"/>'
        '<path d="M12 2.8v18.4M4 7.4l8 4.6 8-4.6"/>'
        '<circle cx="12" cy="12" r="1.4" opacity=".6"/>',
 'zerkalo': '<ellipse cx="12" cy="9.6" rx="6.4" ry="7.2"/>'
            '<ellipse cx="12" cy="9.6" rx="4.2" ry="5"/>'
            '<path d="M9.4 6.4c.9-.9 2-1.4 3.1-1.4"/>'
            '<path d="M12 16.8V21M9 21h6"/>',
 'les': '<path d="M12 2.2 7 9.6h2.9L5.4 15.6h5.1"/><path d="M12 2.2l5 7.4h-2.9l4.5 6h-5.1"/>'
        '<path d="M10.6 15.6h2.8V21h-2.8z"/><path d="M8.6 21h6.8"/>',
 'voda': '<path d="M12 2.8c3.6 4.3 5.4 7.1 5.4 9.5a5.4 5.4 0 0 1-10.8 0c0-2.4 1.8-5.2 5.4-9.5Z"/>'
         '<path d="M9.4 12.6c0 1.6 1.2 2.8 2.6 2.8" opacity=".6"/>'
         '<path d="M4.2 19.4c2.8 1.4 12.8 1.4 15.6 0"/>',
 'strela': '<path d="M4.4 12h13.4m-5.2-5.4L18.8 12l-6.2 5.4"/>',
 'voron': '<path d="M4.2 14.4c2-5.2 6.2-7.6 10.6-7.6l5-2.4-1.4 3.8c1 2.7.4 5.6-1.7 7.7-2.7 2.7-7.2 3.1-10.4 1"/>'
          '<path d="M8.4 17.8 6 21.4M11.8 18.6 10.8 21.6"/>'
          '<circle cx="15.6" cy="8.4" r=".8"/><path d="M17.8 7.2l1.8-.6"/>',
 'podkova': '<path d="M7 20.6V12.8a5 5 0 0 1 10 0v7.8"/>'
            '<path d="M5 20.6h3.8M15.2 20.6H19"/>'
            '<circle cx="9.2" cy="9.4" r=".8"/><circle cx="14.8" cy="9.4" r=".8"/>'
            '<circle cx="8.4" cy="13.6" r=".8"/><circle cx="15.6" cy="13.6" r=".8"/>',
 'perekryostok': '<path d="M12 21.4V12"/><path d="M12 12 4.2 5"/><path d="M12 12l7.8-7"/>'
                 '<circle cx="12" cy="12" r="2.4"/><circle cx="12" cy="12" r="5" opacity=".4"/>',
 'tg': '<path d="M20.6 4.4 2.9 11.2c-1 .4-1 1 .1 1.3l4.4 1.4 1.7 5.2c.3.7.6.8 1.1.3l2.5-2.4 4.6 3.4c.9.5 1.4.2 1.6-.8l2.7-12.7c.2-1-.4-1.5-1-1.2Z"/>',
 'ig': '<rect x="3.4" y="3.4" width="17.2" height="17.2" rx="5"/><circle cx="12" cy="12" r="4"/>'
       '<circle cx="17" cy="7" r="1.1"/>',
}

# знаки старшего футарка для нумерации шагов
RUNY_NOMERA = [
 '<path d="M7 4v16M7 7.6l7-3.2M7 12l7-3.2"/>',                                   # феху
 '<path d="M6 20V7.6C6 5.6 7.6 4 9.8 4h.4C12.4 4 14 5.6 14 7.6V20"/>',           # уруз
 '<path d="M7 4v16M7 7l6 3.4L7 14"/>',                                           # турисаз
 '<path d="M7 4v16M7 7l6-2.6M7 11.6l6-2.6"/>',                                   # ансуз
 '<path d="M7 4v16M7 4h4.4a2.8 2.8 0 0 1 0 5.6H7M10.4 9.6 14 20"/>',             # райдо
 '<path d="M13.6 4 7 12l6.6 8"/>',                                               # кеназ
 '<path d="M6 4l9 16M15 4 6 20"/>',                                              # гебо
 '<path d="M7 20V7l6-3v13"/>',                                                   # вуньо
 '<path d="M6 4v16M14 4v16M6 8.4l8 7.2"/>',                                      # хагалаз
 '<path d="M6 5.6 14 18.4M6 15.4 14 8.6"/>',                                     # наутиз
]


def runa_nomer(n, razmer=58):
    """Номер шага рунической литерой в круге с орнаментом."""
    znak = RUNY_NOMERA[(n - 1) % len(RUNY_NOMERA)]
    tochki = ''.join(
        f'<circle cx="{22 + 17.4 * __import__("math").cos(i * 1.0472 - 1.5708):.1f}" '
        f'cy="{22 + 17.4 * __import__("math").sin(i * 1.0472 - 1.5708):.1f}" r="1" '
        f'fill="#C9A227" opacity=".55"/>' for i in range(6))
    return (f'<svg class="rn" viewBox="0 0 44 44" width="{razmer}" height="{razmer}" '
            f'aria-hidden="true">'
            f'<circle cx="22" cy="22" r="20.5" fill="none" stroke="#C9A227" stroke-width="1.1" opacity=".62"/>'
            f'{tochki}'
            f'<g transform="translate(11.5,10) scale(0.86)" fill="none" stroke="#E3C15B" '
            f'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{znak}</g>'
            f'<text x="22" y="41" text-anchor="middle" fill="#C9A227" '
            f'style="font-family:Forum,serif;font-size:9px;letter-spacing:1px">{n}</text></svg>')


def ico(name, cls='ic'):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{ICONS.get(name, ICONS["krug"])}</svg>')



# Иконки выпадающего меню: у каждой строки свой знак, по нему видно, куда ведёт пункт.
# Рисунок в одном стиле с ICONS: тонкая линия гравюры, без заливок.
MENU_ICONS = {
    # курсы
    'grimuar': '<rect x="4.6" y="3.2" width="13.4" height="17.6" rx="1.6"/>'
               '<path d="M18 5.2h1.6v14.6H18"/><path d="M8 3.2v17.6"/>'
               '<circle cx="13.2" cy="12" r="2.6"/><path d="M13.2 9.4v-1.4m0 8v-1.4m2.6-2.6h1.4m-8 0h1.4"/>'
               '<path d="M11.4 20.8v1.4h3.6v-1.4"/>',
    'besy': '<path d="M7.4 8.2C6 6.6 5.4 5 5.6 3.2c1.7.4 3 1.4 3.9 3"/>'
            '<path d="M16.6 8.2c1.4-1.6 2-3.2 1.8-5-1.7.4-3 1.4-3.9 3"/>'
            '<path d="M12 8.2c-3.2 0-5.6 2.4-5.6 5.6 0 3 2.5 5.4 5.6 5.4s5.6-2.4 5.6-5.4c0-3.2-2.4-5.6-5.6-5.6Z"/>'
            '<path d="M9.8 12.6h.02M14.2 12.6h.02" stroke-width="2.2" stroke-linecap="round"/>'
            '<path d="M9.8 16.2c1.4.9 3 .9 4.4 0"/>',
    'gekata': '<path d="M12 3.4v17.2"/><path d="M5.6 7.2v10.2"/><path d="M18.4 7.2v10.2"/>'
              '<path d="M12 3.4a3 3 0 0 0-2.4 2.6M12 3.4a3 3 0 0 1 2.4 2.6"/>'
              '<circle cx="5.6" cy="6" r="1.5"/><circle cx="18.4" cy="6" r="1.5"/>'
              '<path d="M4.2 20.6h15.6"/><path d="M9.4 17.4h5.2"/>',
    'runy_kurs': '<path d="M6.4 3.6v16.8"/><path d="M6.4 8.4 12 3.6M6.4 12l5.6 4.8"/>'
                 '<path d="M17.4 3.6v16.8"/><path d="M17.4 11.4l3-3.6M17.4 11.4l3 3.6"/>',
    'nastav': '<circle cx="8.4" cy="7.6" r="2.8"/><circle cx="16.6" cy="9.4" r="2.2"/>'
              '<path d="M3.6 20.4c0-3.2 2.2-5.4 4.8-5.4s4.8 2.2 4.8 5.4"/>'
              '<path d="M14.6 20.4c0-2.6 1.4-4.4 3.4-4.4 1.4 0 2.4.8 3 2"/>'
              '<path d="M11.8 12.4l1.6 1.4"/>',
    'stupeni': '<path d="M3.4 20.6h4.2v-4.2h4.2v-4.2h4.2V8h4.6"/>'
               '<path d="M3.4 20.6v-2M20.6 8V3.6"/><circle cx="20.6" cy="5.6" r="1.4"/>'
               '<path d="M7.6 16.4v4.2M11.8 12.2v8.4M16 8v12.6"/>',
    # таро
    'taro_kurs': '<rect x="7.4" y="3.2" width="9.2" height="13.6" rx="1.4"/>'
                 '<path d="M12 5.8l1.5 3.2 3.1.4-2.3 2.2.6 3.2-2.9-1.6-2.9 1.6.6-3.2-2.3-2.2 3.1-.4Z"/>'
                 '<path d="M6 19.4h12M8.4 21.6h7.2"/>',
    'veer': '<rect x="9.6" y="5.4" width="8.4" height="12.4" rx="1.4"/>'
            '<path d="M8.4 6.6 4.8 8.2l3.4 8.6" opacity=".75"/>'
            '<path d="M19.2 6.6l2.4 1.2-2.2 7" opacity=".55"/>'
            '<path d="M13.8 8.4v6.4M11.6 11.6h4.4"/>',
    'vopros': '<rect x="4.8" y="3.4" width="14.4" height="17.2" rx="2"/>'
              '<path d="M9.6 9.4a2.4 2.4 0 1 1 3.3 2.2c-.7.3-1.1 1-1.1 1.7v.5"/>'
              '<path d="M11.8 17.2h.02" stroke-width="2.2" stroke-linecap="round"/>',
    'lunnyj_krug': '<circle cx="12" cy="12" r="8.6"/><path d="M12 3.4a8.6 8.6 0 0 0 0 17.2Z"/>'
                   '<circle cx="12" cy="12" r="2"/>'
                   '<path d="M12 1.6v1.4M12 21v1.4M1.6 12h1.4M21 12h1.4"/>',
    # ведьмин дневник
    'obereg_dom': '<path d="M3.6 11.4 12 4.2l8.4 7.2"/><path d="M5.6 10v9.8h12.8V10"/>'
                  '<path d="M10 19.8v-5.2h4v5.2"/>'
                  '<path d="M12 7.2l.9 1.9 2 .3-1.5 1.4.4 2-1.8-1-1.8 1 .4-2-1.5-1.4 2-.3Z"/>',
    'nechist_les': '<path d="M12 2.8 7.4 9.6h2.6L6.2 15.4h3.4L6 20.6h12l-3.6-5.2h3.4L14.2 9.6h2.6Z"/>'
                   '<path d="M12 20.6v2"/><circle cx="10.2" cy="13.4" r=".8"/><circle cx="13.8" cy="13.4" r=".8"/>',
    'razbory': '<path d="M4 5.4c2.6-1.4 5.2-1.4 8 0v13.8c-2.8-1.4-5.4-1.4-8 0Z"/>'
               '<path d="M20 5.4c-2.6-1.4-5.2-1.4-8 0v13.8c2.8-1.4 5.4-1.4 8 0Z"/>'
               '<path d="M12 5.4v13.8"/><path d="M6.4 9.2h3M6.4 12.4h3M14.6 9.2h3M14.6 12.4h3"/>',
    'slovar_ikona': '<path d="M6.4 3.4h11.2a2 2 0 0 1 2 2v13.2a2 2 0 0 1-2 2H6.4Z"/>'
                    '<path d="M6.4 3.4a2 2 0 0 0-2 2v13.2a2 2 0 0 0 2 2"/>'
                    '<path d="M9.4 14.6 12 7.8l2.6 6.8M10.4 12.4h3.2"/>',
}


def mico(name):
    """Знак строки выпадающего меню."""
    d = MENU_ICONS.get(name)
    if not d:
        return ''
    return ('<svg class="mi" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            + d + '</svg>')
