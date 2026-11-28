# DAY001 학습 기록

- 시작 안내: 2026-11-27 / 종료: 2026-11-28
- 목표: 15문제 / 1~2시간 (실제 소요 시간 미확인)
- 결과: 15/15 정답, 미해결 및 이월 없음
- 출처: 백준 채점 결과에 대한 사용자 확인 및 채팅에 제공된 최종 Python 코드. 별도 제출 페이지 재검증·로컬 실행 미실시.
- 난이도: 기존 배정 기준 (최신 solved.ac 메타데이터 미검증)

| 번호 | 제목 / 최종 코드 | 난이도 | 시간 | 공간 | 채점 |
|---|---|---|---|---|---|
| [1000](https://acmicpc.net/problem/1000) | [A+B](<1000_A+B.py>) | Bronze V | O(1) | O(1) | 정답 |
| [1001](https://acmicpc.net/problem/1001) | [A-B](<1001_A-B.py>) | Bronze V | O(1) | O(1) | 정답 |
| [1271](https://acmicpc.net/problem/1271) | [엄청난 부자2](<1271_엄청난 부자2.py>) | Bronze V | O(1) | O(1) | 정답 |
| [1330](https://acmicpc.net/problem/1330) | [두 수 비교하기](<1330_두 수 비교하기.py>) | Bronze V | O(1) | O(1) | 정답 |
| [2420](https://acmicpc.net/problem/2420) | [사파리월드](<2420_사파리월드.py>) | Bronze V | O(1) | O(1) | 정답 |
| [10039](https://acmicpc.net/problem/10039) | [평균 점수](<10039_평균 점수.py>) | Bronze IV | O(1) | O(1) | 정답 |
| [2845](https://acmicpc.net/problem/2845) | [파티가 끝나고 난 뒤](<2845_파티가 끝나고 난 뒤.py>) | Bronze IV | O(1) | O(1) | 정답 |
| [10797](https://acmicpc.net/problem/10797) | [10부제](<10797_10부제.py>) | Bronze IV | O(1) | O(1) | 정답 |
| [11365](https://acmicpc.net/problem/11365) | [!밀비 급일](<11365_!밀비 급일.py>) | Bronze IV | O(Σ L²) (최악) | O(max L) | 정답 |
| [1085](https://acmicpc.net/problem/1085) | [직사각형에서 탈출](<1085_직사각형에서 탈출.py>) | Bronze III | O(1) | O(1) | 정답 |
| [1267](https://acmicpc.net/problem/1267) | [핸드폰 요금](<1267_핸드폰 요금.py>) | Bronze III | O(N) | O(N) | 정답 |
| [1547](https://acmicpc.net/problem/1547) | [공](<1547_공.py>) | Bronze III | O(N) | O(1) | 정답 |
| [1075](https://acmicpc.net/problem/1075) | [나누기](<1075_나누기.py>) | Bronze II | O(1) | O(1) | 정답 |
| [1100](https://acmicpc.net/problem/1100) | [하얀 칸](<1100_하얀 칸.py>) | Bronze II | O(1) (8×8 고정) | O(1) (8×8 고정) | 정답 |
| [1032](https://acmicpc.net/problem/1032) | [명령 프롬프트](<1032_명령 프롬프트.py>) | Bronze I | O(NM) | O(NM) | 정답 |

## 종료 리뷰

- 난이도별: Bronze V 5, IV 4, III 3, II 2, I 1 (기존 배정 기준).
- 1547: 다중 할당의 좌변이 순차 평가되어 첫 할당 뒤 index() 결과가 바뀜. 두 인덱스를 미리 저장해 해결.
- 1075: 나머지 연산 대신 몫 연산으로 마지막 두 자리 제거 후 00~99 순회.
- 1100: F는 말, 점은 빈 칸. 행과 열의 홀짝성이 동일하면 하얀 칸. (i+j)%2 == 0으로 조건 단순화 가능.
- 1032: 문자열은 불변 객체이므로 list()로 변환 후 수정하고 ''.join()으로 복원. N=1의 별도 분기 불필요.
- 추가 복습: abs(), max(), count(), 슬라이싱 [::-1], f-string :02d, 반복문 원소 직접 순회.
- 복잡도 기준: N은 입력 개수, M은 파일명 길이, L은 각 문자열 길이. 고정 크기는 O(1)로 표기. 큰 정수의 비트 복잡도는 별도이며 1271은 문제의 제한 범위 기준. 11365 문자열 연결은 최악 기준이며 CPython 최적화 가능.
- 최종 코드는 사용자 풀이를 유지하고 개선 제안은 리뷰에만 기록.
