import day01

day_results = [day01.day_one()]

template = "Advent of Code 2024 - finished tasks so far:\n\nDay No | part one | part two\n"
legend = "Legend: ★ - not finished, ✰ - finished"
readme_path = "README.md"


def generate_readme():
    day_results.sort(reverse=True)
    output = template
    stars = 0
    for day in day_results:
        day_number = str(day.day_id)
        pt_one = "✰" if day.part_one_res else "★"
        pt_two = "✰" if day.part_two_res else "★"
        line = f"{day_number.rjust(2, '0')}     |     {pt_one}   |     {pt_two}\n"
        output += line
        if (day.part_one_res):
            stars += 1
        if (day.part_two_res):
            stars += 1
    output += legend
    output += f"\nI have already received {stars} stars!"
    print("\n" + output)

    with open(readme_path, 'w', encoding="utf-8") as file:
        file.write(output)
