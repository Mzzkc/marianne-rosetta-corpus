#!/usr/bin/env python3
"""Offline fixtures and behavioral gates for the six long-tail demonstrations.

These gates establish artifact structure, source joins, routing, compression and
learning consumption. They do not certify the quality of an editorial argument
or measure provider billing. Run with MODE WORKSPACE [VOICE]. No third-party deps.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from pathlib import Path


def write(root: Path, name: str, value: object) -> None:
    (root / name).write_text(json.dumps(value, indent=2) + "\n")


def read(root: Path, name: str):
    return json.loads((root / name).read_text())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prose(value: str) -> None:
    assert isinstance(value, str) and len(value.strip()) >= 12, "substantive text required"


def unique(rows: list[dict]) -> dict[str, dict]:
    assert isinstance(rows, list), "expected a list"
    indexed = {row["id"]: row for row in rows}
    assert len(indexed) == len(rows), "duplicate ids"
    return indexed


def initialize(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(__file__, root / "proof_checks.py")
    write(
        root,
        "source.json",
        {
            "text": {
                "s1": "Retry a write only with the same operation identifier.",
                "s2": "A timeout leaves completion unknown until a receipt is inspected.",
            }
        },
    )
    write(
        root,
        "positions.json",
        {
            "ava": {"author": "Ava", "position": "adopt", "text": "The pilot needs two workers."},
            "bo": {"author": "Bo", "position": "defer", "text": "Rollback takes one hour."},
            "chen": {"author": "Chen", "position": "adopt", "text": "Three workers are available."},
        },
    )
    lines = []
    for number in range(200):
        critical = number in (50, 150)
        message = {
            50: "TLS certificate expired on the public endpoint.",
            150: "Database connection pool exhausted on checkout.",
        }.get(number, "Health probe succeeded; no intervention needed. " * 5)
        lines.append(json.dumps({"id": f"L{number:03}", "critical": critical, "text": message}))
    (root / "raw-log.jsonl").write_text("\n".join(lines) + "\n")
    for voice, fact in [
        (1, "Use request_id in the API example."),
        (2, "Retry requires a saved receipt."),
    ]:
        write(
            root,
            f"task-{voice}.json",
            {
                "owner": voice,
                "finding": fact,
                "assignment": "Revise your section using this finding and the peer's later signal.",
            },
        )
    write(root, "cases.json", {"a": "  ALPHA ", "b": "Beta  ", "c": " gamma "})
    write(root, "run-1.json", {k: v.strip() for k, v in read(root, "cases.json").items()})
    write(
        root,
        "questions.json",
        {
            "a": "Reserve 2 crates plus 3 crates. Total crates?",
            "b": "Four shelves hold 3 crates each. Total crates?",
            "c": "How many crates can site C still accept? Requires packet C.",
            "d": "Can delivery D proceed (1=yes, 0=no)? Requires policy D and exception record.",
        },
    )
    write(root, "packet-c.json", {"capacity": 40, "used": 25, "held": 5})
    write(
        root,
        "policy-d.json",
        {
            "route_closed": True,
            "rule": "A closed route permits delivery only with a signed exception.",
        },
    )
    write(root, "exception-d.json", {"signed_exception": False})
    print("Offline fixtures ready; no external services or publication.")


def page_first(root: Path) -> None:
    rows = unique(read(root, "commentary-1.json"))
    assert set(rows) == {"c1", "c2"}
    assert {r["source"] for r in rows.values()} == {"s1", "s2"}
    for row in rows.values():
        prose(row["text"])


def page_second(root: Path) -> None:
    page_first(root)
    first = unique(read(root, "commentary-1.json"))
    second = unique(read(root, "commentary-2.json"))
    assert set(second) == {"r1", "r2"}
    assert {r["reply_to"] for r in second.values()} == set(first)
    for row in second.values():
        assert row["source"] == first[row["reply_to"]]["source"], "reply lost its source anchor"
        prose(row["text"])


def page(root: Path) -> None:
    page_second(root)
    text = (root / "page.md").read_text()
    anchors = re.findall(r'<a id="([^"]+)"></a>', text)
    assert len(set(anchors)) == len(anchors), "duplicate page anchor"
    assert set(anchors) == {"s1", "s2", "c1", "c2", "r1", "r2"}
    links = re.findall(r"\]\(#([^)]+)\)", text)
    assert set(links) <= set(anchors), "broken page cross-reference"
    for value in read(root, "source.json")["text"].values():
        assert value in text, "central text lost"
    for row in read(root, "commentary-1.json") + read(root, "commentary-2.json"):
        assert row["text"] in text, "commentary lost from published page"
        section = text.split(f'<a id="{row["id"]}"></a>', 1)[1].split('<a id="', 1)[0]
        assert f"](#{row['source']})" in section, "source link missing from layer"
        if "reply_to" in row:
            assert f"](#{row['reply_to']})" in section, "peer link missing from reply layer"


def weave(root: Path) -> None:
    inputs = read(root, "positions.json")
    output = read(root, "editorial.json")
    assert output["position"] in {"adopt", "defer"}
    prose(output["argument"])
    prose(output["conclusion"])
    assert output["support"], "position needs cited support"
    for row in output["support"]:
        source = inputs[row["source"]]
        assert row["quote"] and row["quote"] in source["text"], "invented support quote"
        assert source["position"] == output["position"], "support contradicts the chosen stance"
    dissent = output["dissent"]
    source = inputs[dissent["source"]]
    assert dissent["author"] == source["author"], "dissent must name the actual author"
    assert dissent["quote"] and dissent["quote"] in source["text"], "invented dissent quote"
    assert source["position"] != output["position"], "dissent must preserve an opposing position"
    prose(dissent["response"])


def observer(root: Path) -> None:
    raw = root / "raw-log.jsonl"
    source = [json.loads(line) for line in raw.read_text().splitlines()]
    expected = {row["id"]: row["text"] for row in source if row["critical"]}
    rows = unique(read(root, "brief.json"))
    assert {key: row["quote"] for key, row in rows.items()} == expected, "lost or altered incident"
    assert (root / "brief.json").stat().st_size * 5 < raw.stat().st_size, "no compression benefit"


def operator(root: Path) -> None:
    observer(root)
    actions = unique(read(root, "actions.json"))
    assert set(actions) == set(unique(read(root, "brief.json"))), "unhandled incident"
    for row in actions.values():
        prose(row["action"])
    write(
        root,
        "economy.json",
        {
            "raw_bytes": (root / "raw-log.jsonl").stat().st_size,
            "brief_bytes": (root / "brief.json").stat().st_size,
            "measure": "input bytes; not measured model tokens or provider cost",
        },
    )


def signal(root: Path, voice: int) -> None:
    row = read(root, f"signal-{voice}.json")
    task = read(root, f"task-{voice}.json")
    assert row["owner"] == voice and row["fact"] == task["finding"], "wrong signal owner or finding"


def result(root: Path, voice: int) -> None:
    peer = 3 - voice
    signal(root, voice)
    signal(root, peer)
    row = read(root, f"result-{voice}.json")
    assert row["owner"] == voice and row["peer"] == peer
    assert row["signal_sha256"] == sha(root / f"signal-{peer}.json"), "stale peer signal"
    assert row["adopted_fact"] == read(root, f"signal-{peer}.json")["fact"], (
        "peer finding not adopted"
    )
    prose(row["proposal"])


def workspace(root: Path) -> None:
    result(root, 1)
    result(root, 2)


def aar_review(root: Path) -> None:
    cases, baseline = read(root, "cases.json"), read(root, "run-1.json")
    missed = {key for key, value in cases.items() if baseline[key] != value.strip().casefold()}
    row = read(root, "aar.json")
    assert set(row["actual"]) == missed and set(row["evidence"]) == missed, (
        "review lacks concrete deltas"
    )
    for field in ("intended", "cause", "sustain", "improve"):
        prose(row[field])
    assert row["rule"] == "strip-casefold", (
        "learning does not address observed case normalization gap"
    )


def aar_memory(root: Path) -> None:
    # Writer, not a pure checker: validates the review, then persists memory.json
    # (rule + evidence + review hash) as this score's deterministic stage-3 output.
    aar_review(root)
    row = read(root, "aar.json")
    write(
        root,
        "memory.json",
        {"rule": row["rule"], "evidence": row["evidence"], "review_sha256": sha(root / "aar.json")},
    )


def aar_run(root: Path) -> None:
    aar_review(root)
    memory, output = read(root, "memory.json"), read(root, "run-2.json")
    assert memory["review_sha256"] == sha(root / "aar.json"), "memory refers to another review"
    assert memory["rule"] == "strip-casefold"
    assert output["memory_sha256"] == sha(root / "memory.json"), (
        "second run did not bind its learning"
    )
    expected = {key: value.strip().casefold() for key, value in read(root, "cases.json").items()}
    assert output["results"] == expected, "second run did not correct the measured failures"
    assert output["results"] != read(root, "run-1.json"), "no learning effect"


def screen(root: Path, tier: int) -> None:
    # Evidence is progressively disclosed: difficulty is discovered while solving,
    # never provided as a preassigned severity/complexity label on the questions.
    expected = set(read(root, "questions.json"))
    if tier > 1:
        screen(root, tier - 1)
        expected = {
            row["id"]
            for row in read(root, f"screen-{tier - 1}.json")
            if row["status"] == "escalate"
        }
    rows = unique(read(root, f"screen-{tier}.json"))
    assert set(rows) == expected, "dropped item or reprocessing of an already solved item"
    answers = {"a": 5, "b": 12, "c": 10, "d": 0}
    available = {1: {"a", "b"}, 2: {"c"}, 3: {"d"}}[tier]
    for key, row in rows.items():
        if key in available:
            assert row["status"] == "solved" and row["answer"] == answers[key], (
                "wrong or needless escalation"
            )
        else:
            assert row["status"] == "escalate", "answer lacks required evidence at this tier"
            prose(row["reason"])
    if tier == 1:
        # A first screen that escalates most items is not screening.
        assert sum(row["status"] == "escalate" for row in rows.values()) <= len(rows) / 2


def cascade(root: Path) -> None:
    screen(root, 3)
    solved = [
        r["id"]
        for tier in (1, 2, 3)
        for r in read(root, f"screen-{tier}.json")
        if r["status"] == "solved"
    ]
    assert sorted(solved) == sorted(read(root, "questions.json")), "items not conserved"
    write(root, "routing.json", {"tier_inputs": [4, 2, 1], "solved_once": sorted(solved)})


def main() -> int:
    mode, root = sys.argv[1], Path(sys.argv[2])
    gates = {
        "init": initialize,
        "page-first": page_first,
        "page-second": page_second,
        "page": page,
        "weave": weave,
        "observer": observer,
        "operator": operator,
        "workspace": workspace,
        "aar-review": aar_review,
        "aar-memory": aar_memory,
        "aar-run": aar_run,
        "cascade": cascade,
    }
    try:
        if mode in {"signal", "result", "screen"}:
            {"signal": signal, "result": result, "screen": screen}[mode](root, int(sys.argv[3]))
        else:
            gates[mode](root)
    except (AssertionError, KeyError, ValueError, TypeError, OSError) as exc:
        print(f"FAIL {mode}: {exc}", file=sys.stderr)
        return 1
    print(f"PASS {mode}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
