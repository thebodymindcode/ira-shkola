# -*- coding: utf-8 -*-
"""Готовит картинки сайта: кадры статей 16:9 и образы Иры под страницы."""
from PIL import Image
import os, shutil

OBR = os.path.expanduser('~/Instagram-Irina-Volkova/ФОТО-ОБРАЗЫ-ТАРО')
os.makedirs('images/obrazy', exist_ok=True)

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
    'k-gekata': 'k-gekata.png', 'k-runy': 'k-runy.png', 'k-besy': 'k-besy.png',
    'k-nastav': 'k-nastav.png', 'k-taro': 'k-taro.png', 'k-oberegi': 'k-oberegi3.png',
}
# шапки страниц: сцены без людей, поэтому лицо нигде не режется
SCENY_SHAPOK = {
    'h-kursy': 'h2-kursy.png', 'h-oberegi': 'h2-oberegi.png',
    'h-nechist': 'h2-nechist.png', 'h-vopros': 'h2-vopros2.png',
}
STATI_SCENY = {'01-leshy': 'leshy-v3.png', '03-vodyanoy': 'vodyanoy-nb.png'}

WIDE = {
    # шапки страниц
    'h-glavnaya': '06-oblozhka.jpg', 'h-kursy': '14-krug-svechej.jpg',
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
SREZ_SHAPOK = {'h-glavnaya': 0.06, 'h-irina': 0.06, 'h-taro': 0.32,
               'h-zhurnal': 0.32, 'h-shkola': 0.02, 'h-kontakty': 0.13}

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
        W0, H0 = im.size
        th = int(W0 / 2.4)
        top = int(H0 * SREZ_SHAPOK[name])
        im.crop((0, top, W0, min(H0, top + th))).resize((2400, 1000), Image.LANCZOS).save(
            f'images/obrazy/{name}.jpg', quality=84, optimize=True)
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
    im = Image.open(os.path.join(OBR, src)).convert('RGB')
    crop_ratio(im, 3 / 4).resize((1200, 1600), Image.LANCZOS).save(
        f'images/obrazy/{name}.jpg', quality=82, optimize=True)
    n += 1
print('картинок подготовлено:', n)
