#!/usr/bin/env python3
"""Site command adapters: observable checks only, never an editorial approval."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.h1=0; self.lang=None; self.meta={}; self.canonical=[]; self.main=False; self.text=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html': self.lang=a.get('lang')
        if tag=='h1': self.h1+=1
        if tag=='meta': self.meta[a.get('name','')]=a.get('content','')
        if tag=='link' and a.get('rel')=='canonical': self.canonical.append(a.get('href'))
        if tag=='main': self.main=True
    def handle_endtag(self,tag):
        if tag=='main': self.main=False
    def handle_data(self,text):
        if self.main:self.text.append(text)

def validate(family=None,publish=False):
    routing=json.loads((ROOT/'.agents/workflow-routing.json').read_text())
    errors=[]; pages=[]; drafts=[]
    for item in routing['routes']:
        if family and not any(s.startswith(family+'-') for s in item['skills']):continue
        directory=ROOT/item['prefix'].strip('/')
        if directory.is_dir(): pages.extend(directory.rglob('index.html'))
    for p in sorted(set(pages)):
        parsed=Page(); parsed.feed(p.read_text()); relative=p.relative_to(ROOT).as_posix(); route='/'+relative.removesuffix('index.html')
        if parsed.lang!='nl':errors.append(relative+': expected nl')
        if parsed.h1!=1:errors.append(relative+': expected one H1')
        if parsed.canonical!=['https://biologische-hondensnacks.nl'+route]:errors.append(relative+': wrong canonical')
        if not parsed.meta.get('description'):errors.append(relative+': missing description')
        is_draft='noindex' in parsed.meta.get('robots','')
        if is_draft:drafts.append(route)
        # No automatic change of publication state. Indexable pages need a real registry approval.
        if not is_draft:
            approved=False
            for record in (ROOT/'.content/publication').glob('*.json'):
                data=json.loads(record.read_text())
                if data.get('url')==route and data.get('human_approved') is True and data.get('indexation_authorized') is True:approved=True
            if not approved:errors.append(relative+': indexable without explicit publication registry')
        if publish:
            body=' '.join(parsed.text)
            if re.search(r'Inhoud nog te schrijven|Dit paginatype staat klaar|Structuur wordt bepaald na intentie',body,re.I):errors.append(relative+': unfinished content')
            if family in {'usage','trust','deal'}:
                registry={'usage':'usages','trust':'trust','deal':'deals'}[family]
                records=list((ROOT/'.content'/registry).glob('*.json'))
                if not any(route in json.dumps(json.loads(f.read_text())) for f in records):errors.append(relative+': missing workflow evidence registry')
    for e in errors:print('FAIL:',e)
    if errors:return 1
    if not pages:print('NOT_APPLICABLE: no existing routes for',family)
    else:print(f'PASS: {len(set(pages))} pages checked; {len(drafts)} retain noindex. Machine checks only.')
    return 0
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--family',choices=['guide','usage','brand','comparison','deal','trust']);parser.add_argument('--publish',action='store_true');args=parser.parse_args();raise SystemExit(validate(args.family,args.publish))
