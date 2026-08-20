# -*- coding: utf-8 -*-
"""Готовит картинки сайта: кадры статей 16:9 и образы Иры под страницы."""
from PIL import Image
import os, shutil

OBR = os.path.expanduser('~/Instagram-Irina-Volkova/ФОТО-ОБРАЗЫ-ТАРО')
os.makedirs('images/obrazy', exist_ok=True)

def crop_ratio(im, ratio):
    w, h = im.size
    tw, th = (w, int(w / ratio)) if w / h < ratio else (int(h * ratio), h)
    left, top = (w - tw) // 2, (h - th) // 3   # верхняя треть: лица и свет обычно выше центра
    return im.crop((left, top, left + tw, top + th))

# 1. кадры статей до 1200x675
n = 0
for f in sorted(os.listdir('images/zhurnal')):
    if not f.endswith('.jpg'):
        continue
    p = 'images/zhurnal/' + f
    im = Image.open(p).convert('RGB')
    im = crop_ratio(im, 16 / 9).resize((1200, 675), Image.LANCZOS)
    im.save(p, quality=82, optimize=True)
    n += 1

# 2. два кадра из образов для статей без видео
for slug, src in (('01-leshy', '09-voron.jpg'), ('03-vodyanoy', '12-luna-nad-vodoj.jpg')):
    im = Image.open(os.path.join(OBR, src)).convert('RGB')
    crop_ratio(im, 16 / 9).resize((1200, 675), Image.LANCZOS).save(
        f'images/zhurnal/{slug}.jpg', quality=82, optimize=True)
    n += 1

# 3. образы под страницы: широкий (16:9) и портретный (3:4)
WIDE = {
    # карточки курсов: разные планы, портрет крупно только один
    'k-gekata': '16-luna-utyos.jpg', 'k-runy': '17-luna-tyanetsya.jpg',
    'k-besy': '08-chyornoe-zerkalo.jpg', 'k-nastav': '11-renessans-portret.jpg',
    'k-taro': '27-krug-svechej-taro.jpg', 'k-oberegi': '18-luna-okno.jpg',
    # шапки страниц
    'h-glavnaya': '06-oblozhka.jpg', 'h-kursy': '14-krug-svechej.jpg',
    'h-shkola': '12-luna-nad-vodoj.jpg', 'h-taro': '26-svecha-taro.jpg',
    'h-zhurnal': '24-taro-stena.jpg', 'h-oberegi': '05-svecha-fazy-luny.jpg',
    'h-nechist': '15-lico-iz-dyma.jpg', 'h-vopros': '19-svechi-karta.jpg',
    'h-kontakty': '20-svechi-plamya.jpg', 'h-irina': '21-svechi-oglyanulas.jpg',
    # карточки разделов в журнале
    'z-oberegi': '22-svechi-oreol.jpg', 'z-nechist': '09-voron.jpg',
}
PORTRET = {
    'p-glavnaya': '10-hrustalnyj-shar.jpg', 'p-irina1': '02-karta-u-lica.jpg',
    'p-irina2': '13-ogonyok-v-ladoni.jpg', 'p-shkola': '04-tasuet-kolodu.jpg',
    'p-taro': '25-taro-levitaciya.jpg',
}
for name, src in WIDE.items():
    im = Image.open(os.path.join(OBR, src)).convert('RGB')
    crop_ratio(im, 16 / 9).resize((1600, 900), Image.LANCZOS).save(
        f'images/obrazy/{name}.jpg', quality=82, optimize=True)
    n += 1
for name, src in PORTRET.items():
    im = Image.open(os.path.join(OBR, src)).convert('RGB')
    crop_ratio(im, 3 / 4).resize((900, 1200), Image.LANCZOS).save(
        f'images/obrazy/{name}.jpg', quality=82, optimize=True)
    n += 1
print('картинок подготовлено:', n)
