#!/usr/bin/env python3
import re
import sys
from itertools import count
from urllib.parse import unquote

txt = sys.stdin.read()

# find links
links = dict()
link_cnt = count(1)
while True:
    match = re.search('\[\[(.+?)\|(.+?)\]\]', txt)
    if not match:
        break
    link, label = match.groups()
    link = unquote(link)

    if link in links:
        link_num = links[link]
    else:
        link_num = next(link_cnt)
        links[link] = link_num

    txt = txt[:match.start()] + f'{label}[{link_num}]' + txt[match.end():]

links = sorted([(v, k) for k, v in links.items()])

# remove images
txt = re.sub('\{\{.*?\}\}', '', txt)

# remove empty strings
txt = txt.replace('\n\n\n', '\n\n')

# print result
sys.stdout.write(txt)
sys.stdout.write('\n\n')
for n, l in links:
    sys.stdout.write(f'[{n}] {l}\n')
