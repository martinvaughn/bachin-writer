import os, os.path
import svg_stack as ss
from random import randint

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
        _path = "svgs/upper/upper_" + char
        num = get_random_number(_path)
        return ("char", _path + "/upper_" + char + "_" + str(num) + ".svg", idx)
    #### Individual Checks
    if char == " ":
        return ("space", "svgs/blank_template_7_x_10.svg", idx)
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
    input_str = "hello my name's what my name's who my name is slim shaddy. ~Please keep all hands and feet in the boat at all times and do not lose your balance because there are certainly sharks and sharks are not your friend no matter how cute you think they are, remember that all they see is a delicious human sived snack. don't @ me tho ~new line added here. 12 04 89~112244008899"
    ftuples = []
    for idx, char in enumerate(input_str):
        folder_tuple = get_folder(char, idx)
        print(folder_tuple)
        ftuples.append(folder_tuple)

    ftuples2 = [
            ("char","svgs/lower/lower_h/lower_h_1.svg",1), 
            ("char","svgs/lower/lower_i/lower_i_1.svg",2), 
            ("space","svgs/blank_template.svg",3),
            ("char","svgs/lower/lower_s/lower_s_1.svg",4),
            ("char","svgs/lower/lower_o/lower_o_1.svg",5), 
            ("char","svgs/lower/lower_s/lower_s_1.svg",6),
            ("char","svgs/lower/lower_s/lower_s_1.svg",7), 
            ("space","svgs/blank_template.svg",8),
            # ("new line", 1),
            ("char","svgs/lower/lower_m/lower_m_1.svg",9),
            ("char","svgs/lower/lower_o/lower_o_1.svg",10),
            ("char","svgs/lower/lower_o/lower_o_1.svg",11),
            ("char","svgs/lower/lower_n/lower_n_1.svg",12),
            ("space","svgs/blank_template.svg",88),
            ("char","svgs/lower/lower_s/lower_s_1.svg",13),
            ("char","svgs/lower/lower_n/lower_n_1.svg",14),
            ("char","svgs/lower/lower_o/lower_o_1.svg",15),
            ("char","svgs/lower/lower_s/lower_s_1.svg",16),
            ("space","svgs/blank_template.svg",90),
            ("char","svgs/lower/lower_s/lower_s_1.svg",17),
            ("char","svgs/lower/lower_s/lower_s_1.svg",18),
            ("char","svgs/lower/lower_s/lower_s_1.svg",19),
            ("char","svgs/lower/lower_s/lower_s_1.svg",20),
            ("char","svgs/lower/lower_s/lower_s_1.svg",21),
            ("char","svgs/lower/lower_s/lower_s_1.svg",22),
            ("char","svgs/lower/lower_s/lower_s_1.svg",23),
            ("char","svgs/lower/lower_s/lower_s_1.svg",24),
            ("char","svgs/lower/lower_s/lower_s_1.svg",25),
            ("char","svgs/lower/lower_s/lower_s_1.svg",26),
            ("char","svgs/lower/lower_s/lower_s_1.svg",27),
            ("new line","svgs/blank_template.svg",28),
            ("space","svgs/blank_template.svg",36),
            ("char","svgs/lower/lower_h/lower_h_1.svg",29), 
            ("char","svgs/lower/lower_i/lower_i_1.svg",30), 
            ("space","svgs/blank_template.svg",37),
            ("char","svgs/lower/lower_s/lower_s_1.svg",31),
            ("char","svgs/lower/lower_o/lower_o_1.svg",32), 
            ("char","svgs/lower/lower_s/lower_s_1.svg",33),
            ("char","svgs/lower/lower_s/lower_s_1.svg",34), 
            ("space","svgs/blank_template.svg",84),
            ("char","svgs/lower/lower_m/lower_m_1.svg",35),
            ("char","svgs/lower/lower_o/lower_o_1.svg",36),
            ("char","svgs/lower/lower_o/lower_o_1.svg",38),
            ("char","svgs/lower/lower_n/lower_n_1.svg",39),
            ("space","svgs/blank_template.svg",89),
            ("char","svgs/lower/lower_s/lower_s_1.svg",40),
            ("char","svgs/lower/lower_n/lower_n_1.svg",41),
            ("char","svgs/lower/lower_o/lower_o_1.svg",42),
            ("char","svgs/lower/lower_s/lower_s_1.svg",43),
            ("space","svgs/blank_template.svg",85),
            ("char","svgs/lower/lower_s/lower_s_1.svg",44),
            ("char","svgs/lower/lower_s/lower_s_1.svg",45),
            ("char","svgs/lower/lower_s/lower_s_1.svg",46),
            ("char","svgs/lower/lower_s/lower_s_1.svg",47),
            ("char","svgs/lower/lower_s/lower_s_1.svg",48),
            ("char","svgs/lower/lower_s/lower_s_1.svg",49),
            ("char","svgs/lower/lower_s/lower_s_1.svg",50),
            ("char","svgs/lower/lower_s/lower_s_1.svg",51),
            ("char","svgs/lower/lower_s/lower_s_1.svg",52),
            ("char","svgs/lower/lower_s/lower_s_1.svg",53),
            ("char","svgs/lower/lower_s/lower_s_1.svg",54),
            ("space","svgs/blank_template.svg",101),
            ("char","svgs/lower/lower_s/lower_s_1.svg",55),
            ("char","svgs/lower/lower_n/lower_n_1.svg",56),
            ("char","svgs/lower/lower_o/lower_o_1.svg",57),
            ("char","svgs/lower/lower_s/lower_s_1.svg",58),
            ]
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
                
            if line_layout.get_size().width > 556: 
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
