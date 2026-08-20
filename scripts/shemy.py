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
    s.append(f'<path d="M120 300 L120 170 L330 60 L540 170 L540 300 Z" fill="none" '
             f'stroke="{L}" stroke-width="2"/>')
    s.append(f'<path d="M120 300 L540 300" stroke="{Z}" stroke-width="2.4"/>')
    # точки на доме и подписи справа на равных интервалах, без наложений
    tochki = [
        (330, 150, 'Печь', 'угощение домовому'),
        (200, 220, 'Окно', 'громничная свеча'),
        (470, 205, 'Красный угол', 'рушник и свеча'),
        (330, 300, 'Порог', 'крапива, нож, соль'),
    ]
    for i, (x, y, zag, txt) in enumerate(tochki):
        ly = 96 + i * 74
        s.append(f'<path d="M{x} {y} C {x + 90} {y}, 560 {ly}, 630 {ly}" fill="none" '
                 f'stroke="{L}" stroke-width="1"/>')
        s.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{Z}"/>')
        s.append(f'<circle cx="{x}" cy="{y}" r="14" fill="none" stroke="{Z}" stroke-width="1" opacity=".45"/>')
        s.append(f'<text x="646" y="{ly - 3}" fill="{T}" style="{FS};font-size:22px">{zag}</text>')
        s.append(f'<text x="646" y="{ly + 22}" fill="{TT}" style="{F};font-size:14.5px">{txt}</text>')
    return obertka(''.join(s), 1000, 380,
                   'Оберег ставили на границе дома: у порога, окна, красного угла и печи. '
                   'Там, где чужое могло войти внутрь.')


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


ZNAKI_PUTI = [
    '<path d="M-9 -12v24M-9 -7l11-5M-9 -1l11-5"/>',
    '<path d="M-9 12V-6c0-3.4 2.6-6 6-6h.6c3.4 0 6 2.6 6 6V12"/>',
    '<path d="M-9 -12v24M-9 -7l10 5.4-10 5.4"/>',
    '<path d="M-9 -12v24M-9 -7l10-4.4M-9 -0.6l10-4.4"/>',
    '<path d="M-9 -12v24M-9 -12h7.4a4.6 4.6 0 0 1 0 9.2H-9M-1.6 -2.8 4 12"/>',
]


def put_uchenika():
    """Как идёт поток."""
    shagi = [('Источник', 'откуда пришёл обряд'), ('Практика', 'делают руками'),
             ('Разбор', 'смотрят при всех'), ('Своя работа', 'ведут сами')]
    s = []
    s.append(f'<line x1="60" y1="110" x2="940" y2="110" stroke="{L}" stroke-width="2"/>')
    for i, (zag, txt) in enumerate(shagi):
        x = 100 + i * 267
        s.append(f'<circle cx="{x}" cy="110" r="34" fill="#16131C" stroke="{Z}" stroke-width="1.6"/>')
        s.append(f'<circle cx="{x}" cy="110" r="28" fill="none" stroke="{Z}" stroke-width=".8" opacity=".4"/>')
        s.append(f'<g transform="translate({x},110)" fill="none" stroke="{ZS}" stroke-width="2" '
                 f'stroke-linecap="round" stroke-linejoin="round">{ZNAKI_PUTI[i % len(ZNAKI_PUTI)]}</g>')
        s.append(f'<text x="{x}" y="182" fill="{T}" text-anchor="middle" style="{FS};font-size:23px">{zag}</text>')
        s.append(f'<text x="{x}" y="210" fill="{TT}" text-anchor="middle" style="{F};font-size:14px">{txt}</text>')
        if i < len(shagi) - 1:
            s.append(f'<path d="M{x + 46} 110 h175 m-12 -6 l12 6 -12 6" stroke="{Z}" '
                     f'stroke-width="1.4" fill="none" opacity=".65"/>')
    return obertka(''.join(s), 1000, 240,
                   'Порядок один во всех направлениях: сначала источник, потом руки, потом разбор.')


def put_duraka():
    """Путь Дурака: нулевая карта и три ряда по семь арканов."""
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'content'))
    from arkany import ARKANY
    ryady = [('Мир людей', ARKANY[1:8]), ('Мир испытаний', ARKANY[8:15]),
             ('Мир целого', ARKANY[15:22])]
    s = []
    # нулевая карта отдельно
    s.append(f'<rect x="20" y="86" width="92" height="132" rx="10" fill="none" '
             f'stroke="{Z}" stroke-width="1.6"/>')
    s.append(f'<text x="66" y="140" text-anchor="middle" fill="{ZS}" '
             f'style="{FS};font-size:30px">0</text>')
    s.append(f'<text x="66" y="172" text-anchor="middle" fill="{T}" style="{FS};font-size:17px">Шут</text>')
    s.append(f'<text x="66" y="242" text-anchor="middle" fill="{TT}" style="{F};font-size:12.5px">вне счёта</text>')
    s.append(f'<path d="M124 152 h26 m-8 -5 l8 5 -8 5" stroke="{Z}" stroke-width="1.4" fill="none"/>')
    for r, (nazv, ryad) in enumerate(ryady):
        y = 30 + r * 108
        s.append(f'<text x="168" y="{y + 14}" fill="{Z}" style="{FS};font-size:15px;'
                 f'letter-spacing:2px">{nazv.upper()}</text>')
        for i, a in enumerate(ryad):
            x = 168 + i * 116
            s.append(f'<rect x="{x}" y="{y + 24}" width="100" height="62" rx="8" fill="none" '
                     f'stroke="{L}" stroke-width="1.2"/>')
            s.append(f'<text x="{x + 50}" y="{y + 50}" text-anchor="middle" fill="{ZS}" '
                     f'style="{FS};font-size:19px">{a["n"]}</text>')
            s.append(f'<text x="{x + 50}" y="{y + 72}" text-anchor="middle" fill="{TT}" '
                     f'style="{F};font-size:11.5px">{a["name"][:13]}</text>')
    return obertka(''.join(s), 1000, 350,
                   'Двадцать один аркан делится на три ряда по семь. Первый ряд про жизнь среди людей, '
                   'второй про испытания, третий про выход к целому.')


def fazy_luny():
    """Восемь фаз луны по кругу и работа в каждой."""
    import math
    fazy = [
        ('Новолуние', 'замысел и тишина', 0.0),
        ('Молодая', 'первый шаг', 0.125),
        ('Первая четверть', 'усилие и правка', 0.25),
        ('Прибывающая', 'набор силы', 0.375),
        ('Полнолуние', 'пик и ясность', 0.5),
        ('Убывающая', 'отдача лишнего', 0.625),
        ('Последняя четверть', 'разбор итога', 0.75),
        ('Старая луна', 'покой перед новым', 0.875),
    ]
    cx, cy, r = 300, 190, 128
    s = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{L}" stroke-width="1.4"/>']
    for i, (nazv, delo, t) in enumerate(fazy):
        a = -math.pi / 2 + t * 2 * math.pi
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        # рисуем саму фазу кружком с тенью
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="17" fill="#0E0C11" stroke="{Z}" stroke-width="1.4"/>')
        if 0 < t < 0.5:
            s.append(f'<path d="M{x:.0f} {y - 17:.0f} A 17 17 0 0 1 {x:.0f} {y + 17:.0f} Z" fill="{ZS}" opacity=".9"/>')
        elif t == 0.5:
            s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="15" fill="{ZS}" opacity=".92"/>')
        elif t > 0.5:
            s.append(f'<path d="M{x:.0f} {y - 17:.0f} A 17 17 0 0 0 {x:.0f} {y + 17:.0f} Z" fill="{ZS}" opacity=".9"/>')
        # подпись в столбце справа
        ly = 46 + i * 42
        s.append(f'<text x="520" y="{ly}" fill="{T}" style="{FS};font-size:20px">{nazv}</text>')
        s.append(f'<text x="520" y="{ly + 20}" fill="{TT}" style="{F};font-size:13.5px">{delo}</text>')
        s.append(f'<circle cx="{500}" cy="{ly - 6}" r="4" fill="{Z}" opacity=".75"/>')
    s.append(f'<text x="{cx}" y="{cy - 6}" text-anchor="middle" fill="{Z}" '
             f'style="{FS};font-size:19px;letter-spacing:2px">ЛУННЫЙ</text>')
    s.append(f'<text x="{cx}" y="{cy + 20}" text-anchor="middle" fill="{Z}" '
             f'style="{FS};font-size:19px;letter-spacing:2px">КРУГ</text>')
    return obertka(''.join(s), 1000, 396,
                   'Круг занимает около двадцати девяти с половиной суток. Работа привязана '
                   'не к дню недели, а к тому, где сейчас луна.')


def timeline_iry():
    """Путь Иры: от первой колоды до школы."""
    vehi = [
        ('11 лет', 'первая колода', 'Карты попали в руки и остались.'),
        ('23 года', 'практика', 'К ней начали приходить люди.'),
        ('2014', 'первый курс', 'Собран авторский курс, началось преподавание.'),
        ('Города', 'четыре страны', 'Москва, Петербург, Израиль, Париж.'),
        ('Сегодня', 'школа', 'Потоки в закрытых каналах, разбор работ.'),
    ]
    s = []
    s.append(f'<line x1="70" y1="120" x2="930" y2="120" stroke="{L}" stroke-width="2"/>')
    for i, (kogda, chto, opis) in enumerate(vehi):
        x = 110 + i * 195
        s.append(f'<circle cx="{x}" cy="120" r="9" fill="{Z}"/>')
        s.append(f'<circle cx="{x}" cy="120" r="19" fill="none" stroke="{Z}" stroke-width="1" opacity=".45"/>')
        s.append(f'<text x="{x}" y="82" text-anchor="middle" fill="{ZS}" style="{FS};font-size:25px">{kogda}</text>')
        s.append(f'<text x="{x}" y="170" text-anchor="middle" fill="{T}" style="{FS};font-size:18px">{chto}</text>')
        slova = opis.split()
        stroki, tek = [], ''
        for w in slova:
            if len(tek + ' ' + w) > 24:
                stroki.append(tek); tek = w
            else:
                tek = (tek + ' ' + w).strip()
        stroki.append(tek)
        for j, st in enumerate(stroki):
            s.append(f'<text x="{x}" y="{196 + j * 19}" text-anchor="middle" fill="{TT}" '
                     f'style="{F};font-size:13px">{st}</text>')
    return obertka(''.join(s), 1000, 270,
                   'Путь от первой колоды до школы занял больше двадцати лет.')
