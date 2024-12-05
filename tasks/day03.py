import re


def day_three():
    test_filepath = "resources/test-inputs/test03.txt"
    input_filepath = "resources/inputs/input03.txt"

    test_pt1 = part_one(test_filepath)
    input_pt1 = part_one(input_filepath)
    test_pt2 = part_two(test_filepath)
    input_pt2 = part_two(input_filepath)

    print("part one (test):", test_pt1)  # 161
    print("part one (real input):", input_pt1)  # 173529487
    # print("part two (test):", test_pt2)  # 48 but the test case is different than in pt 1, so it'll be wrong
    print("part two (real input):", input_pt2)  # 99532691


def part_one(filepath):
    with open(filepath) as file:
        text = file.read()
    my_regex = r"mul\([0-9]{1,3}\,[0-9]{1,3}\)"
    search_results = re.findall(my_regex, text)
    sum = 0
    for sr in search_results:
        mul_tokens = re.split("[^0-9]+", sr)
        (a, b) = map(int, filter(str.isnumeric, mul_tokens))
        sum += a * b
    return sum


def part_two(filepath):
    with open(filepath) as file:
        text = file.read()
    my_regex = r"do\(\)|don't\(\)|mul\([0-9]{1,3}\,[0-9]{1,3}\)"
    # part two test case
    # text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    search_results = re.findall(my_regex, text)
    sum = 0
    do_flag = True
    for sr in search_results:
        if (sr == "do()"):
            do_flag = True
            continue
        elif (sr == "don't()"):
            do_flag = False
            continue
        elif (not do_flag):
            continue

        mul_tokens = re.split("[^0-9]+", sr)
        (a, b) = map(int, filter(str.isnumeric, mul_tokens))
        sum += a * b
    return sum
