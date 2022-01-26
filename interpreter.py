"""Simple assembly interpreter.

Designed for the Very Very Reduced Instruction Set language specified in xmas quizzz.
File to run specified by SOURCE_FILE, haven't bothered to add an argparser.
Sorry for python 3, python 2 is too expensive
"""

from __future__ import annotations
import re


SOURCE_FILE = 'ADDER.asm'


REGEX_LINE = re.compile(r'^\s*(.*?)\s*(?://.*)?$', re.MULTILINE)
REGEX_ADDRESS = re.compile(r'^([A-Z][a-z]*):$')
REGEX_ASSIGNMENT = re.compile(r'^([A-Z]+) = ([A-Z]+|[0-9]+)$')
REGEX_JUMP = re.compile(r'^JPZ ([a-z]+)$')
REGEX_OPERATION = re.compile(r'^(AND|XOR) ([A-Z]+|[0-9]+) ([A-Z]+|[0-9]+)$')
PRINT_SEP = '  '
PRINT_UNDERLINE = '-'
PRINT_BINARY_FORMAT = '{:0>8b}'


Namespace = dict[str, int]
Lines = list[str]
Stepthrough = list[tuple[int, str, Namespace]]


def process_lines(source: str) -> Lines:
    return [m[1] for m in REGEX_LINE.finditer(source) if m[1]]


def get_addresses(lines: list[str]) -> Namespace:
    addresses = {}

    for index, l in enumerate(lines):
        match = REGEX_ADDRESS.match(l)
        if match is not None:
            addresses[match[1].lower()] = index

    return addresses


def extract_arg(arg: str, variables: Namespace) -> int:
    if arg.isdigit():
        return int(arg)
    else:
        return variables[arg]


def update_stepthrough(stepthrough: Stepthrough, instruction: int, line: str, variables: Namespace):
    new_step = (instruction, line, variables.copy())
    stepthrough.append(new_step)


def execute_lines(lines: list[str]) -> Stepthrough:
    stepthrough = []
    variables = {}
    last_calculation = 0
    instruction = 0
    instruction_max = len(lines)
    addresses = get_addresses(lines)

    # the duplicated loop continuation blocks are a bit nasty
    while True:
        # end of file
        if instruction >= instruction_max:
            break

        l = lines[instruction]

        # address declarations are skipped
        if instruction in addresses.values():
            update_stepthrough(stepthrough, instruction, l, variables)
            instruction += 1
            continue

        # assignment
        match = REGEX_ASSIGNMENT.match(l)
        if match is not None:
            name = match[1]
            assignee = match[2]
            assignee_ex = extract_arg(assignee, variables)
            variables[name] = assignee_ex
            update_stepthrough(stepthrough, instruction, l, variables)
            instruction += 1
            continue

        # jump
        match = REGEX_JUMP.match(l)
        if match is not None:
            update_stepthrough(stepthrough, instruction, l, variables)
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
            arg_right = match[3]
            arg_left_ex = extract_arg(arg_left, variables)
            arg_right_ex = extract_arg(arg_right, variables)
            op = match[1]
            if op == 'AND':
                last_calculation = arg_left_ex & arg_right_ex
            elif op == 'XOR':
                last_calculation = arg_left_ex ^ arg_right_ex
            if not arg_left.isdigit():  # left arg is a name not a literal
                variables[arg_left] = last_calculation
            update_stepthrough(stepthrough, instruction, l, variables)
            instruction += 1
            continue

        raise ValueError(f'Invalid instruction: "{l}".')

    return stepthrough


def print_stepthrough(stepthrough: Stepthrough) -> str:
    final_variables = stepthrough[-1][2]

    column_headers = ['Instruction', 'Line', *final_variables.keys()]
    column_contents = []
    column_contents.append([str(s[0]) for s in stepthrough])
    column_contents.append([s[1] for s in stepthrough])
    for v in final_variables:
        variable_column = []
        for s in stepthrough:
            value = s[2].get(v)
            if value is None:
                variable_column.append('')
            else:
                variable_column.append(PRINT_BINARY_FORMAT.format(value))
        column_contents.append(variable_column)

    column_widths_headless = [max(len(x) for x in column) for column in column_contents]
    column_widths = [max(len(head), max_value) for head, max_value in zip(column_headers, column_widths_headless)]
    # pad instruction counter
    ic_fstring = f'{{:>{column_widths_headless[0]}}}'
    column_contents[0] = [ic_fstring.format(ic) for ic in column_contents[0]]

    table_lines = []

    header = PRINT_SEP.join(value.ljust(width) for value, width in zip(column_headers, column_widths))
    table_lines.append(header)
    underline = PRINT_UNDERLINE * len(header)
    table_lines.append(underline)
    for i in range(len(stepthrough)):
        row_list = [c[i] for c in column_contents]
        row = PRINT_SEP.join(str(value).ljust(width) for value, width in zip(row_list, column_widths))
        table_lines.append(row)

    return '\n'.join(table_lines)


def main():
    with open(SOURCE_FILE, encoding='utf-8') as file:
        source = file.read()
    lines = process_lines(source)
    stepthrough = execute_lines(lines)
    table = print_stepthrough(stepthrough)
    print(table)


if __name__ == '__main__':
    main()
