# -*- coding: utf-8 -*-
"""Готовит 22 старших аркана колоды Уэйта-Смита 1909 года под тёмный сайт.

Оригиналы (общественное достояние, Wikimedia Commons) лежат в _karty_src/.
Каждая карта светлая, а сайт ночной, поэтому карта кладётся на притемнённое
поле: тёплое свечение под картой, мягкая тень, золотая нить по кромке и
тонкая золотая рамка по краю кадра. Все 22 файла выходят одного размера,
пропорция карты не трогается: она вписывается целиком, без среза и растяжки.
"""
from PIL import Image, ImageDraw, ImageFilter
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'content'))
from arkany import ARKANY

SRC = '_karty_src'
OUT = 'images/karty'

# имена файлов Commons по номеру аркана
FAJLY = {
 0: 'RWS_Tarot_00_Fool.jpg',            1: 'RWS_Tarot_01_Magician.jpg',
 2: 'RWS_Tarot_02_High_Priestess.jpg',  3: 'RWS_Tarot_03_Empress.jpg',
 4: 'RWS_Tarot_04_Emperor.jpg',         5: 'RWS_Tarot_05_Hierophant.jpg',
 6: 'RWS_Tarot_06_Lovers.jpg',          7: 'RWS_Tarot_07_Chariot.jpg',
 8: 'RWS_Tarot_08_Strength.jpg',        9: 'RWS_Tarot_09_Hermit.jpg',
 10: 'RWS_Tarot_10_Wheel_of_Fortune.jpg', 11: 'RWS_Tarot_11_Justice.jpg',
 12: 'RWS_Tarot_12_Hanged_Man.jpg',     13: 'RWS_Tarot_13_Death.jpg',
 14: 'RWS_Tarot_14_Temperance.jpg',     15: 'RWS_Tarot_15_Devil.jpg',
 16: 'RWS_Tarot_16_Tower.jpg',          17: 'RWS_Tarot_17_Star.jpg',
 18: 'RWS_Tarot_18_Moon.jpg',           19: 'RWS_Tarot_19_Sun.jpg',
 20: 'RWS_Tarot_20_Judgement.jpg',      21: 'RWS_Tarot_21_World.jpg',
}

W, H = 900, 1420          # кадр один на все карты
POLE_X = 96               # поле слева и справа: у всех карт одинаковое
UGOL = 14                 # скругление самой карты
RAMKA = 46                # золотая нить по краю кадра, одинаково у всех 22 карт
ZOLOTO = (201, 162, 39)
VERH, NIZ = (31, 26, 42), (12, 10, 16)   # градиент поля
MINI = 'images/karty/mini'
MINI_W = 380


def fon():
    """Ночное поле: градиент, тёплое свечение по центру, тень по углам."""
    f = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(f)
    for y in range(H):
        k = y / (H - 1)
        d.line([(0, y), (W, y)],
               fill=tuple(int(VERH[i] + (NIZ[i] - VERH[i]) * k) for i in range(3)))
    m = (W // 4, H // 4)
    sv = Image.new('L', m, 0)
    ImageDraw.Draw(sv).ellipse([m[0] * 0.06, m[1] * 0.12, m[0] * 0.94, m[1] * 0.88], fill=120)
    sv = sv.filter(ImageFilter.GaussianBlur(22)).resize((W, H), Image.LANCZOS)
    f.paste(Image.new('RGB', (W, H), (104, 79, 34)), (0, 0), sv)
    vin = Image.new('L', m, 255)
    ImageDraw.Draw(vin).rounded_rectangle([m[0] * 0.04, m[1] * 0.03, m[0] * 0.96, m[1] * 0.97],
                                          int(m[0] * 0.1), fill=0)
    vin = vin.filter(ImageFilter.GaussianBlur(14)).resize((W, H), Image.LANCZOS)
    f.paste(Image.new('RGB', (W, H), (6, 5, 8)), (0, 0), vin)
    return f


def skruglit(razmer, r, otstup=0):
    m = Image.new('L', razmer, 0)
    ImageDraw.Draw(m).rounded_rectangle([otstup, otstup, razmer[0] - 1 - otstup,
                                         razmer[1] - 1 - otstup], r, fill=255)
    return m


def sobrat(src, dst, mini_dst):
    karta = Image.open(src).convert('RGB')
    kw, kh = karta.size
    # ширина у всех одна, пропорция файла не трогается: ни среза, ни растяжки
    nw = W - 2 * POLE_X
    nh = int(round(kh * nw / kw))
    karta = karta.resize((nw, nh), Image.LANCZOS)
    x, y = POLE_X, (H - nh) // 2

    kadr = fon()

    ten = Image.new('L', (W, H), 0)
    ImageDraw.Draw(ten).rounded_rectangle([x - 6, y - 2, x + nw + 6, y + nh + 14],
                                          UGOL + 8, fill=170)
    ten = ten.filter(ImageFilter.GaussianBlur(20))
    kadr.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), ten)

    kadr.paste(karta, (x, y), skruglit(karta.size, UGOL))

    sloj = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(sloj)
    # кромку карты подчёркиваем тонкой тёмной линией, чтобы белое не растекалось
    d.rounded_rectangle([x, y, x + nw - 1, y + nh - 1], UGOL, outline=(0, 0, 0, 90), width=2)
    # золотая нить по краю кадра: у всех карт она стоит одинаково
    d.rounded_rectangle([RAMKA, RAMKA, W - 1 - RAMKA, H - 1 - RAMKA], 18,
                        outline=ZOLOTO + (140,), width=2)
    kadr = Image.alpha_composite(kadr.convert('RGBA'), sloj).convert('RGB')

    kadr.save(dst, 'JPEG', quality=86, optimize=True, progressive=True)
    mini = kadr.resize((MINI_W, int(round(H * MINI_W / W))), Image.LANCZOS)
    mini.save(mini_dst, 'JPEG', quality=84, optimize=True, progressive=True)
    return kadr.size


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(MINI, exist_ok=True)
    n = 0
    for a in ARKANY:
        src = os.path.join(SRC, FAJLY[a['n']])
        if not os.path.exists(src):
            raise SystemExit('нет оригинала: ' + src)
        dst = os.path.join(OUT, a['slug'] + '.jpg')
        mini_dst = os.path.join(MINI, a['slug'] + '.jpg')
        r = sobrat(src, dst, mini_dst)
        n += 1
        print(f'{a["slug"]:16} {r[0]}x{r[1]}  {os.path.getsize(dst) // 1024} КБ  '
              f'мини {os.path.getsize(mini_dst) // 1024} КБ')
    print('карт готово:', n)


if __name__ == '__main__':
    main()
