# 백준 브론즈 전수 학습

Python 기초 문법·구현 능력·문제 해석 및 풀이 속도 향상을 위한 일일 학습 기록.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

## 학습 개요

- 대상: 백준 출처 Bronze V~I 및 동일 레벨 새싹 문제
- 기준: solved.ac 난이도 값 1~5, BOJ 원본 문제 번호
- 시간: 하루 1~2시간, 초기 15문제, 이후 12문제 기준
- 진행: 유형 미공개 → 직접 풀이 → 코드 검토 → 실제 채점 확인 → 일일 기록
- 삼성역량준비와 독립 운영

## 현재 상태 (2026-11-28)

- DAY001: 기존 채팅 배정 15문제 유지, 정답 확인 기록 없음
- DAY002~005: 기존 계획 60문제 임시 배정
- 초기 목록 총 75개 고유 번호, 최신 난이도·제출 가능 여부 및 기존 AC 재확인 필요
- 전체 문제 수·전체 회차: 미확정 (solved.ac 전체 목록 조회 실패)
- 75개는 전체 모집단이 아닌 초기 후보 목록

## 구성

| 경로 | 역할 |
|---|---|
| [CURRICULUM.md](CURRICULUM.md) | 일별 배정 및 전수 배정 기준 |
| [PROGRESS.md](PROGRESS.md) | 정답 확인 및 누적 현황 |
| [problem_list.csv](problem_list.csv) | 문제 번호·배정·검증 상태 |
| [DAY001](DAY001/) | 첫 회차 문제와 리뷰 |
| [tools/assign_curriculum.py](tools/assign_curriculum.py) | 검증된 전체 목록을 바탕으로 후속 배정 생성 (미실행) |

## 기록 방식

- 채팅: 백준 브론즈 DAY001 시작 / 마무리
- 코드: DAYxxx/문제번호_문제명.py (사용자 실제 최종 풀이)
- 리뷰: DAYxxx/review.md (복잡도, 반례, 오답 원인)
- 한국어 커밋 메시지, 실제 원격 반영 확인 후 완료 보고

## 출처와 한계

- [solved.ac 난이도 기준](https://help.solved.ac/ko/problem/level)
- [solved.ac 공지사항](https://solved.ac/notices)
- 2026년 11월 solved.ac 개편으로 여러 저지의 문제 번호가 통합되므로 BOJ 원본 ID를 확인하여 집계.
- 전체 검색 및 기존 API 응답 미확보. 전체 목록 확보 전에는 누적 전수 진행률 미산정.
- 정답 및 Python 제출 가능 여부는 실제 확인 전까지 미확인으로 유지.
