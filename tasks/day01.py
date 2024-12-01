from utils.Results import TestingResults
def day_one():
    test_filepath = "resources/test-inputs/test01.txt"
    input_filepath = "resources/inputs/input01.txt"

    test_pt1 = part_one(test_filepath)
    input_pt1 = part_one(input_filepath)
    test_pt2 = part_two(test_filepath)
    input_pt2 = part_two(input_filepath)

    print("part one (test):", test_pt1)  # 11
    print("part one (real input):", input_pt1)  # 3508942
    print("part two (test):", test_pt2)  # 31
    print("part two (real input):", input_pt2)  # 26593248

    return TestingResults(1, (input_pt1 == 3508942), (input_pt2 == 26593248))



def part_one(filepath):
    (list1, list2) = parse_input(filepath)
    list1.sort()
    list2.sort()
    return sum(map(lambda x1, x2: abs(x1 - x2), list1, list2))


def part_two(filepath):
    (list1, list2) = parse_input(filepath)

    freq = {}
    for num in list2:
        freq[num] = freq.get(num, 0) + 1

    result_score = 0
    for id in list1:
        result_score += id * freq.get(id, 0)
    return result_score


def parse_input(filepath):
    with open(filepath) as file:
        list1 = []
        list2 = []
        for row in file:
            texts = row.split()
            ints = list(map(int, texts))
            list1.append(ints[0])
            list2.append(ints[1])
    return (list1, list2)
