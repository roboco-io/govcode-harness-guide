# GovCode Harness 도입 가이드

**프로젝트 목적:** 다양한 공공 프로젝트에서 비개발자가 안전하게 바이브 코딩을 할 수 있도록 한다. [의도 문서](INTENT.md)를 이 저장소의 가이드·홍보 문구의 기준으로 삼는다.

**보안이 내재화된 개발 하네스**를 지향하는 GovCode Harness의 한국어 온보딩 가이드와 마케팅 브로슈어를 제공한다. 보안 기준을 개발 흐름의 검사·수정 지원·승인·증적에 연결하는 가치와 첫 도입 경로를 설명한다.
제품의 전체 목표와 현재 구현을 구분한다. v0.10.0 프리뷰는 프로젝트 정보·규정 팩·문서 초안 생성 기반을 제공하며 비개발자의 전체 제작 경험 완성을 뜻하지 않는다.

- 공개 사이트: https://roboco.io/govcode-harness-guide/
- 업데이트 안내: https://roboco.io/govcode-harness-guide/updates.html
- 본 프로젝트: https://github.com/roboco-io/govcode-harness
- 비개발자를 위한 쉬운 안내: https://roboco.io/govcode-harness-guide/start.html
- 개발 담당자용 설치·실행: https://roboco.io/govcode-harness-guide/onboarding.html
- 브로슈어: https://roboco.io/govcode-harness-guide/brochure.html
- PDF: https://roboco.io/govcode-harness-guide/downloads/govcode-harness-brochure.pdf

## 제품 기획 문서

- [PR 보도자료 초안](https://roboco.io/govcode-harness-guide/pr.html)
- [고객·내부 FAQ](https://roboco.io/govcode-harness-guide/faq.html)

[Working Backwards PR/FAQ 초안](docs/PR_FAQ.md)은 다양한 공공 프로젝트에서 비개발자가 직접 안전하게 바이브 코딩을 하는 목표 경험과 고객·내부 질문, 파일럿 검증 과제를 정리한 검토용 문서다. 미래 출시 가정과 현재 구현 상태를 구분한다.

## 파일럿과 무상 사용

현재 프로젝트는 **파일럿 단계**다. 본 프로젝트 코드는 Apache-2.0 조건에 따라 개인·기관·기업이 라이선스 비용이나 로열티 없이 사용·수정·재배포할 수 있다. 상업적 이용도 가능하다. 재배포 조건과 무보증 조항을 따르며 설치·인프라·운영 비용은 별도다. 이 가이드와 브로슈어는 CC BY 4.0이다.

[웹 피드백·기여 안내](https://roboco.io/govcode-harness-guide/community.html) · [기여 방법](CONTRIBUTING.md) · [가이드 이슈](https://github.com/roboco-io/govcode-harness-guide/issues/new/choose) · [본 프로젝트 이슈](https://github.com/roboco-io/govcode-harness/issues/new/choose)

## 버전 대응

| 가이드 | 기준 코드 | 검증 범위 |
| --- | --- | --- |
| 현재 가이드 | [v0.10.0 프리뷰](https://github.com/roboco-io/govcode-harness/tree/v0.10.0) | macOS·Python 3.12 로컬 참조, 합성 자료·역할, fixture 모델 |

두 저장소는 서브모듈 없이 독립적으로 관리한다. 가이드의 명령과 주장은 고정 코드 태그를 기준으로 한다. 본 프로젝트의 태그를 바꾸면 버전 대응표와 페이지 내 링크·검증 결과를 함께 갱신한다.

## 프로젝트 업데이트 기준

2026-10-30 공개된 프리릴리스 `v0.10.0`(커밋 `7d60fdb677b6792cf6b7dd451a3b87a6d038fa91`)를 기준으로 한다. 프로젝트 프로필·규정 팩 발행·버전 고정·적용 대상 판단과 설계 문서 초안 생성이 공개됐다. 산출물 검사·충족 평가·새 단계 게이트·관리 화면 확장은 후속 범위다.
릴리스 검증 기록은 439개 시험 통과를 보고한다. 가이드 작업에서는 고정 태그의 실행 명령과 문서를 대조하며 전체 시험 결과를 별도로 재실행한 것으로 표현하지 않는다.

## 화면 테마

상단에 본 프로젝트 GitHub 링크와 테마 전환 버튼이 있다. 최초 방문에는 기기의 다크·라이트 설정을 따른다. 수동 선택은 브라우저에 저장하고, ‘자동’을 누르면 기기 설정으로 돌아간다. 저장이 제한된 환경에서도 현재 화면의 전환은 동작한다. 인쇄·PDF는 밝은 배경을 유지한다.

Playwright와 Chrome이 준비된 제작 환경에서 `node scripts/check_theme.mjs`로 기기 설정·선택 저장·페이지 이동·인쇄·저장 제한 및 화면 너비를 확인한다.

## 로컬 제작

Python 3.10 이상으로 실행한다. 사이트에는 외부 폰트·분석 도구·서버 의존성이 없다.

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
python3 -m http.server 8877 --bind 127.0.0.1 --directory site
```

브라우저에서 `http://127.0.0.1:8877/`를 연다. 소스는 `scripts/build_site.py`와 `site/assets/`다. 생성된 HTML도 커밋하므로 Pages가 Python을 실행할 필요가 없다.

## PDF 갱신

`brochure.html`과 PDF는 같은 HTML·인쇄 CSS를 사용한다. Chromium의 인쇄 기능에서 A4, 배경 그래픽 사용, 여백 없음, 머리글·바닥글 없음으로 저장할 수 있다. 공식 PDF는 `site/downloads/govcode-harness-brochure.pdf`에 둔다.

Playwright가 준비된 제작 환경에서는 다음 스크립트로 재생성할 수 있다.

```sh
node scripts/export_pdf.mjs
# Playwright 전용 Chromium 대신 설치된 Chrome을 사용할 경우:
PLAYWRIGHT_CHANNEL=chrome node scripts/export_pdf.mjs
```

PDF는 A4 2쪽인지 확인하고, 한글·잘림·공백 페이지를 이미지로 검토한 뒤 게시한다. 웹 문구를 바꾸면 PDF도 다시 만든다.

## GitHub Pages 배포

`main`은 제작 소스, `gh-pages`는 `site/`의 정적 배포 결과다. 저장소 Pages 설정은 `gh-pages`의 루트를 가리킨다.

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
git add README.md scripts site
git commit -m "docs: update adoption guide"
git push origin main
git subtree push --prefix site origin gh-pages
```

실제 Pages 배포 성공 후 공개 URL에서 소개·온보딩·브로슈어·PDF를 확인한다. PDF와 `downloads/SHA256SUMS`도 함께 갱신한다. 빌드·검증은 `.runtime` 또는 외부 작업 경로에서 수행하고 토큰·개인 키·로컬 설정을 커밋하지 않는다.

실제 검사기와 관리 서버는 GitHub Pages에서 실행하지 않는다. 사이트는 안내와 공개 자료만 제공한다.

## 라이선스와 출처 표시

가이드·브로슈어·자체 제작 자료·제작 소스는 [CC BY 4.0](LICENSE)으로 제공한다. 제공자는 roboco-io / GovCode Harness contributors다.
재사용 시 출처와 라이선스 링크를 표시하고 변경한 경우 변경 사실을 표시한다. [출처 표시 예와 범위](ATTRIBUTION.md)를 따른다.
프로젝트 코드와 그 인용은 Apache-2.0, 별도 제3자 자료는 해당 원래 라이선스를 유지한다.
