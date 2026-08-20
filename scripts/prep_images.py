# -*- coding: utf-8 -*-
"""Готовит картинки сайта: кадры статей 16:9 и образы Иры под страницы."""
from PIL import Image, ImageFilter, ImageDraw
import os, shutil

OBR = os.path.expanduser('~/Instagram-Irina-Volkova/ФОТО-ОБРАЗЫ-ТАРО')
os.makedirs('images/obrazy', exist_ok=True)

def polosa_portreta(src_path, out, dolya=0.72, verh=0.0, zapas=0.07):
    """Полоса шапки: портрет целиком справа на размытой подложке.
    Так лицо не режется ни сверху, ни сбоку, а слева остаётся место под текст."""
    W, H = 2400, 1000
    im = Image.open(src_path).convert('RGB')
    Wi, Hi = im.size
    th = int(Hi * dolya)
    top = int(Hi * verh)
    kadr = im.crop((0, top, Wi, min(Hi, top + th)))
    hp = int(H * (1 - zapas))
    k = hp / kadr.size[1]
    kadr = kadr.resize((int(kadr.size[0] * k), hp), Image.LANCZOS)
    fon = im.crop((0, top, Wi, min(Hi, top + th))).resize((W, H), Image.LANCZOS)
    fon = fon.filter(ImageFilter.GaussianBlur(40))
    fon = Image.blend(fon, Image.new('RGB', (W, H), (14, 12, 17)), 0.74)
    x = W - kadr.size[0] - int(W * 0.02)
    y = H - hp
    maska = Image.new('L', (kadr.size[0], hp), 255)
    d = ImageDraw.Draw(maska)
    for i in range(280):
        d.line([(i, 0), (i, hp)], fill=int(255 * i / 280))
    verh_maska = Image.new('L', (kadr.size[0], hp), 255)
    dv = ImageDraw.Draw(verh_maska)
    for j in range(150):
        dv.line([(0, j), (kadr.size[0], j)], fill=int(255 * j / 150))
    maska = Image.composite(maska, Image.new('L', maska.size, 0), verh_maska)
    fon.paste(kadr, (x, y), maska)
    fon.save(out, quality=86, optimize=True)



def bezopasnyj_portret(src_path, out, W=1000, H=1500, vozduh_verh=0.15, vozduh_niz=0.05):
    """Портрет для колонки текста: фигура целиком внутри кадра, сверху воздух.
    Колонка тянется по высоте текста и режет картинку по краям, поэтому лицо
    держим с запасом: срез съедает воздух, а не голову."""
    im = Image.open(src_path).convert('RGB')
    Wi, Hi = im.size
    hp = int(H * (1 - vozduh_verh - vozduh_niz))
    k = hp / Hi
    kadr = im.resize((max(1, int(Wi * k)), hp), Image.LANCZOS)
    fon = crop_ratio(im, W / H, sverhu=0.5).resize((W, H), Image.LANCZOS)
    fon = fon.filter(ImageFilter.GaussianBlur(46))
    fon = Image.blend(fon, Image.new('RGB', (W, H), (14, 12, 17)), 0.6)
    x = (W - kadr.size[0]) // 2
    y = int(H * vozduh_verh)
    if kadr.size[0] <= W:
        maska = Image.new('L', kadr.size, 255)
        d = ImageDraw.Draw(maska)
        pero = max(40, int(kadr.size[0] * 0.06))
        for i in range(pero):
            v = int(255 * i / pero)
            d.line([(i, 0), (i, hp)], fill=v)
            d.line([(kadr.size[0] - 1 - i, 0), (kadr.size[0] - 1 - i, hp)], fill=v)
        fon.paste(kadr, (x, y), maska)
    else:
        obr = kadr.crop(((kadr.size[0] - W) // 2, 0, (kadr.size[0] - W) // 2 + W, hp))
        fon.paste(obr, (0, y))
    fon.save(out, quality=86, optimize=True)


def centr_lica(im):
    """Ищет вертикальный центр кожи: по нему кадрируем, чтобы лицо не резалось.
    Возвращает долю высоты (0..1) или None, если кожи в кадре нет."""
    m = im.convert('RGB').resize((160, int(160 * im.size[1] / im.size[0])))
    px = m.load()
    w, h = m.size
    stroki = []
    for y in range(h):
        n = 0
        for x in range(w):
            r, g, b = px[x, y]
            if r > 80 and g > 45 and b > 30 and r > g > b and r - b > 18 and abs(r - g) > 8:
                n += 1
        stroki.append(n)
    vsego = sum(stroki)
    if vsego < w * h * 0.02:
        return None
    # медиана по массе кожи
    nakop, cel = 0, vsego / 2
    for y, n in enumerate(stroki):
        nakop += n
        if nakop >= cel:
            return y / h
    return None


def crop_ratio(im, ratio, sverhu=1 / 3):
    """sverhu: доля высоты, с которой начинается срез. Для портретов берём выше центра,
    иначе лицо режется по глазам."""
    w, h = im.size
    tw, th = (w, int(w / ratio)) if w / h < ratio else (int(h * ratio), h)
    left = (w - tw) // 2
    top = int((h - th) * sverhu) if h > th else 0
    return im.crop((left, top, left + tw, top + th))

# 1. кадры статей до 1200x675
n = 0
for f in sorted(os.listdir('images/zhurnal')):
    if not f.endswith('.jpg'):
        continue
    p = 'images/zhurnal/' + f
    im = Image.open(p).convert('RGB')
    im = crop_ratio(im, 16 / 9).resize((1800, 1012), Image.LANCZOS)
    im.save(p, quality=82, optimize=True)
    n += 1

# 2. два кадра из образов для статей без видео


# 3. образы под страницы: широкий (16:9) и портретный (3:4)
# карточки и шапки курсов идут из сгенерированных сцен в _generacii (Runway, 20.08.2026)
SCENY = {
    'k-gekata': 'b-gekata.png', 'k-runy': 'b-runy.png', 'k-besy': 'b-besy.png',
    'k-nastav': 'b-nastav.png', 'k-taro': 'b-taro.png', 'k-oberegi': 'b-oberegi.png',
}
# шапки страниц: сцены без людей, поэтому лицо нигде не режется
SCENY_SHAPOK = {
    'h-kursy': 'b-kursy.png', 'h-oberegi': 'b-oberegi.png',
    'h-nechist': 'b-nechist.png', 'h-vopros': 'b-vopros.png',
    'h-zhurnal': 'h2-zhurnal.png',
}
STATI_SCENY = {'01-leshy': 'b-leshy.png', '03-vodyanoy': 'b-vodyanoy.png'}

WIDE = {
    # шапки страниц
    'h-glavnaya': '14-krug-svechej.jpg', 'h-kursy': '14-krug-svechej.jpg',
    'h-shkola': '12-luna-nad-vodoj.jpg', 'h-taro': '26-svecha-taro.jpg',
    'h-zhurnal': '24-taro-stena.jpg', 'h-oberegi': '05-svecha-fazy-luny.jpg',
    'h-nechist': '15-lico-iz-dyma.jpg', 'h-vopros': '19-svechi-karta.jpg',
    'h-kontakty': '20-svechi-plamya.jpg', 'h-irina': '21-svechi-oglyanulas.jpg',
    # карточки разделов в журнале
    'z-oberegi': '05-svecha-fazy-luny.jpg', 'z-nechist': '09-voron.jpg',
}
PORTRET = {
    'p-glavnaya': '10-hrustalnyj-shar.jpg', 'p-irina1': '02-karta-u-lica.jpg',
    'p-irina2': '13-ogonyok-v-ladoni.jpg', 'p-shkola': '04-tasuet-kolodu.jpg',
    'p-taro': '25-taro-levitaciya.jpg',
}
for name, src in SCENY.items():
    p = os.path.join('_generacii', src)
    if os.path.exists(p):
        im = Image.open(p).convert('RGB')
        crop_ratio(im, 16 / 9).resize((2200, 1238), Image.LANCZOS).save(
            f'images/obrazy/{name}.jpg', quality=84, optimize=True)
        n += 1
for name, src in STATI_SCENY.items():
    p = os.path.join('_generacii', src)
    if os.path.exists(p):
        im = Image.open(p).convert('RGB')
        crop_ratio(im, 16 / 9).resize((1800, 1012), Image.LANCZOS).save(
            f'images/zhurnal/{name}.jpg', quality=84, optimize=True)
        n += 1

for name, src in SCENY_SHAPOK.items():
    p = os.path.join('_generacii', src)
    if os.path.exists(p):
        im = Image.open(p).convert('RGB')
        crop_ratio(im, 2.4, sverhu=0.5).resize((2400, 1000), Image.LANCZOS).save(
            f'images/obrazy/{name}.jpg', quality=84, optimize=True)
        n += 1

# для карточек с портретом доля подобрана глазами: автопоиск ловит руки и грудь
RUCHNOJ_SREZ = {'z-nechist': 0.18, 'z-oberegi': 0.06}
SREZ_SHAPOK = {
    'h-glavnaya': dict(dolya=0.66, verh=0.02),
    'h-irina': dict(dolya=0.70, verh=0.02),
    'h-taro': dict(dolya=0.78, verh=0.04),
    'h-shkola': dict(dolya=0.96, verh=0.0, zapas=0.04),
    'h-kontakty': dict(dolya=0.80, verh=0.06),
}

for name, src in WIDE.items():
    if name in SCENY_SHAPOK:
        continue
    if name in RUCHNOJ_SREZ:
        im = Image.open(os.path.join(OBR, src)).convert('RGB')
        W0, H0 = im.size
        th = int(W0 / (16 / 9))
        top = int(H0 * RUCHNOJ_SREZ[name])
        im.crop((0, top, W0, min(H0, top + th))).resize((2200, 1238), Image.LANCZOS).save(
            f'images/obrazy/{name}.jpg', quality=84, optimize=True)
        n += 1
        continue
    im = Image.open(os.path.join(OBR, src)).convert('RGB')
    # 2.4:1 это пропорция полосы шапки. Для портретов доля подобрана глазами,
    # автопоиск ловит руки и грудь и режет лицо.
    if name in SREZ_SHAPOK:
        polosa_portreta(os.path.join(OBR, src), f'images/obrazy/{name}.jpg',
                        **SREZ_SHAPOK[name])
        n += 1
        continue
    lico = centr_lica(im)
    W0, H0 = im.size
    th = int(W0 / 2.4)
    if lico is None:
        dolya = 0.2
    else:
        # хотим, чтобы центр лица оказался примерно на 42% высоты полосы
        top = int(lico * H0 - th * 0.42)
        top = max(0, min(H0 - th, top))
        dolya = top / max(1, H0 - th)
    crop_ratio(im, 2.4, sverhu=dolya).resize((2400, 1000), Image.LANCZOS).save(
        f'images/obrazy/{name}.jpg', quality=82, optimize=True)
    print(f'  {name}: лицо на {round((lico or 0)*100)}%, срез с {round(dolya*100)}%')
    n += 1
for name, src in PORTRET.items():
    bezopasnyj_portret(os.path.join(OBR, src), f'images/obrazy/{name}.jpg')
    n += 1
print('картинок подготовлено:', n)
