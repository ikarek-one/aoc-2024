import copy

import numpy as np

from utils.Results import TestingResults


def day_two():
    test_filepath = "resources/test-inputs/test02.txt"
    input_filepath = "resources/inputs/input02.txt"

    test_pt1 = part_one(test_filepath)
    input_pt1 = part_one(input_filepath)
    test_pt2 = part_two(test_filepath)
    input_pt2 = part_two(input_filepath)

    print("part one (test):", test_pt1)  # 2
    print("part one (real input):", input_pt1)  # 510
    print("part two (test):", test_pt2)  # 4
    print("part two (real input):", input_pt2)  # 553

    return TestingResults(2, input_pt1 == 510, input_pt2 == 553)


def part_one(filepath):
    reports = parse_input(filepath)
    return sum(map(lambda report: (1 if (is_report_safe(report)) else 0), reports))


def is_report_safe(report):
    diffs = np.diff(np.array(report))
    return all(map(lambda lvl: -3 <= lvl <= -1, diffs)) or all(map(lambda lvl: 1 <= lvl <= 3, diffs))


def part_two(filepath):
    reports = parse_input(filepath)
    return sum(map(lambda report: (1 if (is_report_safe_dampened(report)) else 0), reports))


def is_report_safe_dampened(report):
    for i in range(len(report)):
        report_without_ith = copy.copy(report)
        report_without_ith.pop(i)
        if (is_report_safe(report_without_ith)):
            return True
    return False


def parse_input(filepath):
    with open(filepath) as file:
        reports = []
        for row in file:
            levels = list(map(int, row.split()))
            reports.append(levels)
    return reports
