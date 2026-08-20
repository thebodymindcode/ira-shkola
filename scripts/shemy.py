# -*- coding: utf-8 -*-
"""Инфографика сайта: схемы на чистом SVG, в палитре сайта."""

Z = '#C9A227'      # золото
ZS = '#E3C15B'     # золото светлое
T = '#E9E3DA'      # текст
TT = '#A79E93'     # тихий
L = 'rgba(232,226,217,.16)'
F = "font-family:'Montserrat',sans-serif"
FS = "font-family:'Forum',Georgia,serif"


def obertka(vnutri, vw=1000, vh=420, podpis=''):
    p = (f'<p class="shema-podpis">{podpis}</p>' if podpis else '')
    return (f'<figure class="shema"><svg viewBox="0 0 {vw} {vh}" role="img" '
            f'preserveAspectRatio="xMidYMid meet">{vnutri}</svg>{p}</figure>')


def koloda():
    """Строение колоды таро: 22 старших и 56 младших по четырём мастям."""
    s = []
    # старшие
    s.append(f'<text x="20" y="34" fill="{Z}" style="{FS};font-size:19px;letter-spacing:2px">'
             'СТАРШИЕ АРКАНЫ · 22</text>')
    for i in range(22):
        x = 20 + i * 44
        s.append(f'<rect x="{x}" y="50" width="34" height="52" rx="5" fill="none" '
                 f'stroke="{Z}" stroke-width="1.4" opacity=".85"/>')
        s.append(f'<text x="{x + 17}" y="82" fill="{ZS}" text-anchor="middle" '
                 f'style="{F};font-size:12px">{i}</text>')
    # младшие
    s.append(f'<text x="20" y="152" fill="{Z}" style="{FS};font-size:19px;letter-spacing:2px">'
             'МЛАДШИЕ АРКАНЫ · 56</text>')
    masti = [('Жезлы', 'огонь'), ('Кубки', 'вода'), ('Мечи', 'воздух'), ('Пентакли', 'земля')]
    for r, (mast, stihiya) in enumerate(masti):
        y = 176 + r * 58
        s.append(f'<text x="20" y="{y + 26}" fill="{T}" style="{F};font-size:15px">{mast}</text>')
        s.append(f'<text x="120" y="{y + 26}" fill="{TT}" style="{F};font-size:13px">{stihiya}</text>')
        for i in range(14):
            x = 220 + i * 52
            s.append(f'<rect x="{x}" y="{y + 8}" width="40" height="26" rx="4" fill="none" '
                     f'stroke="{L}" stroke-width="1.2"/>')
            podpis = str(i + 1) if i < 10 else ['В', 'Р', 'Д', 'К'][i - 10]
            s.append(f'<text x="{x + 20}" y="{y + 26}" fill="{TT}" text-anchor="middle" '
                     f'style="{F};font-size:11.5px">{podpis}</text>')
    s.append(f'<text x="220" y="418" fill="{TT}" style="{F};font-size:12px">'
             'В, Р, Д, К это Валет, Рыцарь, Дама и Король</text>')
    return obertka(''.join(s), 1000, 430,
                   'Семьдесят восемь карт: двадцать два старших аркана и четыре масти по четырнадцать карт.')


def etty():
    """Три этта старшего футарка."""
    imena = [
        ['феху', 'уруз', 'турисаз', 'ансуз', 'райдо', 'кеназ', 'гебо', 'вуньо'],
        ['хагалаз', 'наутиз', 'иса', 'йера', 'эйваз', 'перто', 'альгиз', 'соулу'],
        ['тейваз', 'беркана', 'эваз', 'манназ', 'лагуз', 'ингуз', 'дагаз', 'отала'],
    ]
    s = []
    for r, ryad in enumerate(imena):
        y = 34 + r * 128
        s.append(f'<text x="20" y="{y}" fill="{Z}" style="{FS};font-size:18px;letter-spacing:2px">'
                 f'ЭТТ {r + 1}</text>')
        s.append(f'<line x1="20" y1="{y + 12}" x2="980" y2="{y + 12}" stroke="{L}" stroke-width="1"/>')
        for i, im in enumerate(ryad):
            x = 20 + i * 121
            s.append(f'<rect x="{x}" y="{y + 26}" width="104" height="62" rx="8" fill="none" '
                     f'stroke="{Z}" stroke-width="1.2" opacity=".7"/>')
            s.append(f'<text x="{x + 52}" y="{y + 58}" fill="{ZS}" text-anchor="middle" '
                     f'style="{FS};font-size:22px">{r * 8 + i + 1}</text>')
            s.append(f'<text x="{x + 52}" y="{y + 78}" fill="{TT}" text-anchor="middle" '
                     f'style="{F};font-size:12px">{im}</text>')
    return obertka(''.join(s), 1000, 400,
                   'Двадцать четыре знака идут тремя рядами по восемь. Ряд принято называть эттом.')


def dom_granicy():
    """Границы дома и чем их закрывали."""
    s = []
    # силуэт избы
    s.append(f'<path d="M120 300 L120 170 L330 60 L540 170 L540 300 Z" fill="none" '
             f'stroke="{L}" stroke-width="2"/>')
    s.append(f'<path d="M120 300 L540 300" stroke="{Z}" stroke-width="2"/>')
    tochki = [
        (330, 300, 'Порог', 'крапива, нож, соль', 'низ'),
        (200, 220, 'Окно', 'громничная свеча', 'lev'),
        (470, 205, 'Красный угол', 'рушник и свеча', 'prav'),
        (330, 150, 'Печь', 'угощение домовому', 'verh'),
    ]
    for x, y, zag, txt, storona in tochki:
        s.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{Z}"/>')
        s.append(f'<circle cx="{x}" cy="{y}" r="15" fill="none" stroke="{Z}" stroke-width="1" opacity=".5"/>')
        if storona == 'lev':
            lx, ly, ank = 640, y, 'start'
            s.append(f'<path d="M{x + 16} {y} H620" stroke="{L}" stroke-width="1"/>')
        elif storona == 'prav':
            lx, ly, ank = 640, y, 'start'
            s.append(f'<path d="M{x + 16} {y} H620" stroke="{L}" stroke-width="1"/>')
        elif storona == 'verh':
            lx, ly, ank = 640, y, 'start'
            s.append(f'<path d="M{x + 16} {y} H620" stroke="{L}" stroke-width="1"/>')
        else:
            lx, ly, ank = 640, y, 'start'
            s.append(f'<path d="M{x + 16} {y} H620" stroke="{L}" stroke-width="1"/>')
        s.append(f'<text x="{lx}" y="{ly - 4}" fill="{T}" text-anchor="{ank}" '
                 f'style="{FS};font-size:21px">{zag}</text>')
        s.append(f'<text x="{lx}" y="{ly + 18}" fill="{TT}" text-anchor="{ank}" '
                 f'style="{F};font-size:14px">{txt}</text>')
    return obertka(''.join(s), 1000, 360,
                   'Оберег ставили не в доме вообще, а на границе: у порога, окна, красного угла и печи.')


def mesta_nechisti():
    """Где кто живёт: места и часы."""
    mesta = [
        ('Дом', 'домовой, кикимора, мара', 'ночь'),
        ('Двор и хлев', 'дворовой, овинник', 'сумерки'),
        ('Баня', 'банник', 'после третьего пара'),
        ('Поле', 'полевик, полудница', 'полдень'),
        ('Лес', 'леший, волколак', 'любое время'),
        ('Вода', 'водяной, русалка', 'ночь и полдень'),
    ]
    s = []
    for i, (mesto, kto, chas) in enumerate(mesta):
        x = 20 + (i % 3) * 327
        y = 24 + (i // 3) * 170
        s.append(f'<rect x="{x}" y="{y}" width="300" height="146" rx="14" fill="none" '
                 f'stroke="{L}" stroke-width="1.4"/>')
        s.append(f'<path d="M{x} {y + 14} v-8 a14 14 0 0 1 14 -6 h40" stroke="{Z}" '
                 f'stroke-width="2" fill="none"/>')
        s.append(f'<text x="{x + 22}" y="{y + 48}" fill="{T}" style="{FS};font-size:24px">{mesto}</text>')
        s.append(f'<text x="{x + 22}" y="{y + 82}" fill="{TT}" style="{F};font-size:14px">{kto}</text>')
        s.append(f'<text x="{x + 22}" y="{y + 118}" fill="{Z}" style="{F};font-size:12.5px;'
                 f'letter-spacing:1.4px">{chas.upper()}</text>')
    return obertka(''.join(s), 1000, 380,
                   'У каждого своё место и свой час. Половина запретов держится именно на времени суток.')


def put_uchenika():
    """Как идёт поток."""
    shagi = [('Источник', 'откуда пришёл обряд'), ('Практика', 'делают руками'),
             ('Разбор', 'смотрят при всех'), ('Своя работа', 'ведут сами')]
    s = []
    s.append(f'<line x1="60" y1="110" x2="940" y2="110" stroke="{L}" stroke-width="2"/>')
    for i, (zag, txt) in enumerate(shagi):
        x = 100 + i * 267
        s.append(f'<circle cx="{x}" cy="110" r="34" fill="#16131C" stroke="{Z}" stroke-width="1.6"/>')
        s.append(f'<text x="{x}" y="119" fill="{ZS}" text-anchor="middle" style="{FS};font-size:26px">{i + 1}</text>')
        s.append(f'<text x="{x}" y="182" fill="{T}" text-anchor="middle" style="{FS};font-size:23px">{zag}</text>')
        s.append(f'<text x="{x}" y="210" fill="{TT}" text-anchor="middle" style="{F};font-size:14px">{txt}</text>')
        if i < len(shagi) - 1:
            s.append(f'<path d="M{x + 46} 110 h175 m-12 -6 l12 6 -12 6" stroke="{Z}" '
                     f'stroke-width="1.4" fill="none" opacity=".65"/>')
    return obertka(''.join(s), 1000, 240,
                   'Порядок один во всех направлениях: сначала источник, потом руки, потом разбор.')
