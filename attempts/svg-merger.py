def main():
    import svg_stack as ss
    doc = ss.Document()
    ftuples = [
            ("char","svgs/lower/lower_h/lower_h_1.svg"), 
            ("char","svgs/lower/lower_i/lower_i_1.svg"), 
            # ("space","blank_template.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_o/lower_o_1.svg"), 
            ("char","svgs/lower/lower_s/lower_s_1.svg"),
            ("char","svgs/lower/lower_s/lower_s_1.svg"), 
            # ("space","blank_template.svg"),
            ("char","svgs/lower/lower_m/lower_m_1.svg"),
            ("char","svgs/lower/lower_o/lower_o_1.svg"),
            ("char","svgs/lower/lower_o/lower_o_1.svg"),
            ("char","svgs/lower/lower_n/lower_n_1.svg"),
            # ("space","blank_template.svg"),
            ("char","svgs/lower/lower_s/lower_s_1.svg"),
            ("char","svgs/lower/lower_n/lower_n_1.svg"),
            ("char","svgs/lower/lower_o/lower_o_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            # ("space","blank_template.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ("char","svgs/lower/lower_b/lower_b_1.svg"),
            ]
        # 1. If there’s a new line type, how do we that?
        # 2. If there’s a space, how do we that?
        # 3. If it goes over the 400px limit, how do we go 
        #   to a new line without separating a word? 
        #   (Aka how do we move an entire word to the next line?)
    result_layout = ss.VBoxLayout()
    word = []
    for ftuple in ftuples:
        line_layout = ss.HBoxLayout()
        if ftuple[0] == "char":
            word.append(ftuple[1])
        elif ftuple[0] == "space" or ftuple == ftuples[-1]:
            word_layout = ss.HBoxLayout()
            for char in word:
                word_layout.addSVG(char,alignment=ss.AlignCenter) 
            word = []
            word_layout.addSVG(ftuple[1],alignment=ss.AlignCenter)
            line_layout.addLayout(word_layout)

            # doc.setLayout(line_layout)
            # doc.save('length_check.svg')
            # from svgpathtools import svg2paths 
            # total_length = 0
            # paths, attributes = svg2paths('length_check.svg')
            # for path in paths:
            #     total_length += path.length()
            # print(total_length)
        elif ftuple[0] == "new line":
            result_layout.addLayout(line_layout)
        result_layout.addLayout(line_layout)

    doc.setLayout(result_layout)
    doc.save('api_test.svg')
    
if __name__ == "__main__": main()
    # for ftuple in ftuples:
    #     layout2 = ss.HBoxLayout()
    #     index = ftuples.index(ftuple)
    #     start = 0
    #     if index % 2 == 0 and index != 0:
    #         for file in ftuples[start:index + 1]:
    #             layout2.addSVG(file[1],alignment=ss.AlignCenter)
    #         start = index + 1
    #     elif ftuple[0] == "space":
    #         layout2.addSVG("blank_template.svg")
    #     layout1.addLayout(layout2)