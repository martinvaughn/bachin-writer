import os, os.path
import svg_stack as ss
from random import randint
import sys

def choose_number(count):
    ## return number between 1 and count
    return randint(1, count)

def get_random_number(path):
    count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    return choose_number(count)# get the count of items within the path.

def get_folder(char: str, idx: int):
    if char.islower():
        _path = "svgs/lower/lower_" + char
        num = get_random_number(_path)
        return ("char", _path + "/lower_" + char + "_" + str(num) + ".svg", idx)
    if char.isupper():
        _path = "svgs/upper/upper_" + char.lower()
        num = get_random_number(_path)
        return ("char", _path + "/upper_" + char.lower() + "_" + str(num) + ".svg", idx)
    #### Individual Checks
    # old..
    #if char == " ":
    #    return ("space", "svgs/blank_template_7_x_10.svg", idx)
    if char == " ":
        _path = "svgs/spaces"
        num = get_random_number(_path)
        return ("space", "svgs/blank_template_" + str(num) + ".svg", idx)
        
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
    if char == "@":
        _path = "svgs/special_characters/at_symbol"
        num = get_random_number(_path)
        return ("char", _path + "/at_symbol_"  + str(num) + ".svg", idx)
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
    # 3
    if char == "4":
        _path = "svgs/numbers/number_four"
        num = get_random_number(_path)
        return ("char", _path + "/number_four_"  + str(num) + ".svg", idx)
    # 5-7
    if char == "8":
        _path = "svgs/numbers/number_eight"
        num = get_random_number(_path)
        return ("char", _path + "/number_eight_"  + str(num) + ".svg", idx)
    if char == "9":
        _path = "svgs/numbers/number_nine"
        num = get_random_number(_path)
        return ("char", _path + "/number_nine_"  + str(num) + ".svg", idx)


def main():
    doc = ss.Document()
    if len(sys.argv) == 1:
        print("ERROR: Please provide an input string")
        return 
    input_str = sys.argv[1]
    ftuples = []
    for idx, char in enumerate(input_str):
        folder_tuple = get_folder(char, idx)
        # print(folder_tuple)
        ftuples.append(folder_tuple)
 
    result_layout = ss.VBoxLayout()
    yes = True
    while yes == True:
        i = 0
        word = []
        line_layout = ss.HBoxLayout()
        while i < len(ftuples):
            if ftuples[i][0] == "new_line":
                result_layout.addLayout(line_layout)
                line_layout = ss.HBoxLayout()
                
            if line_layout.get_size().width > 580: 
                result_layout.addLayout(line_layout)
                line_layout = ss.HBoxLayout()
                i -= 1
            elif ftuples[i] == ftuples[-1]: 
                word_layout = ss.HBoxLayout()
                word.append(ftuples[i][1])
                for file in word:
                    word_layout.addSVG(file,alignment=ss.AlignLeft)
                line_layout.addLayout(word_layout)
                yes = False
            elif ftuples[i][0] == 'space':
                word_layout = ss.HBoxLayout()
                word.append(ftuples[i][1])
                for file in word:
                    word_layout.addSVG(file,alignment=ss.AlignCenter)
                line_layout.addLayout(word_layout)
                word = []
            elif ftuples[i][0] == "char":
                word.append(ftuples[i][1])
            i += 1

    result_layout.addLayout(line_layout)  
    doc.setLayout(result_layout)
    doc.save('generated.svg')
    
if __name__ == "__main__": main()
