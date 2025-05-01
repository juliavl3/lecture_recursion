import os
import json

cwd_path = os.getcwd()
file_path = "files"


def read_data(file_name, key="ordered_numbers"):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, str), sequential data
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(os.path.join(cwd_path, file_path, file_name), mode="r") as json_file:
        seqs = json.load(json_file)

    return seqs[key]


def binary_search(seq, number):
    """
    Function performs binary search on !!ordered!! sequence and stores position of match if found.
    :param seq: (list): list of numbers
    :param number: (int): number to match within sequence
    :return: (int, None): index of match if found, None otherwise
    """
    left, right = (0, len(seq) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return middle
    return None

def recursive_binary_search(sequence, number, left, right):

    # if number in sequence:
    #     left = sequence[0]
    #     right = sequence[-1]
    #     nb_vals = len(sequence)
    #     if nb_vals <= 1:
    #         return 0
    #     middle = sequence[nb_vals // 2]
    #     if middle == number or left == number or right == number:
    #         idx = sequence.index(number)
    #         return idx
    #     if middle < number:
    #         return recursive_binary_search(sequence[len(sequence) // 2:],number,left,right)
    #     if middle > number:
    #         return recursive_binary_search(sequence[:len(sequence) // 2],number,left,right)
    # else:
    #     return None

    while left > right:
        return  None

    middle = (right + left) // 2

    while left <= right:

        if number < sequence[middle]:
            return recursive_binary_search(sequence, number, left,  middle - 1)
        elif number > sequence[middle]:
            return recursive_binary_search(sequence, number, middle + 1, right)
        else:
            return middle
    return None
    # asymptoticka zlozitost je O(log*n) - vyhoda

def main(file_name, number):
    sequence = read_data(file_name=file_name, key="ordered_numbers")
    print(sequence)
    # iterative binary search
    left = 0
    right = len(sequence) - 1
    print(binary_search(sequence, number=my_number))
    print(recursive_binary_search(sequence,my_number,left, right))

if __name__ == "__main__":
    my_file = "sequential.json"
    my_number = 90
    main(my_file, my_number)
