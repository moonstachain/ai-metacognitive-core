#!/usr/bin/env python3
"""Helper entrypoint for ai-metacognitive-core."""

from __future__ import annotations

import argparse


EIGHT_QUESTIONS = [
    "Is my model of the user's goal real, or only a surface reading?",
    "Is this path globally better, or merely locally comfortable?",
    "What reusable skills, scripts, APIs, tools, or auth do I already have?",
    "What is my highest-risk misread right now?",
    "What evidence would prove I am not pseudo-complete?",
    "What boundary truly requires the human, and what does not?",
    "What from this run deserves to remain, and what must be forgotten?",
    "If I keep going now, is that actually better, or am I just unable to stop?",
]

SITUATION_MAP = [
    "自治判断",
    "全局最优判断",
    "能力复用判断",
    "验真判断",
    "进化判断",
    "当前最大失真",
]


def print_summary() -> None:
    print("ai-metacognitive-core")
    print()
    print("Meta constitution:")
    print("1. 极克制的人类介入")
    print("2. 面向全局最优的平衡")
    print("3. 默认先盘点既有能力")
    print("4. 任务后递归自进化")
    print()
    print("Four-need situation map:")
    for item in SITUATION_MAP:
        print(f"- {item}")
    print()
    print("Eight-question discipline:")
    for index, question in enumerate(EIGHT_QUESTIONS, start=1):
        print(f"{index}. {question}")


def print_template() -> None:
    print("# AI 元认知 Situation Map")
    print()
    for item in SITUATION_MAP:
        print(f"- `{item}`: ")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Local helper for the ai-metacognitive-core skill."
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="print a blank situation-map template",
    )
    args = parser.parse_args()

    if args.template:
        print_template()
        return

    print_summary()


if __name__ == "__main__":
    main()
