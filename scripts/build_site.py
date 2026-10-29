"""Build a self-contained Korean adoption site from versioned content."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
URL = 'https://roboco.io/govcode-harness-guide/'
REPO = 'https://github.com/roboco-io/govcode-harness'
CODE_REF = 'v0.9.0-apache2'
TAG = REPO + '/tree/' + CODE_REF
FILES = REPO + '/blob/' + CODE_REF

def code(text):
    return '<div class="codebox"><button type="button" data-copy aria-label="명령 복사">복사</button><pre><code>' + escape(text.strip()) + '</code></pre></div>'

def table(headers, rows):
    return '<div class="table-scroll"><table><thead><tr>' + ''.join('<th scope="col">'+x+'</th>' for x in headers) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows) + '</tbody></table></div>'

def flow():
    return '''<ol class="flow" aria-label="민원 API 변경 검사 흐름">
<li><span class="number">1</span><span>민원 본문을 로그에 기록하는 코드</span><span class="state deny">deny</span></li>
<li><span class="number">2</span><span>원문 로깅 제거 · 감사 이벤트 유지</span><span class="state">수정</span></li>
<li><span class="number">3</span><span>새 commit의 필수 검사 재실행</span><span class="state allow">allow</span></li>
<li><span class="number">4</span><span>정책·판정·수정 이력을 증적으로 연결</span><span class="state">증적</span></li></ol>'''

def platform_flow():
    return '<ol class="flow platform-flow" aria-label="제품 목표: 공공 프로젝트 규정 충족 흐름"><li><span class="number">1</span><span>프로젝트 조건과 적용 요구 정리</span><span class="state">적용성</span></li><li><span class="number">2</span><span>규정별 수행 작업·산출물 안내</span><span class="state">작업</span></li><li><span class="number">3</span><span>자동 검사·수정 지원과 담당자 검토</span><span class="state">충족</span></li><li><span class="number">4</span><span>승인·예외·증적과 변경 영향 연결</span><span class="state">추적</span></li></ol>'

def page(name, title, description, body):
    links = [('index.html','솔루션 소개'),('onboarding.html','온보딩 가이드'),('brochure.html','브로슈어')]
    nav = ''.join('<a href="'+path+'"'+(' aria-current="page"' if path==name else '')+'>'+label+'</a>' for path,label in links)
    text = '''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>'''+escape(title)+''' | GovCode Harness</title><meta name="description" content="'''+escape(description)+'''">
<meta name="theme-color" content="#142943"><link rel="license" href="https://creativecommons.org/licenses/by/4.0/"><link rel="canonical" href="'''+URL+name+'''">
<meta property="og:title" content="'''+escape(title)+''' | GovCode Harness"><meta property="og:description" content="'''+escape(description)+'''">
<meta property="og:type" content="website"><meta property="og:locale" content="ko_KR"><meta property="og:url" content="'''+URL+name+'''">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/style.css"><script defer src="assets/site.js"></script></head>
<body><a class="skip" href="#main">본문 바로가기</a><header class="top"><div class="wrap"><a class="brand" href="index.html"><span class="mark" aria-hidden="true">G</span>GovCode Harness</a><nav class="nav" aria-label="주 메뉴">'''+nav+'''</nav></div></header>
'''+body+'''<footer class="footer"><div class="wrap"><p>GovCode Harness · 공공 프로젝트의 규정 충족을 안내하는 하네스 · 첫 참조 구현 v0.9.0<br>합성 자료 검증 기준: 2026-10-29. 검사 통과는 법적 준수 인증이나 기관 운영 승인을 뜻하지 않습니다.<br>© 2026 GovCode Harness contributors · 가이드·브로슈어 <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> · <a href="license.html">출처 표시 안내</a> · 프로젝트 코드 <a href="https://github.com/roboco-io/govcode-harness/blob/main/LICENSE">Apache-2.0</a></p><a href="'''+REPO+'''">프로젝트 GitHub</a></div></footer><div class="sr-only" id="status" role="status" aria-live="polite"></div></body></html>'''
    (SITE/name).write_text(text)

def build():
    page('index.html','공공 프로젝트 규정을 실행 가능한 업무로 연결합니다','공공 프로젝트에 적용되는 법령·규칙·가이드라인을 수행 작업과 자동 검사·수정 지원·검토·증적으로 연결하는 규정 준수 하네스.',
'''<main id="main"><div class="wrap"><section class="hero"><div><span class="tag">공공 프로젝트 수행을 위한 규정 준수 하네스</span><h1>공공 프로젝트 규정을<br>실행 가능한<br>업무로 연결합니다.</h1><p class="lead">적용되는 법령·규칙·가이드라인을 필요한 작업으로 옮깁니다. 자동화할 수 있는 검사와 수정 지원, 담당자의 검토·승인·증적을 연결해 요구 충족을 안내하는 것이 제품의 목표입니다.</p><div class="actions"><a class="button" href="onboarding.html">로컬에서 시작하기</a><a class="button secondary" href="brochure.html">도입 브로슈어 보기</a></div><p class="caption">현재 v0.9.0: 민원 API 로깅을 첫 사례로 검증 · 분야별 확장 설계 중</p></div><div class="dossier"><p class="dossier-title">제품 목표 / 요구에서 충족 근거까지</p>'''+platform_flow()+'''<p class="small">자동화 가능한 작업은 검사·수정으로, 책임 있는 판단은 담당자 검토로 연결합니다. 현재 첫 사례에서 공통 정책·증적 기반을 검증했습니다.</p></div></section>
<div class="proof-strip" aria-label="검증과 지원 범위"><p><strong>첫 사례 320개 회귀 시험 통과</strong>실패 0 · 건너뜀 0, 로컬 참조 기준</p><p><strong>위험본 deny → 수정본 allow</strong>새 commit과 증적을 함께 확인</p><p><strong>기관 내부 실행 지향</strong>공개 사이트는 안내 자료만 제공</p></div></div>
<section class="section"><div class="wrap"><div class="section-head"><h2>어떤 요구를 충족해야 하는지,<br>다음에 무엇을 해야 하는지.</h2><p>발주기관과 수행사는 프로젝트 조건에 맞는 기준을 적용하고, 설계·개발·시험·검수·운영의 작업과 근거를 연결해야 합니다. 이 전체 과정을 안내하는 제품으로 확장합니다.</p></div><div class="columns"><article class="feature"><h3>적용 요구를 작업으로</h3><p>출처·버전·적용 조건을 확인한 요구를 담당자·수행 작업·산출물·검사에 연결하는 것이 목표입니다. 범용 프로젝트 프로필과 규정 팩은 후속 설계 범위입니다.</p></article><article class="feature"><h3>충족 작업의 자동화</h3><p>자동 검사·수정 지원·재검사로 요구 충족을 돕습니다. 현재는 첫 로깅 사례와 공통 정책·승인·게이트 기반을 구현했고, 다른 분야의 검사와 산출물 지원은 확장할 계획입니다.</p></article><article class="feature"><h3>완료까지 근거 추적</h3><p>충족·미충족·검토 대기·미검증을 근거와 함께 안내하는 것이 목표입니다. 현재는 첫 사례의 서명 증적·이력·보관·복구 기반을 검증했습니다.</p></article></div></div></section>
<section class="section wash"><div class="wrap"><div class="section-head"><h2>공공 프로젝트 수행 전반을<br>규정 팩으로 확장합니다.</h2><p>다음은 확장 후보입니다. 모든 프로젝트에 적용되는 의무 목록이나 현재 구현한 검사 목록이 아닙니다.</p></div><div class="columns"><div><h3>개인정보·보안 / 접근성</h3><p>보호 요구와 이용 환경별 점검을 작업·수정·검토 근거에 연결하는 방향입니다.</p></div><div><h3>개발 품질 / 표준·상호운용성</h3><p>필수 시험과 프로젝트별 개발·인터페이스 기준을 확인하도록 확장합니다.</p></div><div><h3>사업 산출물 / 운영·보존</h3><p>단계별 문서·검수·운영·보존 요구와 제출 근거를 안내하도록 확장합니다.</p></div></div><div class="note"><p><strong>첫 사례가 보여 주는 공통 흐름</strong> 민원 API 개인정보 로깅 위험을 탐지해 deny → 수정 → 새 commit 재검사 → allow → 증적으로 연결했습니다. 이 결과가 다른 규정 분야의 자동 충족을 증명하지는 않습니다.</p></div></div></section><section class="section wash"><div class="wrap split"><div><h2>실행·정책·증적을<br>같은 화면에서 확인하세요.</h2><p>한국어 관리 화면에서 역할별로 정책과 실행을 살펴보고, 수정·재검사·예외 이력을 따라갈 수 있습니다.</p><ul class="capability"><li>기관·프로젝트·역할에 따른 서버 측 접근 통제</li><li>합성 작성자·승인자·운영자·감사 열람자 역할</li><li>보관 잠금과 백업·복구를 포함한 증적 수명주기</li></ul><p class="small">화면은 합성 감사 열람자로 검증한 예시입니다. 실제 기관 신원 연동은 별도 적용이 필요합니다.</p></div><figure style="margin:0"><img class="screenshot" src="assets/images/control-desk.png" alt="합성 감사 열람자의 GovCode 관리 화면. 실행 결과와 증적 조회 메뉴를 보여 줍니다." loading="lazy" width="1440" height="1000"><figcaption class="caption">실제 로컬 참조 관리 UI · 합성 자료</figcaption></figure></div></section>
<section class="section"><div class="wrap"><div class="section-head"><h2>확인한 기능과<br>기관에서 결정할 조건을 구분합니다.</h2><p>첫 도입은 합성 자료와 한정된 저장소에서 시작하세요. 검증 범위를 정한 뒤 실제 기관 적용 여부를 판단할 수 있습니다.</p></div><div class="boundaries"><div><h3>지금 실행할 수 있는 것</h3><p>탐지·게이트·독립 승인·서명 증적·보관 및 복구·관리 API와 화면·승인된 수정의 격리 검증을 로컬에서 확인할 수 있습니다.</p></div><div><h3>도입 전에 확정할 것</h3><p>기관별 규정 적용, 운영 신원·키, 보존 분류, 실제 CI 연결, 모델 사용·반출 범위와 파일럿 책임자를 결정해야 합니다.</p></div></div><div class="note"><p><strong>지원 경계</strong> 현재 분석은 제한된 Python AST 범위입니다. 전체 수정 격리 검증은 macOS에서 확인했습니다. 참조 데모의 모델은 fixture이며 실제 LLM 추론·품질을 검증한 결과가 아닙니다.</p></div><div class="actions"><a class="button" href="onboarding.html#prepare">도입 준비 항목 확인</a><a class="button secondary" href="downloads/govcode-harness-brochure.pdf" download>브로슈어 PDF 받기</a><a href="'''+TAG+'''">v0.9.0 코드 보기</a></div></div></section></main>''')

    get_source=code('''git clone --branch v0.9.0-apache2 --depth 1 https://github.com/roboco-io/govcode-harness.git
cd govcode-harness''')
    basic=code('''python3 -m govcode_harness demo --output .runtime/first-onboarding''')
    setup=code(r'''python3 scripts/setup_reference.py \
  --python /absolute/path/to/python3.12 \
  --uv /absolute/path/to/uv''')
    reference=code(r'''.runtime/reference-venv/bin/python -m govcode_harness reference-demo \
  --output .runtime/onboarding-reference''')
    control=code(r'''.runtime/reference-venv/bin/python -m govcode_harness control \
  --config .runtime/onboarding-reference/control-config.json \
  --port 8766''')
    inspect=code('''python3 -m json.tool .runtime/onboarding-reference/reference-result.json''')
    tests=code('''.runtime/reference-venv/bin/python -m unittest discover -s tests -p 'test_*.py' -q
.runtime/reference-venv/bin/python -m govcode_harness gate --help''')
    checklist=''.join('<li><label><input type="checkbox"><span>'+item+'</span></label></li>' for item in [
      '대상 저장소·Python 지원 구문·제외 범위를 정했습니다.',
      '개인정보·보안 담당자와 규정 적용성 및 미확정 항목을 확인했습니다.',
      '정책 작성자·승인자·운영자·감사 열람자와 운영 신원을 정했습니다.',
      '서명키·신뢰 루트·철회 전파·최소 순번 관리 책임을 정했습니다.',
      '증적 보존 분류·접근·보관 잠금·파기·복구 책임을 정했습니다.',
      'CI의 신뢰한 expected commit과 필수 검사·보호 브랜치 설정을 정했습니다.',
      '모델 사용 여부와 허용 입력·반출 범위를 정했습니다.',
      '파일럿 기간·표본·정답·성공 기준·중단 조건·책임자를 정했습니다.'])
    page('onboarding.html','온보딩 가이드','소스 받기부터 기본 데모, 서명 참조 실행, 관리 화면과 실제 기관 파일럿 준비까지 단계별로 안내합니다.',
'''<main id="main" class="wrap"><header class="page-head"><span class="tag">v0.9.0 도입 안내</span><h1>작게 실행하고,<br>기관 적용 조건을 확인하세요.</h1><p>먼저 프로젝트의 적용 요구와 수행 작업을 정리하세요. 아래 실행 명령은 첫 구현 사례인 합성 민원 API 로깅을 확인하는 경로입니다. 다른 규정 분야는 별도 설계·검증이 필요합니다.</p></header><div class="guide-grid"><nav class="toc" aria-label="가이드 목차"><strong>처음 시작하는 순서</strong><a href="#project-scope">프로젝트 요구부터 시작</a><a href="#prepare">1. 준비와 지원 범위</a><a href="#source">2. 소스 받기</a><a href="#basic">3. 기본 흐름 확인</a><a href="#reference">4. 전체 참조 실행</a><a href="#results">5. 결과 읽기</a><a href="#control">6. 관리 화면 열기</a><a href="#ci">7. CI 적용 준비</a><a href="#pilot">8. 기관 파일럿 준비</a><a href="#troubleshooting">문제 해결</a><a href="#evidence">검증 근거와 자료</a></nav><article class="article">
<section id="project-scope"><h2>프로젝트 요구부터 시작하세요</h2><p>GovCode Harness의 목적은 공공 프로젝트에 적용되는 법령·규칙·가이드라인을 충족하도록 안내하는 것입니다. 개인정보 로깅은 첫 구현 사례입니다.</p><ol><li>프로젝트 유형·단계·기관 조건과 적용 후보 기준을 정리합니다.</li><li>출처·버전·적용 조건을 확인하고 요구별 수행 작업·산출물·담당자를 연결합니다.</li><li>자동 검사·수정 지원으로 처리할 항목과 담당자의 판단·승인이 필요한 항목을 구분합니다.</li><li>전체 요구 중 충족·미충족·미검증·검토 대기와 다음 작업을 추적합니다.</li></ol><div class="note"><p><strong>목표와 현재 기능</strong> 범용 프로젝트 프로필·분야별 규정 팩·산출물 검사·전체 충족 현황 안내는 후속 설계입니다. v0.9.0은 로깅 사례와 공통 정책·증적 기반을 제공합니다.</p></div><p><a href="https://github.com/roboco-io/govcode-harness/blob/main/docs/PRODUCT_DIRECTION.md">제품 전체 범위와 다음 설계</a></p></section><section id="prepare"><h2>1. 준비와 지원 범위</h2><p>개발자 또는 플랫폼 담당자가 로컬 환경에서 시작할 수 있습니다. 실제 민원 원문·운영 비밀값을 준비할 필요가 없습니다.</p>'''+table(['경로','필요 환경','확인하는 것'],[
['기본 데모','Python 3.10 이상, Git','표준 라이브러리 경로의 탐지·차단·수정·재검사. 서명 없음.'],
['전체 참조 데모','macOS, Python 3.12 이상, Git, uv, sandbox-exec 사용 가능 환경','서명 정책·격리 수정·증적·보관·복구·관리 API. 로컬 HTTP와 프로세스 실행 허용 필요.'],
['패키지 설치','최초 의존성 다운로드용 네트워크','버전·해시 잠금 의존성을 전용 .runtime 환경에 설치. 전역 Python은 변경하지 않음.']])+'''<p>전체 참조 검증 환경은 macOS와 Python 3.12입니다. 다른 OS에서 기본 검사를 시도할 수 있지만, 전체 격리 검증의 지원을 보장하지 않습니다.</p><p class="small">환경 도구: <a href="https://www.python.org/downloads/">Python 공식 다운로드</a> · <a href="https://docs.astral.sh/uv/getting-started/installation/">uv 공식 설치 안내</a>. 기관에서 승인한 설치 경로를 사용하세요.</p></section>
<section id="source"><h2>2. 고정 버전의 소스 받기</h2><p>재현 가능한 시작점을 위해 가이드의 기준 코드는 <code>v0.9.0</code>이며, 라이선스가 포함된 <code>v0.9.0-apache2</code> 태그를 받습니다. 이미 같은 이름의 폴더가 있다면 새 작업 경로를 사용하세요.</p>'''+get_source+'''<p><a href="'''+REPO+'''/archive/refs/tags/v0.9.0-apache2.zip">라이선스 포함 소스 ZIP 다운로드</a>도 가능합니다. 압축을 푼 경우 해당 폴더로 이동하세요. 검사 대상 저장소는 Git commit이 필요하지만, Harness 자체는 ZIP에서 실행할 수도 있습니다.</p><div class="note"><p>본 프로젝트와 이 가이드는 독립 저장소입니다. 가이드 수정에 서브모듈 갱신이 필요하지 않습니다. <a href="https://github.com/roboco-io/govcode-harness-guide">가이드 소스</a>의 버전 대응표에서 기준 코드를 확인할 수 있습니다.</p></div></section>
<section id="basic"><h2>3. 기본 흐름 먼저 확인하기</h2><p>프로젝트 루트에서 실행합니다. 명령은 새 합성 Git 저장소와 예시 자료를 출력 폴더 안에 만듭니다. 기존 업무 저장소는 수정하지 않습니다.</p>'''+basic+'''<p>정상 완료 시 명령의 종료 코드는 0이며 결과에는 <code>before: deny</code>, <code>after: allow</code>, <code>signature_status: not_signed</code>가 표시됩니다.</p><p>응답 보존, 민원 본문의 일반 로그 제거, 필요한 감사 호출 보존을 함께 확인합니다. 이 경로의 증적은 서명된 운영 증적이 아닙니다.</p></section>
<section id="reference"><h2>4. 서명과 관리까지 전체 참조 실행하기</h2><h3>전용 환경 설치</h3><p>아래 두 경로는 설치된 Python 3.12 이상과 uv의 실제 절대 경로로 바꾸세요. <code>command -v python3.12</code>와 <code>command -v uv</code>로 경로를 확인할 수 있습니다.</p>'''+setup+'''<p>버전·해시 잠금 파일에 따라 별도 환경을 만들고 정책·UI 자원을 포함한 Harness 패키지를 설치합니다. 기존 환경은 덮어쓰지 않습니다.</p><h3>새 출력 폴더에 실행</h3>'''+reference+'''<p>합성 작성자와 독립 승인자의 키 생성 → 예시 정책 서명 → 위험 commit 차단 → fixture 수정 제안과 승인 → 실제 OS 격리 검사 → 별도 알려진 수정 commit의 통과 → 증적 보관·복구 → 관리 API 확인 순서로 실행합니다.</p><div class="note"><p><strong>중요한 구분</strong> 격리된 제안 수정의 검사와 별도 알려진 수정 commit의 게이트 통과를 함께 확인하는 참조 흐름입니다. 실제 LLM이 자동으로 코드를 고쳐 운영 배포했다는 뜻이 아닙니다.</p></div></section>
<section id="results"><h2>5. 결과를 읽고 성공 여부 확인하기</h2>'''+inspect+table(['항목','기대 결과·의미'],[
['before.outcome / after.outcome','deny / allow. 위험본과 수정본은 서로 다른 commit입니다.'],
['model_checks','verdict=verified, sandbox_verified=true, checks의 모든 값 true. backend=fixture, real_model_executed=false.'],
['store_checks / control_checks','각각 4개 / 5개의 확인 항목이 모두 true. 보관·복구와 실제 loopback API의 합성 역할 경계를 확인합니다.'],
['operational_approval / legal_records','false / pending. 실제 기관 승인과 법령 적용 판단을 대신하지 않습니다.']])+table(['종료 코드','처리'],[
['전체 참조 0','필수 합성 확인 완료. 실제 운영 승인으로 해석하지 않습니다.'],
['전체 참조 3','격리 불가 등으로 일부 필수 검증 미완료. 우회하여 완료 처리하지 않습니다.'],
['오류 4','설정·파일·정책 등 오류. 문제를 해결하고 새 출력 경로로 재실행합니다.'],
['scan / gate의 2 또는 3','각각 deny / review. 참조 데모의 완료 코드와 개별 판정 코드를 구분하세요.']])+'''<p>공유 가능한 요약은 <code>reference-result.json</code>입니다. 출력 폴더 전체를 업로드하지 마세요. 개인 키가 들어 있는 역할별 폴더(<code>author/</code>·<code>approver/</code>·<code>operator/</code>·<code>auditor/</code>)와 <code>control-bootstrap.json</code>, 로컬 설정은 공개 대상이 아닙니다.</p></section>
<section id="control"><h2>6. 로컬 관리 화면 열기</h2>'''+control+'''<p>명령이 표시하는 <a href="http://127.0.0.1:8766/">http://127.0.0.1:8766/</a>에 접속합니다. 터미널에서 서버를 실행한 상태로 유지하세요. 새 터미널 또는 로컬 편집기로 <code>control-bootstrap.json</code>의 필요한 역할 토큰을 확인해 화면에 입력합니다. 토큰을 채팅·이슈·화면 공유에 붙이지 마세요.</p>'''+table(['역할','확인할 기능'],[
['author','정책 초안·검토 제출·등록된 실행에 대한 예외 요청'],
['approver','다른 작성자가 제출한 정책·예외의 독립 승인'],
['operator','승인 정책 묶음 발급·보관 잠금 관리'],
['auditor','자기 기관·프로젝트의 실행·정책·증적 열람']])+'''<p>역할은 합성 참조 신원입니다. 운영 OIDC·LDAP 연결이 아닙니다. 데모 이후 화면은 복구한 보관소를 사용하므로 보존 잠금된 합성 증적을 확인할 수 있습니다. 종료하려면 서버 터미널에서 Ctrl+C를 누릅니다.</p><p><strong>GitHub Pages는 이 안내 사이트만 호스팅합니다.</strong> 검사 엔진·민원 API·관리 서버는 로컬 환경에서 실행합니다.</p></section>
<section id="ci"><h2>7. CI 적용을 준비하기</h2><p>먼저 로컬 시험과 게이트 사용법을 확인하세요.</p>'''+tests+'''<ul><li><code>ci/reference-gate.sh</code>는 기본 입력 게이트, <code>ci/reference-signed-gate.sh</code>는 서명 정책 참조 예제입니다.</li><li>신뢰한 전체 expected commit, 현재 HEAD, 증적 commit, 프로필과 receipt를 대조합니다. expected commit을 검사 대상 저장소의 사용자 파일에서 읽지 않습니다.</li><li>서명 묶음·신뢰 목록·기관·프로젝트·최소 순번과 철회 자료는 검사 checkout 밖의 신뢰 경로에서 제공합니다.</li><li>승인 예외는 정확한 commit·도구·정책·탐지 의미에 결합합니다. 오류·미분석·review를 예외로 통과시키지 않습니다.</li><li>과거 archive 무결성 성공을 현재 commit의 통과 결과로 재사용하지 않습니다.</li></ul><p>CI 예제는 비활성 상태입니다. 대상 저장소와 담당자를 정한 뒤 필수 검사와 보호 브랜치를 설정해야 실제 병합·배포를 막을 수 있습니다. 운영 중인 민원 요청을 차단하는 기능이 아닙니다.</p></section>
<section id="pilot"><h2>8. 기관 파일럿을 준비하기</h2><p>이 체크리스트는 준비 상태를 살펴보기 위한 도구입니다. 선택 결과는 저장되거나 전송되지 않으며 기관 승인 기록이 되지 않습니다.</p><p class="progress" data-progress role="status" aria-live="polite"></p><ul class="checklist">'''+checklist+'''</ul><p>권장 순서는 합성 데모 → 승인된 제한 저장소의 관찰 검사 → 독립 정답과 탐지·오탐·검토 부담 측정 → 기관 검토 후 필수 게이트 적용입니다. 일정·비용·성능을 미리 보장하지 않습니다.</p><p>법령상 확정 의무, 기관 정책, 예시 정책, 미확인 요구를 각각 기록하세요. 예시 정책을 운영 의무로 자동 승격하지 마세요. REG-LOG-008 등 미확정 법령 적용 항목은 원문·부칙·기준일 대조와 담당자 판단이 필요합니다.</p></section>
<section id="troubleshooting"><h2>문제 해결</h2>'''+table(['증상','조치'],[
['ENVIRONMENT_EXISTS_USE_EXISTING_OR_NEW_PATH','기존 환경을 사용하거나 설치 명령에 --environment .runtime/reference-new를 지정합니다. 이후 명령의 인터프리터 경로도 함께 바꿉니다.'],
['출력 폴더가 이미 있음','기존 결과를 보존하고 새로운 --output 경로로 실행합니다. 자동 덮어쓰기는 하지 않습니다.'],
['격리 불가 / undeterminable / exit 3','macOS의 sandbox-exec와 로컬 실행 권한을 확인합니다. 다른 OS 또는 제한 실행기에서 완전 성공을 표시하지 않습니다.'],
['crypto·jsonschema 모듈 없음','전용 참조 환경 설치가 완료됐는지 확인하고 .runtime/reference-venv/bin/python으로 실행합니다.'],
['관리 화면 401 / 403','현재 데모의 올바른 역할 토큰과 기관·프로젝트를 확인합니다. 다른 역할로 차단을 우회하지 않습니다.'],
['게이트 오류·commit 불일치','신뢰한 expected commit·현재 HEAD·증적·프로필을 대조하고 수정 후 새 commit을 검사합니다.'],
['포트가 이미 사용 중','--port로 사용하지 않는 로컬 포트를 지정하고 접속 주소도 같은 포트로 바꿉니다.']])+'''</section>
<section id="evidence"><h2>검증 근거와 자세한 자료</h2><p>v0.9.0의 전체 단위·통합 시험 320개는 실패·건너뜀 없이 통과했습니다. 새 독립 합성 확인 표본 40건에서는 지원 위험 16/16 탐지, 지원 안전 오탐 0/16, 지원 표본 검토 필요 1/32, 전체 위험 allow 0건을 확인했습니다. 실제 기관 코드의 정확도나 법적 성능 기준을 뜻하지 않습니다.</p><p>최초 holdout의 검토 비율 실패와 수정 후 재실행도 구분해 보존했습니다. 실제 모델 실행과 품질은 검증하지 않았습니다.</p><ul><li><a href="'''+FILES+'''/docs/REFERENCE_RUNBOOK.md">프로젝트 실행 안내</a></li><li><a href="'''+FILES+'''/docs/RALPH_COMPLETION_REPORT.md">구현·검증 보고서</a></li><li><a href="'''+FILES+'''/docs/R2_CORPUS.md">평가 표본과 분모 설명</a></li><li><a href="'''+FILES+'''/docs/EXTERNAL_READINESS.md">실제 운영 준비 조건</a></li><li><a href="'''+FILES+'''/docs/REVIEW_LEDGER.md">독립 검토와 수정 기록</a></li><li><a href="downloads/govcode-harness-brochure.pdf">도입 검토용 PDF 브로슈어</a></li></ul><p class="small">프로젝트 코드는 Apache-2.0, 이 가이드·브로슈어는 CC BY 4.0입니다. <a href="license.html">출처 표시 예와 라이선스 범위</a>를 확인하세요. 제3자 라이선스 표시는 유지합니다.</p></section></article></div></main>''')

    page('brochure.html','도입 브로슈어','공공 프로젝트의 법령·규칙·가이드라인 충족을 작업·자동화·검토·증적으로 안내하는 GovCode Harness 도입 브로슈어.',
'''<main id="main"><div class="wrap brochure-tools"><div><h1 style="font:700 1.25rem/1.5 -apple-system,BlinkMacSystemFont,sans-serif;margin:0">도입 검토용 브로슈어</h1><p class="small" style="margin:3px 0 0">웹으로 읽거나 A4 2쪽 PDF로 공유하세요.</p></div><div class="actions"><a class="button" href="downloads/govcode-harness-brochure.pdf" download>PDF 다운로드</a><button class="button secondary" type="button" data-print>인쇄</button></div></div><div class="brochure">
<section class="sheet" aria-label="브로슈어 1쪽"><a class="brand" href="https://roboco.io/govcode-harness-guide/"><span class="mark" aria-hidden="true">G</span>GovCode Harness</a><h1>공공 프로젝트 규정을<br>실행 가능한<br>업무로 연결합니다.</h1><p class="deck">법령·규칙·가이드라인을 수행 작업과 충족 근거로.<br>적용 요구부터 자동화·검토·증적까지 안내하는 것이 제품의 목표입니다.</p>'''+platform_flow()+'''<div class="columns"><div class="feature"><h3>작업을 안내합니다</h3><p>프로젝트의 적용 요구를 수행 작업·산출물·검사에 연결하는 것이 목표입니다.</p></div><div class="feature"><h3>충족을 지원합니다</h3><p>자동 검사·수정 지원과 담당자 검토·승인을 연결합니다.</p></div><div class="feature"><h3>근거를 남깁니다</h3><p>작업·검사·수정·승인의 이력을 증적으로 추적합니다.</p></div></div><div class="band"><p><strong>공공 프로젝트의 수행자와 검토자가 같은 요구와 충족 근거를 확인하도록.</strong><br>기관 내부 실행을 지향하며, AI는 제안만 하고 승인과 판정을 대신하지 않습니다.</p></div><p class="small">목표 흐름을 설명한 자료입니다. 현재 v0.9.0은 민원 API 개인정보 로깅을 첫 사례로 구현했으며, 모든 분야의 규정 자동 충족 기능이 구현된 것은 아닙니다.</p><div class="sheet-foot"><span>© 2026 GovCode Harness contributors · <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></span><span>roboco.io/govcode-harness-guide/ · 1 / 2</span></div></section>
<section class="sheet" aria-label="브로슈어 2쪽"><span class="tag">첫 사례의 검증과 제품 확장</span><h2 style="margin-top:20px">민원 API 로깅은 첫 사례입니다.<br>제품의 목표는 공공 프로젝트 전반입니다.</h2><p>첫 사례의 회귀 시험 <strong>320개 통과</strong>, 실패 0·건너뜀 0.<br>로깅 위험 deny → 수정본 allow, 공통 정책·승인·증적·관리 기반을 확인했습니다. 다른 규정 분야의 검증 결과로 일반화하지 않습니다.</p><p class="small">새 독립 합성 표본 40건: 지원 위험 16/16 탐지, 지원 안전 오탐 0/16, 지원 검토 필요 1/32, 전체 위험 allow 0건. 실제 기관 코드 성능이나 준수 인증이 아닙니다.</p><ol class="steps"><li><span class="step-num">1</span><div><h3>프로젝트 요구 정리</h3><p>법령·규칙·가이드·계약상 기준의 적용 조건과 담당자를 정리합니다.</p></div></li><li><span class="step-num">2</span><div><h3>수행 작업과 검사 연결</h3><p>필요 산출물·자동 검사·수정 지원·담당자 검토·증적을 요구에 연결합니다.</p></div></li><li><span class="step-num">3</span><div><h3>한 분야씩 검증</h3><p>현재 로깅 사례를 실행하고, 추가 규정 분야마다 독립 정답과 성공 기준을 정합니다.</p></div></li><li><span class="step-num">4</span><div><h3>충족 현황과 변경 영향 관리</h3><p>미충족·미검증·검토 대기와 다음 작업을 안내하는 흐름을 후속 설계합니다.</p></div></li></ol><div class="note"><p><strong>확장 후보 / 분야별 규정 팩은 후속 설계</strong><br>개인정보·보안, 접근성, 개발 품질, 표준·상호운용성,<br>사업 수행·산출물, 운영·기록·보존. 적용 여부는 프로젝트별로 확인합니다.</p></div><p class="small">현재 검증: 제한된 Python 로깅 분석·macOS 격리·fixture 모델. 실제 LLM 품질·기관 승인·법령 적용 확정·실데이터 파일럿은 미검증입니다. 법령상 의무와 예시 정책을 구분합니다.</p><div><h3>가이드에서 시작하세요</h3><p><a href="'''+URL+'''onboarding.html">roboco.io/govcode-harness-guide/onboarding.html</a><br><a href="'''+TAG+'''">github.com/roboco-io/govcode-harness · Apache-2.0</a></p></div><div class="sheet-foot"><span>roboco-io / GovCode Harness contributors · <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></span><span>도입 일정·비용·실제 기관 성능은 별도 평가 · 2 / 2</span></div></section></div></main>''')
    page('license.html','라이선스와 출처 표시','프로젝트 Apache-2.0과 가이드 CC BY 4.0의 적용 범위 및 출처 표시 예를 안내합니다.',
        '<main id="main" class="wrap"><header class="page-head"><h1>라이선스와 출처 표시</h1><p>프로젝트 코드는 Apache-2.0, 가이드와 브로슈어는 CC BY 4.0으로 제공합니다.</p></header><article class="article" style="padding-bottom:60px"><section><h2>가이드 · CC BY 4.0</h2><p>별도 표시가 없는 가이드·브로슈어·자체 제작 시각 자료와 제작 소스는 Creative Commons Attribution 4.0 International로 제공합니다.</p><p>제목: GovCode Harness 도입 가이드 및 브로슈어<br>제공자: roboco-io / GovCode Harness contributors<br>원문: <a href="'+URL+'">'+URL+'</a></p><p><a rel="license" href="https://creativecommons.org/licenses/by/4.0/deed.ko">CC BY 4.0 한국어 안내</a> · <a href="downloads/CC-BY-4.0.txt">라이선스 원문 다운로드</a></p><h3>출처 표시 예</h3><blockquote><p>roboco-io / GovCode Harness contributors, 「GovCode Harness 도입 가이드 및 브로슈어」, https://roboco.io/govcode-harness-guide/, CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. 변경: 일부 문구를 수정하고 도표를 재구성함.</p></blockquote><p>실제 재사용 방식에 맞게 변경 여부를 표시하세요. 이 예는 라이선스에 추가 조건을 부과하지 않습니다.</p></section><section><h2>프로젝트 · Apache-2.0</h2><p>프로젝트 코드·설정·명령 인용은 Apache License 2.0을 따릅니다. 가이드의 CC BY 4.0이 프로젝트 코드나 제3자 자료의 라이선스를 대체하지 않습니다.</p><p><a href="'+REPO+'/blob/main/LICENSE">프로젝트 LICENSE</a> · <a href="'+REPO+'/blob/main/NOTICE">NOTICE</a> · <a href="https://github.com/roboco-io/govcode-harness-guide/blob/main/ATTRIBUTION.md">상세 출처와 적용 범위</a></p><p>선택적 오철칙 연동의 기존 MIT 라이선스와 저작권 표시는 유지합니다. 가이드의 합성 관리 화면 캡처 이미지 자체는 CC BY 4.0으로 제공하고, 화면을 구현한 프로젝트 코드는 Apache-2.0을 유지합니다.</p></section></article></main>')
    (SITE/'downloads/CC-BY-4.0.txt').write_bytes((ROOT/'LICENSE').read_bytes())
    (SITE/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="10" fill="#2457d6"/><path d="M45 20a18 18 0 1 0 1 23V32H31v8h7a10 10 0 1 1 1-14z" fill="white"/></svg>')
    (SITE/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+URL+'sitemap.xml\n')
    (SITE/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+URL+x+'</loc></url>' for x in ['index.html','onboarding.html','brochure.html','license.html'])+'</urlset>')
    print('Built 4 Korean pages, license download, sitemap, robots and favicon.')

if __name__=='__main__':
    build()
