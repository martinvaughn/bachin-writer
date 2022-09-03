import svg_stack as ss
import sys
import writer_utils as writer_utils

def main():
    doc = ss.Document()
    if len(sys.argv) == 1:
        print("ERROR: Please provide an input string")
        return 
    input_str = sys.argv[1]
    ftuples = []
    for idx, char in enumerate(input_str):
        folder_tuple = writer_utils.get_folder(char, idx)
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
                if ftuples[i-1][0] == "new_line" and ftuples[i] != ftuples[0]:
                    line_layout.addSVG("svgs/blank_template.svg",alignment=ss.AlignLeft)

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
