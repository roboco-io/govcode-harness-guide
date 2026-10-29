# 제작·검증 기록

기준일: 2026-10-29 KST. 기준 소스: roboco-io/govcode-harness의 v0.9.0 태그.

## 로컬 확인

- 본 프로젝트 전체 회귀: `.runtime/reference-venv/bin/python -m unittest discover -s tests -p 'test_*.py' -q`로 320개, 실패 0·건너뜀 0, 88.810초.
- 본 프로젝트 계약 검사: 예시 28개·잘못된 계약 8개 거부·로컬 참조 76개.
- 공개된 v0.9.0을 새 폴더에 clone하고 기본 demo 실행: 위험본 deny·수정본 allow, 응답·원문 로그 제거·감사 호출 보존 모두 true.
- 가이드 생성: `python3 scripts/build_site.py`.
- 정적 검사: `python3 scripts/check_site.py`로 한국어 페이지 3개, 내부 경로·앵커 42개, PDF 해시와 공개 파일 경계 확인.
- 실제 브라우저: 1440×1000·390×844에서 세 페이지의 가로 넘침 없음. 이미지 로드, 명령 복사, 8개 준비 항목의 진행 표시 확인.
- PDF 재생성: 설치된 Chrome을 사용한 `PLAYWRIGHT_CHANNEL=chrome node scripts/export_pdf.mjs` 성공. Playwright 기본 전용 Chromium이 없는 환경에서는 브라우저 설치 또는 channel 지정 필요.
- 최종 PDF: A4 2쪽, 한글·표시 범위·페이지 번호를 이미지로 검토. PDF 링크에 localhost·127.0.0.1이 없음을 확인.

이 기록은 로컬 참조·정적 안내 사이트의 검증이다. 실제 기관 파일럿·운영 승인·실모델 성능 검증을 뜻하지 않는다.

## 공개 배포 확인

- 두 저장소의 공개 상태와 본 프로젝트 v0.9.0 태그를 GitHub API에서 확인했다.
- 최초 Pages 배포: https://github.com/roboco-io/govcode-harness-guide/actions/runs/40794320174 — completed / success.
- Pages 소스: gh-pages 루트. 조직의 기존 도메인을 상속하며 https://roboco.io/govcode-harness-guide/로 연결된다. 해당 새 사이트의 HTTPS 강제를 활성화했다.
- 공개 주소에서 소개·온보딩·브로슈어·PDF·해시 파일·CSS·JS·화면 이미지가 모두 HTTP 200으로 응답했다.
- 본 프로젝트와 가이드는 서브모듈 없이 독립 저장소·고정 코드 태그 링크로 연결했다.

## 제품 목적 정리

사용자 설명에 따라 제품 목적을 공공 프로젝트의 각종 법령·규칙·가이드라인 충족 안내로 정리했다. 개인정보 로깅은 첫 Vertical Slice로 명시했다.
소개·온보딩·브로슈어를 같은 목적에 맞추고, 적용 영역 확장 후보와 현재 v0.9.0 구현·검증을 구분했다.
본 프로젝트의 INTENT.md·제품 방향·PRD·아키텍처·ADR-0012와 연결한다. 실제 새 규정 검사 기능을 구현했다는 주장은 하지 않는다.
1440px·390px에서 세 페이지 가로 넘침이 없고, 수정 PDF가 A4 2쪽이며 각 페이지에 글자 잘림이 없음을 확인했다.
검사 엔진과 시험 코드는 변경하지 않았으므로 기존 320개 회귀 결과를 다른 규정 영역의 결과로 확대하지 않는다.

## 라이선스 적용

본 프로젝트 Apache-2.0, 별도 가이드 CC BY 4.0을 사용자 지시에 따라 적용했다.
가이드 LICENSE는 CC 공식 법적 원문의 사본이며 웹 다운로드와 같은 바이트다. ATTRIBUTION.md와 license.html에 제공자·출처·변경 표시 예·별도 라이선스 범위를 적었다.
라이선스 페이지를 포함한 한국어 4쪽, 로컬 경로·앵커 56개, PDF SHA-256이 정적 검사를 통과했다.
PDF는 A4 2쪽이며 양쪽 페이지의 CC BY 4.0 표시·클릭 링크와 한글 배치를 검토했다.
소스 기준 태그는 기존 v0.9.0을 보존한 v0.9.0-apache2다. 본 프로젝트 wheel의 SPDX 라이선스와 Apache LICENSE·NOTICE·기존 MIT 원문 포함을 확인했다.
검사 엔진과 기존 회귀 시험의 소스는 변경하지 않았다.
