from __future__ import annotations

import re
from copy import copy


REGEX_LINE = re.compile(r'^\s*(.*?)\s*(?://.*)?$', re.MULTILINE)
REGEX_ADDRESS = re.compile(r'^([A-Z][a-z]*):$')
REGEX_ASSIGNMENT = re.compile(r'^([A-Z]+) = ((?P<name>[A-Z]+)|(?P<int>[0-9]+))$')
REGEX_JUMP = re.compile(r'^JPZ ([a-z]+)$')
REGEX_OPERATION = re.compile(r'^(AND|XOR)$')


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
        # end of file
        if instruction >= instruction_max:
            break

        # address declarations are skipped
        if instruction in addresses.values():
            instruction += 1
            continue

        l = lines[instruction]

        # assignment
        match = REGEX_ASSIGNMENT.match(l)
        if match is not None:
            name = match[1]
            try:
                assign_name = match['name']
            except IndexError:
                assign_int = match['int']
                variables[name] = int(assign_int)
            else:
                variables[name] = variables[assign_name]
            instruction += 1
            continue

        # jump
        match = REGEX_JUMP.match(l)
        if match is not None:
            jump_address = match[1]
            instruction = addresses[jump_address]
            continue

    return stepthrough
