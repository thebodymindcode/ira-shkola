# -*- coding: utf-8 -*-
"""Движок сайта школы Ирины Волковой: шаблон, стили, типографика."""
import re

BASE = '/ira-shkola/'
VERSION = '2026082010'
DOMAIN = 'https://thebodymindcode.github.io/ira-shkola'
TITLE_SITE = 'Школа Ирины Волковой'
TG = 'https://t.me/ira_volkova_taro'
IG = 'https://www.instagram.com/theiravolkova/'

NB = ' '

MENU = [
    ('Главная', ''),
    ('Школа', 'shkola/'),
    ('Курсы', 'kursy/'),
    ('Таро', 'taro/'),
    ('Журнал', 'zhurnal/'),
    ('Об Ирине', 'ob-irine/'),
    ('Контакты', 'kontakty/'),
]

FOOTER_LINKS = [
    ('Главная', ''), ('Школа', 'shkola/'), ('Курсы', 'kursy/'),
    ('Геката', 'kursy/gekata/'), ('Руны', 'kursy/runy/'), ('Бесы', 'kursy/besy/'),
    ('Наставничество', 'kursy/nastavnichestvo/'), ('Таро', 'taro/'),
    ('Обереги дома', 'oberegi/'), ('Нечисть', 'nechist/'), ('Журнал', 'zhurnal/'),
    ('Об Ирине', 'ob-irine/'), ('Вопросы', 'vopros-otvet/'), ('Контакты', 'kontakty/'),
]

# ---------------------------------------------------------------- типографика
SHORT = ('и в во на не но с со к ко о об от до за из у я по для при над под без'
         ' же ли бы то а как что чем чуть уже ещё их его её их их').split()
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
    pat = r'(^|[\s(«—,.;:!?])(' + '|'.join(SHORT + NUMWORDS) + r')\s+'
    for _ in range(3):
        t = re.sub(pat, glue, t, flags=re.IGNORECASE)
    return t

def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))

# ---------------------------------------------------------------- иконки
ICONS = {
 'luna': '<path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a6.8 6.8 0 0 0 10.5 10.5Z"/>',
 'klyuch': '<circle cx="8" cy="8" r="3.6"/><path d="M10.6 10.6 20 20m-3-3 2-2m-4 1 1.6-1.6"/>',
 'svecha': '<path d="M12 3c1.8 1.9 2.7 3.3 2.7 4.4a2.7 2.7 0 1 1-5.4 0C9.3 6.3 10.2 4.9 12 3Z"/><rect x="8.6" y="11.4" width="6.8" height="9.6" rx="1.4"/>',
 'kniga': '<path d="M4 5.2A2.2 2.2 0 0 1 6.2 3H19v15H6.2A2.2 2.2 0 0 0 4 20.2Z"/><path d="M4 20.2A2.2 2.2 0 0 1 6.2 18H19v3H6.2A2.2 2.2 0 0 1 4 20.2Z"/>',
 'karta': '<rect x="4.4" y="3" width="11" height="15.6" rx="1.8"/><path d="M8.2 21.2h9a2 2 0 0 0 2-2V7.6"/>',
 'runa': '<path d="M7 3v18M7 9l8-6M7 13l8 6"/>',
 'dom': '<path d="M4 11 12 4l8 7"/><path d="M6.4 10.2V20h11.2v-9.8"/><path d="M10.2 20v-5.2h3.6V20"/>',
 'ogon': '<path d="M12 21c3.6 0 6-2.3 6-5.6 0-4-4-5.6-3.4-10.4C11.8 6.2 9.4 8.6 9.4 11c0 1.3.5 2.2.5 2.8 0 1-.8 1.6-1.6 1.1-.9-.6-1.1-1.9-1.1-2.6C6.2 13.6 6 14.7 6 15.9 6 18.9 8.4 21 12 21Z"/>',
 'krug': '<circle cx="12" cy="12" r="8.4"/><circle cx="12" cy="12" r="3.2"/>',
 'ruka': '<path d="M9 11V5.4a1.6 1.6 0 0 1 3.2 0V11m0-1.2a1.6 1.6 0 0 1 3.2 0V12"/><path d="M15.4 11.4a1.6 1.6 0 0 1 3.2 0V15c0 3.4-2.4 6-6 6-2.4 0-3.8-1-5.2-3l-2.2-3.4a1.6 1.6 0 0 1 2.5-2L9 14.2V9.8"/>',
 'glaz': '<path d="M2.6 12S6.4 5.6 12 5.6 21.4 12 21.4 12 17.6 18.4 12 18.4 2.6 12 2.6 12Z"/><circle cx="12" cy="12" r="2.8"/>',
 'chas': '<circle cx="12" cy="12" r="8.4"/><path d="M12 7.2V12l3.2 2"/>',
 'nit': '<path d="M4 6c4 0 4 12 8 12s4-12 8-12"/>',
 'sol': '<path d="M12 3.4 20 8v8l-8 4.6L4 16V8Z"/><circle cx="12" cy="12" r="2.4"/>',
 'zerkalo': '<ellipse cx="12" cy="9.6" rx="6" ry="6.6"/><path d="M12 16.2V21m-2.6 0h5.2"/>',
 'les': '<path d="M12 3 6.6 11h3L5 18.2h14L14.4 11h3Z"/><path d="M12 18.2V21"/>',
 'voda': '<path d="M12 3.4c3.6 4.2 5.4 7 5.4 9.4a5.4 5.4 0 0 1-10.8 0c0-2.4 1.8-5.2 5.4-9.4Z"/>',
 'strela': '<path d="M5 12h13m-5-5.4L18.6 12 13 17.4"/>',
 'tg': '<path d="M20.6 4.4 2.9 11.2c-1 .4-1 1 .1 1.3l4.4 1.4 1.7 5.2c.3.7.6.8 1.1.3l2.5-2.4 4.6 3.4c.9.5 1.4.2 1.6-.8l2.7-12.7c.2-1-.4-1.5-1-1.2Z"/>',
 'ig': '<rect x="3.4" y="3.4" width="17.2" height="17.2" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="7" r="1.1"/>',
}

def ico(name, cls='ic'):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{ICONS.get(name, ICONS["krug"])}</svg>')
