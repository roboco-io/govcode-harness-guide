# 제작·검증 기록

기준일: 2026-10-29 KST. 기준 소스: roboco-io/govcode-harness의 v0.9.0 태그.

## 로컬 확인

- 본 프로젝트 전체 회귀: `.runtime/reference-venv/bin/python -m unittest discover -s tests -p 'test_*.py' -q`로 320개, 실패 0·건너뜀 0, 88.810초.
- 본 프로젝트 계약 검사: 예시 28개·잘못된 계약 8개 거부·로컬 참조 76개.
- 공개된 v0.9.0을 새 폴더에 clone하고 기본 demo 실행: 위험본 deny·수정본 allow, 응답·원문 로그 제거·감사 호출 보존 모두 true.
- 가이드 생성: `python3 scripts/build_site.py`.
- 정적 검사: `python3 scripts/check_site.py`로 한국어 페이지 3개, 내부 경로·앵커 41개, PDF 해시와 공개 파일 경계 확인.
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
