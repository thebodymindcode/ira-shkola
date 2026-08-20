# -*- coding: utf-8 -*-
"""Рисованная карточка аркана: символ и римская цифра в золотой рамке."""

Z = '#C9A227'
ZS = '#E3C15B'
FON = '#171320'

RIMSKIE = ['0','I','II','III','IV','V','VI','VII','VIII','IX','X',
           'XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI']

# знак для каждого аркана: простая сильная линия
ZNAKI = {
 'durak': '<path d="M60 128 L84 74 L104 108 L124 66"/><circle cx="130" cy="52" r="7"/>',
 'mag': '<path d="M92 40v104"/><path d="M60 92h64"/><circle cx="92" cy="92" r="30"/>',
 'zhritsa': '<path d="M64 44v96M120 44v96"/><path d="M64 60h56"/><circle cx="92" cy="98" r="16"/>',
 'imperatrica': '<circle cx="92" cy="82" r="26"/><path d="M92 108v34M76 124h32"/>',
 'imperator': '<path d="M60 140V74l32-30 32 30v66Z"/><path d="M80 140v-30h24v30"/>',
 'ierofant': '<path d="M92 40v104"/><path d="M68 68h48M68 92h48"/>',
 'vlyublyonnye': '<circle cx="72" cy="96" r="24"/><circle cx="112" cy="96" r="24"/>',
 'kolesnica': '<circle cx="92" cy="112" r="26"/><path d="M92 86V50M62 50h60"/>',
 'sila': '<path d="M60 108c0-26 14-42 32-42s32 16 32 42"/><path d="M74 116a18 18 0 0 0 36 0"/>',
 'otshelnik': '<path d="M92 44v40"/><circle cx="92" cy="104" r="24"/><path d="M92 128v20"/>',
 'koleso': '<circle cx="92" cy="92" r="42"/><circle cx="92" cy="92" r="14"/><path d="M92 50v84M50 92h84"/>',
 'spravedlivost': '<path d="M92 44v100"/><path d="M56 70h72"/><path d="M56 70l-12 30h24ZM128 70l-12 30h24Z"/>',
 'povesheny': '<path d="M52 48h80"/><path d="M92 48v40"/><circle cx="92" cy="104" r="16"/><path d="M92 120l-18 24M92 120l18 24"/>',
 'smert': '<path d="M56 132 132 56"/><path d="M132 56v34M132 56H98"/>',
 'umerennost': '<path d="M64 60l24 32-24 32Z"/><path d="M120 60l-24 32 24 32Z"/>',
 'dyavol': '<path d="M60 60c10 18 10 34 0 52M124 60c-10 18-10 34 0 52"/><circle cx="92" cy="98" r="20"/>',
 'bashnya': '<path d="M70 144V70h44v74Z"/><path d="M70 70l22-24 22 24"/><path d="M128 44l-24 34h20l-16 26"/>',
 'zvezda': '<path d="M92 46l10 30h32l-26 20 10 32-26-20-26 20 10-32-26-20h32Z"/>',
 'luna': '<path d="M118 44a44 44 0 1 0 0 96 34 34 0 0 1 0-96Z"/>',
 'solnce': '<circle cx="92" cy="92" r="26"/><path d="M92 40v14M92 130v14M40 92h14M130 92h14M56 56l10 10M118 118l10 10M128 56l-10 10M66 118l-10 10"/>',
 'sud': '<path d="M56 130h72"/><path d="M92 130V70"/><path d="M62 70l30-26 30 26"/>',
 'mir': '<ellipse cx="92" cy="92" rx="34" ry="48"/><path d="M92 44v96"/>',
}


def karta(slug, nomer, name):
    znak = ZNAKI.get(slug, ZNAKI['mir'])
    rim = RIMSKIE[nomer]
    return f'''<svg class="ark" viewBox="0 0 184 268" role="img" aria-label="{name}">
<rect x="2" y="2" width="180" height="264" rx="14" fill="{FON}" stroke="{Z}" stroke-width="1.4"/>
<rect x="10" y="10" width="164" height="248" rx="9" fill="none" stroke="{Z}"
 stroke-width=".8" opacity=".4"/>
<g fill="none" stroke="{ZS}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"
 opacity=".92">{znak}</g>
<text x="92" y="196" text-anchor="middle" fill="{Z}" style="font-family:'Forum',serif;
 font-size:26px;letter-spacing:3px">{rim}</text>
<text x="92" y="230" text-anchor="middle" fill="#EFE8DD" style="font-family:'Prata',serif;
 font-size:17px">{name}</text>
</svg>'''
