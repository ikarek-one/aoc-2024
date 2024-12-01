def main():
    test_filepath = "resources/test-inputs/test01.txt"
    input_filepath = "resources/inputs/input01.txt"

    print("part one (test):", part_one(test_filepath))  # 11
    print("part one (real input):", part_one(input_filepath))  # 3508942
    print("part two (test):", part_two(test_filepath))  # 31
    print("part two (real input):", part_two(input_filepath))  # 26593248


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
