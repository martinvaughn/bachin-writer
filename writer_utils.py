from random import randint
import os, os.path

def choose_number(count):
    ## return number between 1 and count
    return randint(1, count)

def get_random_number(path):
    count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    return choose_number(count)# get the count of items within the path.

def get_folder(char: str, idx: int):

    # Upper & Lower
    if char.islower():
        _path = "svgs/lower/lower_" + char
        num = get_random_number(_path)
        return ("char", _path + "/lower_" + char + "_" + str(num) + ".svg", idx)
    if char.isupper():
        _path = "svgs/upper/upper_" + char.lower()
        num = get_random_number(_path)
        return ("char", _path + "/upper_" + char.lower() + "_" + str(num) + ".svg", idx)
    # Spaces    
    if char == " ":
        _path = "svgs/spaces"
        num = get_random_number(_path)
        return ("space", "svgs/spaces/blank_template_" + str(num) + ".svg", idx)
    if char == "£":
        _path = "svgs/mini_spaces"
        num = get_random_number(_path)
        return ("mini_space", "svgs/mini_spaces/blank_template_" + str(num) + ".svg", idx)
        
    # Punctuation
    if char == ",":
        _path = "svgs/punctuation/comma"
        num = get_random_number(_path)
        return ("char", _path + "/comma_"  + str(num) + ".svg", idx)
    if char == ".":
        _path = "svgs/punctuation/dot_period"
        num = get_random_number(_path)
        return ("char", _path + "/dot_"  + str(num) + ".svg", idx)
    if char == "'":
        _path = "svgs/punctuation/apostrophe"
        num = get_random_number(_path)
        return ("char", _path + "/apostrophe_"  + str(num) + ".svg", idx)

    # Special Characters
    if char == "@":
        _path = "svgs/special_characters/at_symbol"
        num = get_random_number(_path)
        return ("char", _path + "/at_symbol_"  + str(num) + ".svg", idx)
    if char == "#":
        _path = "svgs/special_characters/hashtag"
        num = get_random_number(_path)
        return ("char", _path + "/hashtag_"  + str(num) + ".svg", idx)
    if char == "-":
        _path = "svgs/special_characters/hyphen"
        num = get_random_number(_path)
        return ("char", _path + "/hyphen_"  + str(num) + ".svg", idx)
    if char == "~":
        return ("new_line", idx)

    ### Numbers
    if char == "0":
        _path = "svgs/numbers/number_zero"
        num = get_random_number(_path)
        return ("char", _path + "/number_zero_"  + str(num) + ".svg", idx)
    if char == "1":
        _path = "svgs/numbers/number_one"
        num = get_random_number(_path)
        return ("char", _path + "/number_one_"  + str(num) + ".svg", idx)
    if char == "2":
        _path = "svgs/numbers/number_two"
        num = get_random_number(_path)
        return ("char", _path + "/number_two_"  + str(num) + ".svg", idx)
    if char == "3":
        _path = "svgs/numbers/number_three"
        num = get_random_number(_path)
        return ("char", _path + "/number_three_"  + str(num) + ".svg", idx)
    if char == "4":
        _path = "svgs/numbers/number_four"
        num = get_random_number(_path)
        return ("char", _path + "/number_four_"  + str(num) + ".svg", idx)
    if char == "5":
        _path = "svgs/numbers/number_five"
        num = get_random_number(_path)
        return ("char", _path + "/number_five_"  + str(num) + ".svg", idx)
    if char == "6":
        _path = "svgs/numbers/number_six"
        num = get_random_number(_path)
        return ("char", _path + "/number_six_"  + str(num) + ".svg", idx)
    if char == "7":
        _path = "svgs/numbers/number_seven"
        num = get_random_number(_path)
        return ("char", _path + "/number_seven_"  + str(num) + ".svg", idx)
    if char == "8":
        _path = "svgs/numbers/number_eight"
        num = get_random_number(_path)
        return ("char", _path + "/number_eight_"  + str(num) + ".svg", idx)
    if char == "9":
        _path = "svgs/numbers/number_nine"
        num = get_random_number(_path)
        return ("char", _path + "/number_nine_"  + str(num) + ".svg", idx)
