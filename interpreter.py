from __future__ import annotations

import re
from copy import copy


REGEX_LINE = re.compile(r'^\s*(.*?)\s*(?://.*)?$', re.MULTILINE)
REGEX_ADDRESS = re.compile(r'^([A-Z][a-z]*):$')
REGEX_ASSIGNMENT = re.compile(r'^([A-Z]+) = ([A-Z]+|[0-9]+)$')
REGEX_JUMP = re.compile(r'^JPZ ([a-z]+)$')
REGEX_OPERATION = re.compile(r'^(AND|XOR) ([A-Z]+|[0-9]+) ([A-Z]+|[0-9]+)$')


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


def extract_argument(arg: str, variables: Namespace) -> int:
    if arg


def execute_lines(lines: list[str]) -> Stepthrough:
    stepthrough = []
    variables = {}
    last_calculation = 0
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
            assignee = match[2]
            if assignee.isdigit():
                variables[name] = int(assignee)
            else:
                variables[name] = variables[assignee]
            instruction += 1
            continue

        # jump
        match = REGEX_JUMP.match(l)
        if match is not None:
            if last_calculation == 0:
                jump_address = match[1]
                instruction = addresses[jump_address]
            else:
                instruction += 1
            continue

        # and, xor
        match = REGEX_OPERATION.match(l)
        if match is not None:
            arg_left = match[2]
            if arg_left.isdigit():
            arg_right = match[3]
            op = match[1]
            # if op == 'AND':
            #     last_calculation =


    return stepthrough
