#!/usr/bin/env python3
"""Export site HTML with resolved URLs for the unchanged upstream link auditor."""
import argparse
from html import escape,unescape
from pathlib import Path
import re
from urllib.parse import urljoin
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--route',action='append',required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
for route in a.route:
    file=(ROOT/route.strip('/')/'index.html').resolve()
    if not file.is_relative_to(ROOT):raise SystemExit('Invalid route')
    text=file.read_text();base_match=re.search(r'<base\b[^>]*href=["\']([^"\']+)',text,re.I);base=urljoin('https://biologische-hondensnacks.nl'+route,base_match.group(1)) if base_match else 'https://biologische-hondensnacks.nl'+route
    text=re.sub(r'\bhref=(["\'])(.*?)\1',lambda m:'href='+m.group(1)+escape(urljoin(base,unescape(m.group(2))),quote=True)+m.group(1),text,flags=re.I)
    slug=re.sub(r'[^a-zA-Z0-9]+','-',route.strip('/') or 'home').strip('-');(a.output/(slug+'.html')).write_text(text)
