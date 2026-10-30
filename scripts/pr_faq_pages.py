"""Render the deliberately small Markdown subset used by the PR/FAQ source."""
from html import escape
import re
from urllib.parse import urlsplit


def inline(text):
    tokens = re.compile(r'\[([^\]]+)\]\(([^)]+)\)|\*\*(.+?)\*\*|`([^`]+)`')
    output, last = [], 0
    for match in tokens.finditer(text):
        output.append(escape(text[last:match.start()]))
        label, href, bold, code = match.groups()
        if href:
            if urlsplit(href).scheme not in ('https', 'http', ''):
                raise ValueError('Unsupported link protocol')
            output.append(f'<a href="{escape(href, quote=True)}">{escape(label)}</a>')
        elif bold:
            output.append(f'<strong>{escape(bold)}</strong>')
        else:
            output.append(f'<code>{escape(code)}</code>')
        last = match.end()
    output.append(escape(text[last:]))
    return ''.join(output)


def render(text, prefix):
    blocks = re.split(r'\n\s*\n', text.strip())
    output = []
    for block in blocks:
        lines = block.splitlines()
        if all(line.startswith('>') for line in lines):
            quote = '\n'.join(line[1:].lstrip() for line in lines)
            output.append('<blockquote>' + render(quote, prefix) + '</blockquote>')
        elif lines[0].startswith('|'):
            rows = [[cell.strip() for cell in line.strip().strip('|').split('|')] for line in lines]
            if len(rows) < 2 or not all(re.fullmatch(r':?-+:?', cell) for cell in rows[1]):
                raise ValueError('Malformed PR/FAQ table')
            header = ''.join('<th scope="col">' + inline(cell) + '</th>' for cell in rows[0])
            body = ''.join('<tr>' + ''.join('<td>' + inline(cell) + '</td>' for cell in row) + '</tr>' for row in rows[2:])
            output.append('<div class="table-scroll"><table><thead><tr>' + header + '</tr></thead><tbody>' + body + '</tbody></table></div>')
        elif lines[0].startswith('### '):
            assert len(lines) == 1
            title = lines[0][4:]
            number = re.match(r'(\d+) ', title)
            anchor = f' id="{prefix}-{number.group(1)}"' if number else ''
            output.append(f'<h3{anchor}>' + inline(title) + '</h3>')
        elif lines[0].startswith('## '):
            assert len(lines) == 1
            output.append('<h2>' + inline(lines[0][3:]) + '</h2>')
        elif lines[0].startswith(('# ', '```', '- ', '* ')):
            raise ValueError('Unsupported PR/FAQ block: ' + lines[0])
        else:
            output.append('<p>' + inline(' '.join(lines)) + '</p>')
    return '\n'.join(output)


def build_pr_faq(root, page):
    source = (root / 'docs/PR_FAQ.md').read_text()
    press = source.split('## PR 목표 출시 시점의 보도자료\n', 1)[1].split('## 고객 FAQ\n', 1)[0]
    customer, rest = source.split('## 고객 FAQ\n', 1)[1].split('## 내부 FAQ\n', 1)
    internal, sources = rest.split('## 근거와 연결 문서\n', 1)
    common = '<p class="small">작성일: 2026-10-30 · 제품 방향 검토용 초안 · <a href="https://github.com/roboco-io/govcode-harness-guide/blob/main/docs/PR_FAQ.md">원문과 변경 이력</a></p>'
    page('pr.html', 'PR 보도자료 초안', '다양한 공공 프로젝트에서 비개발자가 안전하게 바이브 코딩하는 목표 경험을 담은 미래 보도자료 초안입니다.',
         '<main id="main" class="wrap"><header class="page-head"><span class="tag">Working Backwards · 미래 출시 가정</span><h1>PR 보도자료 초안</h1>' + common +
         '<div class="note"><p><strong>실제 출시 공지가 아닙니다.</strong> 목표 출시 시점의 고객 경험을 그린 문서입니다. 인용문은 가상 발언이며 정식 출시일은 미정입니다. 현재 제공 기능은 <a href="faq.html#customer-1">고객 FAQ 1번</a>과 <a href="updates.html">공개 버전 안내</a>에서 확인하세요.</p></div></header>' +
         '<article class="article prfaq-document">' + render(press, 'press') + '<div class="actions"><a class="button" href="faq.html">고객·내부 FAQ 읽기</a><a href="community.html">의견 남기기</a></div></article></main>')
    page('faq.html', '고객 FAQ와 내부 FAQ', 'GovCode Harness의 현재 기능, 바이브 코딩 목표, 비용, 파일럿 참여와 제품 검증 계획을 설명하는 24개 질문입니다.',
         '<main id="main" class="wrap"><header class="page-head"><span class="tag">Working Backwards · 공개 검토 문서</span><h1>고객 FAQ와 내부 FAQ</h1>' + common +
         '<p>고객 FAQ는 사용 범위와 참여 방법을, 내부 FAQ는 제품 가설·검증 계획과 아직 결정하지 않은 사항을 다룹니다. 내부 FAQ도 의견을 받기 위해 공개한 기획 초안이며 확정된 약속이 아닙니다.</p></header>' +
         '<div class="guide-grid"><nav class="toc" aria-label="FAQ 목차"><strong>질문 찾아보기</strong><a href="#customer">고객 FAQ 12개</a><a href="#customer-1">현재 공개 기능</a><a href="#customer-2">대상 업무와 사용자</a><a href="#customer-10">비용·이용 조건</a><a href="#customer-11">비개발자의 직접 제작</a><a href="#internal">내부 FAQ 12개</a><a href="#internal-7">고객 가치 검증</a><a href="#internal-12">남은 결정</a><a href="#sources">근거와 연결 문서</a><a href="pr.html">PR 보도자료 초안</a></nav>' +
         '<article class="article prfaq-document"><section id="customer"><h2>고객 FAQ</h2>' + render(customer, 'customer') + '</section><section id="internal"><h2>내부 FAQ</h2>' + render(internal, 'internal') + '</section><section id="sources"><h2>근거와 연결 문서</h2>' + render(sources, 'sources') + '</section></article></div></main>')
