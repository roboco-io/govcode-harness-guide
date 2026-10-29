"""Validate generated internal paths, anchors and public asset boundaries."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'

class Page(HTMLParser):
    def __init__(self,path):
        super().__init__();self.path=path;self.ids=set();self.refs=[];self.title=False;self.lang=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')=='ko'
        if tag=='title':self.title=True
        if 'id' in a:
            assert a['id'] not in self.ids, f'duplicate id: {self.path.name}'
            self.ids.add(a['id'])
        if tag in ('a','link') and a.get('href'):self.refs.append(a['href'])
        if tag in ('script','img') and a.get('src'):self.refs.append(a['src'])
        if tag=='img':assert a.get('alt'), 'image alt missing'
        if tag=='script':assert not urlsplit(a.get('src','')).scheme,'external script prohibited'

def main():
    pages={}
    for path in SITE.glob('*.html'):
        p=Page(path);p.feed(path.read_text());assert p.lang and p.title;pages[path]=p
    checked=0
    for path,p in pages.items():
        for ref in p.refs:
            u=urlsplit(ref)
            if u.scheme or u.netloc:continue
            target=(path.parent/unquote(u.path)).resolve() if u.path else path
            assert SITE.resolve() in target.parents, f'path escapes site: {ref}'
            assert target.is_file(),f'missing asset: {ref}'
            if u.fragment and target in pages:assert unquote(u.fragment) in pages[target].ids,f'missing anchor: {ref}'
            checked+=1
    for path in SITE.rglob('*'):
        if not path.is_file():continue
        assert not path.is_symlink()
        assert not any(x in path.parts for x in ['.runtime','.git','private-keys','node_modules'])
        assert path.suffix not in ['.pem','.key','.env']
        assert b'-----BEGIN PRIVATE KEY-----' not in path.read_bytes()
    pdf=SITE/'downloads/govcode-harness-brochure.pdf'
    assert pdf.read_bytes().startswith(b'%PDF-')
    checksum=hashlib.sha256(pdf.read_bytes()).hexdigest()+'  govcode-harness-brochure.pdf\n'
    assert (SITE/'downloads/SHA256SUMS').read_text()==checksum,'stale PDF checksum'
    print(f'PASS: {len(pages)} Korean pages, {checked} local paths/anchors, PDF checksum and public asset boundaries')

if __name__=='__main__':main()
