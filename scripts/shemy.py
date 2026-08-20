# -*- coding: utf-8 -*-
"""Инфографика сайта: схемы на чистом SVG, в палитре сайта."""

Z = '#C9A227'      # золото
ZS = '#E3C15B'     # золото светлое
T = '#E9E3DA'      # текст
TT = '#A79E93'     # тихий
L = 'rgba(232,226,217,.16)'
F = "font-family:'Montserrat',sans-serif"
FS = "font-family:'Forum',Georgia,serif"


def _kuski(tekst):
    """Короткие слова (предлоги, союзы) склеиваем со следующим словом,
    чтобы строка не заканчивалась на «в», «и», «а»."""
    kuski = []
    for w in reversed(tekst.split()):
        if len(w) <= 2 and kuski and any(c.isalpha() for c in w):
            kuski[-1] = w + ' ' + kuski[-1]
        else:
            kuski.append(w)
    kuski.reverse()
    return kuski


def _zhadno(kuski, shirina):
    stroki, tek = [], ''
    for w in kuski:
        if tek and len(tek) + 1 + len(w) > shirina:
            stroki.append(tek)
            tek = w
        else:
            tek = (tek + ' ' + w).strip()
    if tek:
        stroki.append(tek)
    return stroki


def _stroki(tekst, max_znakov):
    """Режет строку по словам и выравнивает их по длине.
    Слово никогда не обрывается, одинокий хвост в одно короткое слово не остаётся."""
    kuski = _kuski(tekst)
    dlinnoe = max(len(k) for k in kuski)
    if dlinnoe > max_znakov:                     # склейка не влезла, режем по словам
        kuski = tekst.split()
        dlinnoe = max(len(k) for k in kuski)
    nado = len(_zhadno(kuski, max_znakov))
    nizhe, vyshe = min(dlinnoe, max_znakov), max_znakov
    while nizhe < vyshe:                          # ищем самую узкую строку при том же числе строк
        sred = (nizhe + vyshe) // 2
        if len(_zhadno(kuski, sred)) <= nado:
            vyshe = sred
        else:
            nizhe = sred + 1
    return _zhadno(kuski, nizhe)


def obertka(vnutri, vw=1000, vh=420, podpis='', s_nachala=False):
    """s_nachala: у схем с рядами читают слева направо, поэтому на узком экране
    такую схему открываем с начала, а рисунок по центру наводим по середине."""
    p = (f'<p class="shema-podpis">{podpis}</p>' if podpis else '')
    nach = ' data-nachalo="1"' if s_nachala else ''
    return (f'<figure class="shema"{nach}><svg viewBox="0 0 {vw} {vh}" role="img" '
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
                     f'style="{F};font-size:12.5px">{podpis}</text>')
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
    """Границы дома и чем их закрывали. Точки стоят на самом контуре,
    выноски уходят наружу и потому нигде не пересекают дом."""
    s = []
    # земля
    s.append(f'<line x1="330" y1="320" x2="710" y2="320" stroke="{Z}" stroke-width="2.4"/>')
    # стены и крыша
    s.append(f'<path d="M380 320 V170 H660 V320" fill="none" stroke="{L}" stroke-width="2"/>')
    s.append(f'<path d="M348 170 L520 80 L692 170" fill="none" stroke="{L}" stroke-width="2" '
             f'stroke-linejoin="round"/>')
    # труба над печью
    s.append(f'<path d="M600 122 V100 H632 V139" fill="none" stroke="{L}" stroke-width="2"/>')
    # печь внутри, под трубой
    s.append(f'<path d="M576 320 V264 H628 V320" fill="none" stroke="{L}" stroke-width="1.6"/>')
    s.append(f'<path d="M590 320 V298 a12 12 0 0 1 24 0 V320" fill="none" stroke="{Z}" '
             f'stroke-width="1.4" opacity=".7"/>')
    # дверь, порог у земли
    s.append(f'<path d="M490 320 V246 H550 V320" fill="none" stroke="{L}" stroke-width="1.8"/>')
    # окно у левой стены
    s.append(f'<rect x="404" y="196" width="60" height="48" rx="3" fill="none" stroke="{L}" '
             f'stroke-width="1.6"/>')
    s.append(f'<path d="M434 196 V244 M404 220 H464" stroke="{L}" stroke-width="1.2"/>')
    # красный угол: угол стены под крышей
    s.append(f'<path d="M660 196 H630 V170" fill="none" stroke="{Z}" stroke-width="1.4" opacity=".55"/>')

    def tochka(x, y):
        s.append(f'<circle cx="{x}" cy="{y}" r="6.5" fill="{Z}"/>')
        s.append(f'<circle cx="{x}" cy="{y}" r="13" fill="none" stroke="{Z}" stroke-width="1" opacity=".45"/>')

    def podpis(x, y, zag, txt, ank='start'):
        s.append(f'<text x="{x}" y="{y}" fill="{T}" text-anchor="{ank}" style="{FS};font-size:23px">{zag}</text>')
        s.append(f'<text x="{x}" y="{y + 25}" fill="{TT}" text-anchor="{ank}" style="{F};font-size:14.5px">{txt}</text>')

    # печь: точка на трубе, подпись справа сверху
    tochka(616, 100)
    s.append(f'<path d="M630 99 C 672 96, 700 94, 730 94" fill="none" stroke="{L}" stroke-width="1"/>')
    podpis(740, 100, 'Печь', 'угощение домовому')
    # красный угол: точка на верхнем углу стены, подпись справа
    tochka(660, 170)
    s.append(f'<path d="M673 173 C 700 182, 712 196, 730 204" fill="none" stroke="{L}" stroke-width="1"/>')
    podpis(740, 212, 'Красный угол', 'рушник и свеча')
    # окно: точка на левой стене, подпись слева
    tochka(380, 220)
    s.append(f'<path d="M206 220 H367" fill="none" stroke="{L}" stroke-width="1"/>')
    podpis(20, 214, 'Окно', 'громничная свеча')
    # порог: точка на земле под дверью, подпись слева внизу
    tochka(520, 320)
    s.append(f'<path d="M206 352 H500 C 512 352, 520 345, 520 333" fill="none" stroke="{L}" stroke-width="1"/>')
    podpis(20, 346, 'Порог', 'крапива, нож, соль')
    return obertka(''.join(s), 1000, 396,
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
                   'Порядок один во всех направлениях: сначала источник, потом руки, потом разбор.', s_nachala=True)


def put_duraka():
    """Путь Дурака: нулевая карта и три ряда по семь арканов.
    Имя карты переносится по словам, обрывать его нельзя."""
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'content'))
    from arkany import ARKANY
    ryady = [('Мир людей', ARKANY[1:8]), ('Мир испытаний', ARKANY[8:15]),
             ('Мир целого', ARKANY[15:22])]
    s = []
    # нулевая карта отдельно, над рядами
    s.append(f'<rect x="20" y="16" width="120" height="86" rx="10" fill="none" '
             f'stroke="{Z}" stroke-width="1.6"/>')
    s.append(f'<text x="80" y="56" text-anchor="middle" fill="{ZS}" style="{FS};font-size:28px">0</text>')
    s.append(f'<text x="80" y="84" text-anchor="middle" fill="{T}" style="{FS};font-size:19px">Шут</text>')
    s.append(f'<path d="M152 59 h30 m-9 -5.5 l9 5.5 -9 5.5" stroke="{Z}" stroke-width="1.4" fill="none"/>')
    s.append(f'<text x="196" y="52" fill="{T}" style="{FS};font-size:22px">Шут идёт вне счёта</text>')
    s.append(f'<text x="196" y="78" fill="{TT}" style="{F};font-size:14.5px">'
             'с него начинается дорога, номера у него нет</text>')
    for r, (nazv, ryad) in enumerate(ryady):
        y0 = 134 + r * 140
        s.append(f'<text x="20" y="{y0}" fill="{Z}" style="{FS};font-size:16px;'
                 f'letter-spacing:2.4px">{nazv.upper()}</text>')
        s.append(f'<line x1="20" y1="{y0 + 10}" x2="962" y2="{y0 + 10}" stroke="{L}" stroke-width="1"/>')
        for i, a in enumerate(ryad):
            x = 20 + i * 137
            s.append(f'<rect x="{x}" y="{y0 + 22}" width="120" height="86" rx="9" fill="none" '
                     f'stroke="{L}" stroke-width="1.2"/>')
            s.append(f'<text x="{x + 60}" y="{y0 + 60}" text-anchor="middle" fill="{ZS}" '
                     f'style="{FS};font-size:21px">{a["n"]}</text>')
            imya = _stroki(a['name'], 15)
            ty = y0 + 86 if len(imya) == 1 else y0 + 80
            for k, st in enumerate(imya):
                s.append(f'<text x="{x + 60}" y="{ty + k * 16}" text-anchor="middle" fill="{TT}" '
                         f'style="{F};font-size:12.5px">{st}</text>')
    return obertka(''.join(s), 1000, 548,
                   'Двадцать один аркан делится на три ряда по семь. Первый ряд про жизнь среди людей, '
                   'второй про испытания, третий про выход к целому.', s_nachala=True)


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


def timeline_iry(kratko=False):
    """Путь Иры: от первой колоды до школы. kratko=True даёт короткую ленту."""
    vehi = [
        ('11 лет', 'первая колода', 'Карты попали в руки и остались.'),
        ('23 года', 'практика', 'К ней начали приходить люди.'),
        ('2014', 'первый курс', 'Собран авторский курс, началось преподавание.'),
        ('Города', 'четыре страны', 'Москва, Петербург, Израиль, Париж.'),
        ('Сегодня', 'школа', 'Потоки в закрытых каналах, разбор работ.'),
    ]
    if kratko:
        vehi = [vehi[0], vehi[1], vehi[2], vehi[4]]
    n = len(vehi)
    shag = 780 // (n - 1)
    s = []
    s.append(f'<line x1="70" y1="120" x2="930" y2="120" stroke="{L}" stroke-width="2"/>')
    for i, (kogda, chto, opis) in enumerate(vehi):
        x = 110 + i * shag
        s.append(f'<circle cx="{x}" cy="120" r="9" fill="{Z}"/>')
        s.append(f'<circle cx="{x}" cy="120" r="19" fill="none" stroke="{Z}" stroke-width="1" opacity=".45"/>')
        s.append(f'<text x="{x}" y="82" text-anchor="middle" fill="{ZS}" style="{FS};font-size:25px">{kogda}</text>')
        s.append(f'<text x="{x}" y="170" text-anchor="middle" fill="{T}" style="{FS};font-size:18px">{chto}</text>')
        for j, st in enumerate(_stroki(opis, 24)):
            s.append(f'<text x="{x}" y="{196 + j * 19}" text-anchor="middle" fill="{TT}" '
                     f'style="{F};font-size:13px">{st}</text>')
    podpis = ('Первая колода в одиннадцать лет, практика с двадцати трёх, авторский курс с 2014 года.'
              if kratko else
              'Путь от первой колоды до школы занял больше двадцати лет.')
    return obertka(''.join(s), 1000, 270, podpis, s_nachala=True)


KURSY_RAZVILKA = [
    ('Колода дома есть, а читаю по чужим значениям', 'Таро', 'чтение колоды'),
    ('Практика уже есть, хочу собрать её в систему', 'Геката', 'ритуальная магия'),
    ('Тянет север и старые знаки', 'Руны', 'старший футарк'),
    ('В семье что-то делали с солью и ножом', 'Обереги дома', 'раздел журнала'),
    ('Вопросы стали свои, в общий канал их неловко', 'Личная работа', 'один на один'),
]


def kuda_idti():
    """Развилка: от вопроса читателя к направлению школы."""
    s = []
    ryady = [70, 165, 260, 355, 450]
    # узел вопроса
    s.append(f'<rect x="20" y="228" width="176" height="64" rx="14" fill="none" '
             f'stroke="{Z}" stroke-width="1.6"/>')
    s.append(f'<text x="108" y="268" text-anchor="middle" fill="{T}" '
             f'style="{FS};font-size:23px">Ваш вопрос</text>')
    s.append(f'<path d="M196 260 H228" stroke="{Z}" stroke-width="1.4" fill="none"/>')
    s.append(f'<line x1="228" y1="70" x2="228" y2="450" stroke="{L}" stroke-width="1.4"/>')
    for y, (vopros, kurs, chto) in zip(ryady, KURSY_RAZVILKA):
        s.append(f'<path d="M228 {y} C 258 {y}, 268 {y}, 296 {y}" fill="none" '
                 f'stroke="{L}" stroke-width="1.2"/>')
        s.append(f'<circle cx="228" cy="{y}" r="5" fill="{Z}"/>')
        stroki = _stroki(vopros, 36)
        ty = y + 7 if len(stroki) == 1 else y - 6
        for k, st in enumerate(stroki):
            s.append(f'<text x="308" y="{ty + k * 25}" fill="{T}" '
                     f'style="{F};font-size:16.5px">{st}</text>')
        s.append(f'<path d="M668 {y} h26 m-9 -5.5 l9 5.5 -9 5.5" stroke="{Z}" '
                 f'stroke-width="1.4" fill="none" opacity=".8"/>')
        s.append(f'<rect x="706" y="{y - 31}" width="274" height="62" rx="14" fill="none" '
                 f'stroke="{L}" stroke-width="1.4"/>')
        s.append(f'<text x="730" y="{y - 2}" fill="{ZS}" style="{FS};font-size:21px">{kurs}</text>')
        s.append(f'<text x="730" y="{y + 20}" fill="{TT}" style="{F};font-size:13.5px">{chto}</text>')
    return obertka(''.join(s), 1000, 500,
                   'Строгой лестницы в школе нет. Направление берут по своему вопросу, '
                   'а порядок дальше складывается сам.')


STUPENI_GRIMUARA = [
    'Подготовка и инструментарий',
    'Знакомство с эгрегором',
    'Двадцать два старших аркана',
    'Интуитивное чтение',
    'Диагностика магического негатива',
    'Расклады и коррекция',
    'Лёгкая ритуалика',
    'Зеркальные перекрёстки',
    'Сложная ритуальная работа',
]


def lenta_grimuara():
    """Девять ступеней курса лентой: три ряда по три, каждый ряд слева направо."""
    xs = [20, 350, 680]
    ys = [24, 172, 320]
    s = []
    for i, zag in enumerate(STUPENI_GRIMUARA):
        r, k = divmod(i, 3)
        x, y = xs[k], ys[r]
        s.append(f'<rect x="{x}" y="{y}" width="300" height="104" rx="14" fill="none" '
                 f'stroke="{L}" stroke-width="1.4"/>')
        s.append(f'<circle cx="{x + 44}" cy="{y + 52}" r="21" fill="none" stroke="{Z}" stroke-width="1.4"/>')
        s.append(f'<text x="{x + 44}" y="{y + 60}" text-anchor="middle" fill="{ZS}" '
                 f'style="{FS};font-size:21px">{i + 1}</text>')
        stroki = _stroki(zag, 22)
        ty = y + 60 if len(stroki) == 1 else y + 48
        for m, st in enumerate(stroki):
            s.append(f'<text x="{x + 82}" y="{ty + m * 24}" fill="{T}" '
                     f'style="{FS};font-size:19px">{st}</text>')
        if k < 2:                                   # стрелка к соседней ступени
            s.append(f'<path d="M{x + 306} {y + 52} h16 m-6 -5 l6 5 -6 5" stroke="{Z}" '
                     f'stroke-width="1.4" fill="none" opacity=".75"/>')
        elif r < 2:                                 # переход на следующий ряд
            s.append(f'<path d="M{x + 150} {y + 110} V{y + 130} H{xs[0] + 150} V{ys[r + 1] - 8} '
                     f'm-5 -6 l5 6 5 -6" stroke="{Z}" stroke-width="1.4" fill="none" opacity=".7"/>')
    return obertka(''.join(s), 1000, 448,
                   'Ступени идут подряд: сначала инструменты и сила за колодой, потом чтение '
                   'и диагностика, а сложная ритуальная работа только в конце.', s_nachala=True)


ZNAKI_PRIVYCHEK = [
    '<path d="M-11 -14h22v28h-22z"/><path d="M-6 0l4 5 8-11"/>',
    '<path d="M-11 -4a11.7 11.7 0 0 1 20-3"/><path d="M9 -7l-6 1M9 -7l1 6"/>'
    '<path d="M11 4a11.7 11.7 0 0 1-20 3"/><path d="M-9 7l6-1M-9 7l-1-6"/>',
    '<path d="M-11 -14h22v28h-22z"/><path d="M-6 -7h13M-6 0h13M-6 7h8"/>',
]

PRIVYCHKI = [
    ('Ответ придуман заранее',
     'Человек уже решил, что должно выпасть, и подбирает к этому карты. Расклад сходится, а толку нет.',
     'Покажи, где на картинке то, что ты сейчас сказал.'),
    ('Один вопрос по кругу',
     'Тот же вопрос перекладывают по второму и третьему разу, пока картинка не станет приятной.',
     'Звучит уже не «что здесь происходит», а «успокой меня».'),
    ('Чужие выписанные значения',
     'Значения выписаны из интернета в тетрадь, и человек говорит ими, а на карты почти не смотрит.',
     'Опиши выпавшее своими словами, будто рисунка никто не видел.'),
]


def privychki_novichka():
    """Три привычки, из-за которых расклад читается мимо."""
    s = []
    for i, (zag, telo, lovyat) in enumerate(PRIVYCHKI):
        x = 20 + i * 327
        s.append(f'<rect x="{x}" y="20" width="306" height="390" rx="18" fill="none" '
                 f'stroke="{L}" stroke-width="1.4"/>')
        s.append(f'<circle cx="{x + 56}" cy="82" r="30" fill="none" stroke="{Z}" stroke-width="1.4"/>')
        s.append(f'<g transform="translate({x + 56},82)" fill="none" stroke="{ZS}" stroke-width="1.8" '
                 f'stroke-linecap="round" stroke-linejoin="round">{ZNAKI_PRIVYCHEK[i]}</g>')
        s.append(f'<text x="{x + 268}" y="90" text-anchor="end" fill="{Z}" '
                 f'style="{FS};font-size:26px" opacity=".55">{i + 1}</text>')
        for j, st in enumerate(_stroki(zag, 23)):
            s.append(f'<text x="{x + 24}" y="{150 + j * 27}" fill="{T}" '
                     f'style="{FS};font-size:23px">{st}</text>')
        for j, st in enumerate(_stroki(telo, 32)):
            s.append(f'<text x="{x + 24}" y="{214 + j * 21}" fill="{TT}" '
                     f'style="{F};font-size:14.5px">{st}</text>')
        s.append(f'<line x1="{x + 24}" y1="300" x2="{x + 282}" y2="300" stroke="{L}" stroke-width="1"/>')
        s.append(f'<text x="{x + 24}" y="330" fill="{Z}" '
                 f'style="{F};font-size:12.5px;letter-spacing:1.6px">КАК ЛОВЯТ НА ЗАНЯТИИ</text>')
        for j, st in enumerate(_stroki(lovyat, 32)):
            s.append(f'<text x="{x + 24}" y="{358 + j * 21}" fill="{T}" '
                     f'style="{F};font-size:14px">{st}</text>')
    return obertka(''.join(s), 1000, 440,
                   'Три привычки, из-за которых расклад читается мимо. На занятиях их снимают '
                   'вопросом к самому раскладу, а не запретом.')
