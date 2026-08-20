# -*- coding: utf-8 -*-
"""Перекладывает ПОДПИСЬ.txt рилсов Иры в структуру статьи сайта."""
import json, os, re, glob

BASE_DIRS = [
    (os.path.expanduser('~/Reels Instagram/2026-08-06-нечисть-ира'), 'nechist'),
    (os.path.expanduser('~/Reels Instagram/2026-08-06-мистика-ира'), 'oberegi'),
]

EMOJI = re.compile('[\U0001F000-\U0001FAFF☀-➿️⬀-⯿]')

def parse(path):
    raw = open(path, encoding='utf-8').read().strip()
    blocks = [b.strip() for b in raw.split('\n\n') if b.strip()]
    head = EMOJI.sub('', blocks[0]).strip()
    # имя существа = до первой точки
    m = re.match(r'^([^.!?]+)[.!?]\s*(.*)$', head, re.S)
    name = m.group(1).strip() if m else head
    deck = (m.group(2).strip() if m else '').rstrip(':').strip()
    body = blocks[1:]
    # последний блок = призыв про телеграм, убираем
    if body and ('Telegram' in body[-1] or 'телеграм' in body[-1].lower() or 'шапк' in body[-1]):
        body = body[:-1]
    lead = ''
    sections = []
    cur = None
    lines = []
    for b in body:
        lines.extend([l.strip() for l in b.split('\n') if l.strip()])
    for line in lines:
        line = EMOJI.sub('', line).strip()
        if not line:
            continue
        m2 = re.match(r'^(\d+)\.\s*(.+?)\s*$', line)
        if m2 and len(line) < 120:
            cur = {'h': m2.group(2).rstrip('.').strip(), 'p': []}
            sections.append(cur)
        elif cur is None:
            lead = (lead + ' ' + line).strip()
        else:
            cur['p'].append(line)
    return {'name': name, 'deck': deck, 'lead': lead, 'sections': sections}

out = []
for d, kind in BASE_DIRS:
    for folder in sorted(glob.glob(os.path.join(d, '*/'))):
        p = os.path.join(folder, 'ПОДПИСЬ.txt')
        if not os.path.exists(p):
            continue
        slug = os.path.basename(folder.rstrip('/'))
        art = parse(p)
        art['slug'] = slug
        art['kind'] = kind
        out.append(art)

json.dump(out, open('content/articles.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('статей:', len(out))
for a in out[:3] + out[-2:]:
    print('---', a['slug'], '|', a['name'], '|', len(a['sections']), 'разделов | лид', len(a['lead']), 'зн')
    print('   дек:', a['deck'][:90])
    print('   h:', ' / '.join(s['h'] for s in a['sections']))
bad = [a['slug'] for a in out if len(a['sections']) < 3 or not a['lead']]
print('подозрительные:', bad)
