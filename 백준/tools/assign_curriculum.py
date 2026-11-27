"""검증된 BOJ Bronze 전체 CSV를 바탕으로 기존 배정을 보존한 후속 배정 초안 생성."""
import argparse
import csv
import random
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["problem_id", "title", "level", "day", "assignment_status",
          "study_status", "prior_ac", "python_status", "metadata_status", "url"]

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def quotas(day):
    if day <= 5:
        return [5, 4, 3, 2, 1]
    if day <= 10:
        return [4, 4, 3, 2, 2]
    if day <= 20:
        return [3, 3, 3, 3, 2]
    return [3, 3, 2, 2, 2]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--expected-count", type=int, required=True,
                        help="동일 기준 시점·출처의 검증된 전체 BOJ Bronze 고유 건수")
    args = parser.parse_args()
    catalog = {}
    for r in read_csv(args.snapshot):
        if r["source"].strip().upper() != "BOJ":
            raise ValueError("BOJ 출처 외 데이터 포함")
        pid, level = int(r["problem_id"]), int(r["level"])
        if pid <= 0 or level not in range(1, 6) or not r["title"].strip():
            raise ValueError(f"잘못된 메타데이터: {pid}")
        if pid in catalog:
            raise ValueError(f"중복 BOJ ID: {pid}")
        catalog[pid] = dict(r, level=level, problem_id=pid)
    if len(catalog) != args.expected_count or not catalog:
        raise ValueError("전체 건수 불일치 또는 빈 목록")

    previous = {}
    for r in read_csv(ROOT / "problem_list.csv"):
        pid = int(r["problem_id"])
        if pid in previous:
            raise ValueError(f"기존 배정 중복: {pid}")
        if pid not in catalog:
            raise ValueError(f"기존 ID가 전체 목록에 없음: {pid}; 수동 검토 필요")
        previous[pid] = r

    def make(pid, day, old=None):
        r = catalog[pid]
        old = old or {}
        return dict(problem_id=pid, title=r["title"], level=r["level"], day=day,
                    assignment_status=old.get("assignment_status", "assigned"),
                    study_status=old.get("study_status", "unconfirmed"),
                    prior_ac=old.get("prior_ac") if old.get("prior_ac") not in (None, "", "unknown") else r.get("prior_ac") or "unknown",
                    python_status=old.get("python_status") if old.get("python_status") not in (None, "", "unknown") else r.get("python_status") or "unknown",
                    metadata_status="snapshot_imported",
                    url=f"https://acmicpc.net/problem/{pid}")

    result = [make(pid, r["day"], r) for pid, r in previous.items()]
    pools = {}
    rng = random.Random(20261128)
    for level in range(1, 6):
        ids = sorted(pid for pid, r in catalog.items()
                     if pid not in previous and r["level"] == level)
        rng.shuffle(ids)
        pools[level] = deque(ids)
    day = max((int(r["day"][3:]) for r in result if r["day"]), default=0) + 1
    while any(pools.values()):
        selected = []
        q = quotas(day)
        for level, target in enumerate(q, 1):
            for _ in range(min(target, len(pools[level]))):
                selected.append(pools[level].popleft())
        while len(selected) < sum(q) and any(pools.values()):
            for level in range(1, 6):
                if pools[level] and len(selected) < sum(q):
                    selected.append(pools[level].popleft())
        rng.shuffle(selected)
        result.extend(make(pid, f"DAY{day:03d}") for pid in selected)
        day += 1
    if len(result) != len(catalog) or {r["problem_id"] for r in result} != set(catalog):
        raise RuntimeError("누락 또는 중복 배정")
    out = ROOT / "generated"
    out.mkdir(exist_ok=True)
    with (out / "problem_list.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(result)
    counts = Counter(r["level"] for r in result)
    by_day = {}
    for r in result:
        by_day.setdefault(r["day"], []).append(r)
    lines = ["# 전체 배정 초안", "", f"- 전체 문제: {len(result)}",
             f"- 전체 회차: {len(by_day)}", "- 입력 목록의 출처·건수 검증은 입력 제공자가 수행",
             "- 기존 배정 유지, 최신 레벨 변경 및 기존 AC/Python 제한은 별도 검토 필요", "",
             "| 레벨 | 수 |", "|---|---:|"]
    lines += [f"| {i} | {counts[i]} |" for i in range(1, 6)]
    lines += ["", "| 회차 | 문제 번호 | 수 |", "|---|---|---:|"]
    for d, rs in sorted(by_day.items(), key=lambda x: int(x[0][3:])):
        links = ", ".join(f'[{r["problem_id"]}]({r["url"]})' for r in rs)
        lines.append(f"| {d} | {links} | {len(rs)} |")
    (out / "CURRICULUM.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"총 {len(result)}문제 / {len(by_day)}회차: {dict(sorted(counts.items()))}")
    print("generated/에 초안 저장. 기존 파일은 변경하지 않음.")

if __name__ == "__main__":
    main()
