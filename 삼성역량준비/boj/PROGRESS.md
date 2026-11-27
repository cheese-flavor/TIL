# 삼성코테 BOJ·CodeTree 통합 학습 진도

- 학습 과정: **Day 01 완료, Day 02~22 추가 21일**. [통합 3주 로드맵](PLAN_COMBINED_21D.md) 기준 백준 먼저 → 코드트리 잔여 문제.
- 현재 상태: **BOJ Day 04 완료 / Day 05 시작 대기**
- 학습 규칙: [CHAT_GUIDE.md](CHAT_GUIDE.md)
- 배정: BOJ 45개 및 기존 CodeTree 83개 중 대응 후보 43개를 중복 제외하여 잠정 85개. 기출 대응표는 공식 1:1 매핑이 아니며 세부 조건 재확인 가능. Day 01 완료 2개를 제외한 83개를 Day 02~22에 배정.
- 백준 채점 정답: **14문제 기록됨** (사용자 정답 보고 기준; 독립 채점 검증 미수행)
- 전체 진도: 정답 확인 **14/85문제(16.5%)**, 학습 진행 **14/85문제(16.5%)**. BOJ 정답 **14/45**(31개 남음), 학습 **14/45**(31개 미학습), CodeTree 잔여 **0/40**(40개 남음). 기존 CodeTree 학습 기록은 별도 보존.
- Day 01 solved.ac 수동 갱신: 미확인
- Day 02 solved.ac 수동 갱신: 미확인
- Day 03 solved.ac 수동 갱신: 미확인
- Day 04 solved.ac 수동 갱신: 미확인
- 확인 방법: 사용자가 지정 플랫폼에 직접 제출하고 정답 결과를 채팅에 보고; `BOJ 정답(사용자 보고)` 또는 `CodeTree 정답(사용자 보고)`로 명시. 미해결은 정답 집계에 넣지 않음.
- 이전 CodeTree 자료: `삼성역량준비/`의 기존 PLAN/solutions와 `TIL/codetree/` 보존

## 문제별 학습 기록

| Day | 날짜 | 백준 번호·문제 | 당시 확인 티어 | 독립 시도(분) | 제출 결과 및 증거 | 힌트/리뷰 | GitHub 코드·기록 | 재풀이 |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| 01 | 2026-11-24 | [13458 시험 감독](https://www.acmicpc.net/problem/13458) | Bronze II (공개 자료 기준) | 권장 30분 (실측 미기록) | **BOJ 정답(사용자 보고)** / 독립 검증 미수행 | 음수 잔여인원 예외·분기 순서 교정 / O(n) 시간·공간 | [day01/13458 코드·리뷰](solutions/day01/13458/README.md) | 미정 |
| 01 | 2026-11-24 | [14501 퇴사](https://www.acmicpc.net/problem/14501) | Silver III (공개 자료 기준) | 권장 40~45분 (실측 미기록) | **BOJ 정답(사용자 보고)** / 독립 검증 미수행 | 재귀 상태·선택/미선택·종료·가지치기 / 시간 O(2^N), 공간 O(N) | [day01/14501 코드·리뷰](solutions/day01/14501/README.md) | 권장: 다음 복습 세션, 실제 날짜 미정 |
| 02 | 2026-11-24~25 | [14888 연산자 끼워넣기](https://www.acmicpc.net/problem/14888) | Silver I (계획값) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 제출 원문 미대조 | 독립 if·상태 복원·음수 정수 나눗셈 | [코드·리뷰](solutions/day02/14888/README.md) | 미정 |
| 02 | 2026-11-24~25 | [14889 스타트와 링크](https://www.acmicpc.net/problem/14889) | Silver I (계획값) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 제출 원문 미대조 | 조합 DFS·선수 번호·대칭 제거 | [코드·리뷰](solutions/day02/14889/README.md) | 미정 |
| 02 | 2026-11-24~25 | [14503 로봇 청소기](https://www.acmicpc.net/problem/14503) | Gold V (계획값) | 실측 미기록 | **BOJ 정답(DFS, 사용자 보고)** / 제출 원문 미확보 / while 미확인 | 방향 배열·반시계 회전·return·반복문 | [코드·리뷰](solutions/day02/14503/README.md) | while 제출 확인 |
| 02 | 2026-11-24~25 | [14891 톱니바퀴](https://www.acmicpc.net/problem/14891) | Gold V (계획값) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 풀이 버전별 채점 미확인 | 회전 전 접점·문자열·0-based 인덱스 | [코드·리뷰](solutions/day02/14891/README.md) | 미정 |
| 03 | 2026-11-25 | [15686 치킨 배달](https://www.acmicpc.net/problem/15686) | Gold V (공개 자료 기준) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 실제 제출 원문 미대조 | 조합 DFS·리스트 복사·M개 선택 근거·거리 계산 | [코드·리뷰](solutions/day03/15686/README.md) | 미정 |
| 03 | 2026-11-25 | [20055 컨베이어 벨트 위의 로봇](https://www.acmicpc.net/problem/20055) | Gold V (계획 기준) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 실제 제출 원문 미대조 | 리스트 회전·pop 반환값·목적지 내구도·하차 처리 | [코드·리뷰](solutions/day03/20055/README.md) | 미정 |
| 03 | 2026-11-26 | [21608 상어 초등학교](https://www.acmicpc.net/problem/21608) | Gold V (계획 기준) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 실제 제출 원문 미대조 | 빈자리 후보·우선순위·만족도·튜플 비교 개선 | [코드·리뷰](solutions/day03/21608/README.md) | 개선 코드 복습 |
| 03 | 2026-11-26 | [21610 마법사 상어와 비바라기](https://www.acmicpc.net/problem/21610) | Gold V (계획 기준) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 실제 제출 원문 미대조 | 순환 좌표·이전/이후 상태 분리·비 내리기와 물복사 분리 | [코드·리뷰](solutions/day03/21610/README.md) | 미정 |
| 04 | 2026-11-27 | [3190 뱀](https://www.acmicpc.net/problem/3190) | Gold IV (계획 기준) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 제출 원문 미대조 | 리스트 구조·사과 제거·방향 전환 시점 | [코드·리뷰](solutions/day04/3190/README.md) | 미정 |
| 04 | 2026-11-27 | [14499 주사위 굴리기](https://www.acmicpc.net/problem/14499) | Gold IV (계획 기준) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 제출 원문 미대조 | 면 ID·점수 분리·두 축 동기화·입력 및 인덱스 | [코드·리뷰](solutions/day04/14499/README.md) | 미정 |
| 04 | 2026-11-27 | [14500 테트로미노](https://www.acmicpc.net/problem/14500) | Gold IV (계획 기준) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 제출 원문 미대조 | DFS 방문·복원·T형 중심 유지 분기 | [코드·리뷰](solutions/day04/14500/README.md) | 미정 |
| 04 | 2026-11-27 | [14502 연구소](https://www.acmicpc.net/problem/14502) | Gold IV (계획 기준) | 실측 미기록 | **BOJ 정답(사용자 보고)** / 제출 원문 미대조 | 조합·영역 DFS, return 및 종료 조건, 행별 복사 | [코드·리뷰](solutions/day04/14502/README.md) | DFS 복습 권장 |

## Day 진행표

| Day | 문제 수 | 진도 | 비고 |
| --- | ---: | --- | --- |
| [BOJ Day 01](solutions/day01/README.md) | 2문제 계획 / 2문제 정답 | **완료** | 13458·14501 정답(사용자 보고), solved.ac 갱신 미확인 |
| [BOJ Day 02](solutions/day02/README.md) | 4문제 학습 / 4문제 정답 | **완료** | 4문제 정답(사용자 보고), 실제 제출 코드 미대조, solved.ac 갱신 미확인 |
| [BOJ Day 03](solutions/day03/README.md) | 4문제 계획 / 4문제 정답 | **완료** | 4문제 정답(사용자 보고), 실제 제출 원문 미대조, solved.ac 갱신 미확인 |
| [BOJ Day 04](solutions/day04/README.md) | 4문제 계획 / 4문제 정답 | **완료** | 4문제 정답(사용자 보고), 제출 원문 미대조, solved.ac 갱신 미확인 |
| Day 05 (BOJ) | 4문제 계획 | 시작 전 | Gold IV (계획값; 시작 시 확인) |
| Day 06 (BOJ) | 4문제 계획 | 시작 전 | Gold III (계획값; 시작 시 확인) |
| Day 07 (BOJ) | 4문제 계획 | 시작 전 | Gold III (계획값; 시작 시 확인) |
| Day 08 (BOJ) | 4문제 계획 | 시작 전 | Gold III → Gold II (계획값; 시작 시 확인) |
| Day 09 (BOJ) | 4문제 계획 | 시작 전 | Gold II (계획값; 시작 시 확인) |
| Day 10 (BOJ) | 4문제 계획 | 시작 전 | Gold II (계획값; 시작 시 확인) |
| Day 11 (BOJ) | 4문제 계획 | 시작 전 | Gold I (계획값; 시작 시 확인) |
| Day 12 (BOJ) | 3문제 계획 | 시작 전 | Gold I (계획값; 시작 시 확인) |
| Day 13 (CodeTree) | 4문제 계획 | 시작 전 | L12 (계획값; 시작 시 확인) |
| Day 14 (CodeTree) | 4문제 계획 | 시작 전 | L12 → L13 (계획값; 시작 시 확인) |
| Day 15 (CodeTree) | 4문제 계획 | 시작 전 | L13 (계획값; 시작 시 확인) |
| Day 16 (CodeTree) | 4문제 계획 | 시작 전 | L13 (계획값; 시작 시 확인) |
| Day 17 (CodeTree) | 4문제 계획 | 시작 전 | L13 (계획값; 시작 시 확인) |
| Day 18 (CodeTree) | 4문제 계획 | 시작 전 | L14 (계획값; 시작 시 확인) |
| Day 19 (CodeTree) | 4문제 계획 | 시작 전 | L14 → L15 (계획값; 시작 시 확인) |
| Day 20 (CodeTree) | 4문제 계획 | 시작 전 | L15 (계획값; 시작 시 확인) |
| Day 21 (CodeTree) | 4문제 계획 | 시작 전 | L16 → L17 (계획값; 시작 시 확인) |
| Day 22 (CodeTree) | 4문제 계획 | 시작 전 | L17 → L18 → L19 (계획값; 시작 시 확인) |

- Day 종료 시 solved.ac [연동 설정](https://solved.ac/settings/integrations) 링크 안내(사용자 직접 갱신; 보고 여부 별도 기록).

 > 정답 기록과 설명·리뷰는 별개. 실제 제출 근거를 확인하지 못하면 정답으로 처리하지 않음.
