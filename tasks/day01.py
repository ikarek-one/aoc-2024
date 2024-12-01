def main():
    test_filepath = "resources/test-inputs/test01.txt"
    input_filepath = "resources/inputs/input01.txt"

    print("part one (test):", partOne(test_filepath))  # 11
    print("part one (real input):", partOne(input_filepath))  # 3508942
    print("part two (test):", partTwo(test_filepath))  # 31
    print("part two (real input):", partTwo(input_filepath))  # 26593248


def partOne(filepath):
    (list1, list2) = parse_input(filepath)
    list1.sort()
    list2.sort()
    assert len(list1) == len(list2)
    return sum(map(lambda x1, x2: abs(x1 - x2), list1, list2))


def partTwo(filepath):
    (list1, list2) = parse_input(filepath)
    assert len(list1) == len(list2)

    freq = {}
    for i in range(len(list1)):
        num = list2[i]
        freq[num] = freq.get(num, 0) + 1

    result = 0
    for id in list1:
        result += id * freq.get(id, 0)
    return result


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
