from __future__ import annotations

import re


REGEX_LINE = re.compile(r'^\s*(.*?)\s*(?://.*)?$', re.MULTILINE)
REGEX_ADDRESS = re.compile(r'^([a-zA-Z]+):$')
REGEX_ASSIGNMENT = re.compile()


Namespace = dict[str, int]
Lines = list[str]
Stepthrough = list[tuple[int, Namespace]]


def process_lines(source: str) -> Lines:
    return [m[1] for m in REGEX_LINE.finditer(source)]


def get_addresses(lines: list[str]) -> Namespace:
    addresses = {}

    for index, l in enumerate(lines):
        match = REGEX_ADDRESS.match(l)
        if match is not None:
            addresses[match[1].lower()] = index

    return addresses


def execute_lines(lines: list[str]) -> Stepthrough:
    stepthrough = []
    variables = {}
    instruction = 0
    instruction_max = len(lines)
    addresses = get_addresses(lines)

    while True:
        if instruction >= instruction_max:
            break

    return stepthrough
