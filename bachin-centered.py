import svg_stack as ss
import sys
import writer_utils as writer_utils
import svgwrite

def main():
    doc = ss.Document()
    if len(sys.argv) == 1:
        print("ERROR: Please provide an input string")
        return 
    input_str = sys.argv[1]
    ftuples = []
    for idx, char in enumerate(input_str):
        folder_tuple = writer_utils.get_folder(char, idx)
        ftuples.append(folder_tuple)
    result_layout = ss.VBoxLayout()
    yes = True
    while yes == True:
        i = 0
        word = []
        line_layout = ss.HBoxLayout()
        doc_width = 580
        while i < len(ftuples):
            if ftuples[i][0] == "new_line":
                if ftuples[i-1][0] == "new_line" and ftuples[i] != ftuples[0]:
                    line_layout.addSVG("svgs/blank_template.svg", alignment=ss.AlignLeft)
                white_space_length = (doc_width / 2) - (line_layout.get_size().width / 2)
                dwg = svgwrite.Drawing('svgs/white_space.svg', size=(white_space_length, "10"))
                dwg.save()
                white_space_layout = ss.HBoxLayout()
                white_space_layout.addSVG("svgs/white_space.svg", alignment=ss.AlignCenter)
                centered_layout = ss.HBoxLayout()
                centered_layout.addLayout(white_space_layout)
                centered_layout.addLayout(line_layout)
                result_layout.addLayout(centered_layout)
                line_layout = ss.HBoxLayout()                    
            
            if ftuples[i] == ftuples[-1]: 
                word_layout = ss.HBoxLayout()
                word.append(ftuples[i][1])
                for file in word:
                    word_layout.addSVG(file, alignment=ss.AlignLeft)
                line_layout.addLayout(word_layout)
                # if line_layout.get_size().width + word_layout.get_size().width > doc_width:
                white_space_length = (doc_width / 2) - (line_layout.get_size().width / 2)
                dwg = svgwrite.Drawing('svgs/white_space.svg', size=(white_space_length, "10"))
                dwg.save()
                white_space_layout = ss.HBoxLayout()
                white_space_layout.addSVG("svgs/white_space.svg", alignment=ss.AlignCenter)
                centered_layout = ss.HBoxLayout()
                centered_layout.addLayout(white_space_layout)
                centered_layout.addLayout(line_layout)
                result_layout.addLayout(centered_layout)
                line_layout = ss.HBoxLayout()
                yes = False
            elif ftuples[i][0] == 'space':
                word_layout = ss.HBoxLayout()
                word.append(ftuples[i][1])
                for file in word:
                    word_layout.addSVG(file, alignment=ss.AlignLeft)
                if line_layout.get_size().width + word_layout.get_size().width > doc_width:
                    white_space_length = (doc_width / 2) - (line_layout.get_size().width / 2)
                    dwg = svgwrite.Drawing('svgs/white_space.svg', size=(white_space_length, "5"))
                    dwg.save()
                    white_space_layout1 = ss.HBoxLayout()
                    white_space_layout1.addSVG("svgs/white_space.svg", alignment=ss.AlignCenter)
                    centered_layout1 = ss.HBoxLayout()
                    centered_layout1.addLayout(white_space_layout1)
                    centered_layout1.addLayout(line_layout)
                    result_layout.addLayout(centered_layout1)
                    line_layout = ss.HBoxLayout()
                line_layout.addLayout(word_layout)
                word = []
            elif ftuples[i][0] == "char":
                word.append(ftuples[i][1])
            i += 1
    result_layout.addLayout(line_layout)
    doc.setLayout(result_layout)
    doc.save('centered.svg')
    
if __name__ == "__main__":
    main()