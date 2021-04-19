import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    return data[field]


def linear_search(sequence, searched_number):
    """
    :param sequence: (list)
    :param searched_number: (int)
    :return: (dict)
    """

    count = 0
    positions = []
    for i, number in enumerate(sequence):
        if number == searched_number:
            count = count + 1
            positions.append(i)

    return {"positions": positions, "count": count}


def pattern_search(dna_sequence, codon):
    positions = set()
    i = 0
    while i < len(dna_sequence) - len(codon):
        idx = 0
        while idx < len(codon):
            if dna_sequence[i + idx] == codon[idx]:
                idx = idx + 1
            else:
                break
        else:
            positions.add(i)
        i = i + 1
    return positions


def binary_search(sequence, searched_number):
    left = 0
    right = len(sequence) - 1
    middle = right // 2
    while right >= left:
        if sequence[middle] == searched_number:
            return middle
        elif sequence[middle] < searched_number:
            left = middle + 1
            middle = (left + right) // 2
        elif sequence[middle] > searched_number:
            right = middle - 1
            middle = (left + right) // 2
    return None


def main():
    sequential_data = read_data("sequential.json", "dna_sequence")
    codon_positions = pattern_search(sequential_data, "ATA")
    print(codon_positions)
    sequential_data = read_data("sequential.json", "unordered_numbers")
    search_number = 5
    results = linear_search(sequential_data, search_number)
    print(results)
    ordered_numbers = read_data("sequential.json", "ordered_numbers")
    results = binary_search(ordered_numbers, 0)
    print(results)


if __name__ == '__main__':
    main()
