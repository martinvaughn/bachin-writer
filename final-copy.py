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
    if char == " ":
        return ("space", "svgs/blank_template_4_x_10.svg", idx)
 
    # then individual items for punctuation. 


def main():
    doc = ss.Document()
    input_str = "a aa"
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
            if ftuples[i][0] == "new line":
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
