from re import I


def main():
    import svg_stack as ss
    import svgelements as svg
    doc = ss.Document()
    ftuples = [
            ("char","svgs/lower/lower_h/lower_h_1.svg",1), 
            ("char","svgs/lower/lower_i/lower_i_1.svg",2), 
            ("space","blank_template.svg",3),
            ("char","svgs/lower/lower_b/lower_b_1.svg",4),
            ("char","svgs/lower/lower_o/lower_o_1.svg",5), 
            ("char","svgs/lower/lower_s/lower_s_1.svg",6),
            ("char","svgs/lower/lower_s/lower_s_1.svg",7), 
            ("space","blank_template.svg",8),
            ("char","svgs/lower/lower_m/lower_m_1.svg",9),
            ("char","svgs/lower/lower_o/lower_o_1.svg",10),
            ("char","svgs/lower/lower_o/lower_o_1.svg",11),
            ("char","svgs/lower/lower_n/lower_n_1.svg",12),
            ("char","svgs/lower/lower_s/lower_s_1.svg",13),
            ("char","svgs/lower/lower_n/lower_n_1.svg",14),
            ("char","svgs/lower/lower_o/lower_o_1.svg",15),
            ("char","svgs/lower/lower_b/lower_b_1.svg",16),
            ("char","svgs/lower/lower_b/lower_b_1.svg",17),
            ("char","svgs/lower/lower_b/lower_b_1.svg",18),
            ("char","svgs/lower/lower_b/lower_b_1.svg",19),
            ("char","svgs/lower/lower_b/lower_b_1.svg",20),
            ("char","svgs/lower/lower_b/lower_b_1.svg",21),
            ("char","svgs/lower/lower_b/lower_b_1.svg",22),
            ("char","svgs/lower/lower_b/lower_b_1.svg",23),
            ("char","svgs/lower/lower_b/lower_b_1.svg",24),
            ("char","svgs/lower/lower_b/lower_b_1.svg",25),
            ("char","svgs/lower/lower_b/lower_b_1.svg",26),
            ("char","svgs/lower/lower_b/lower_b_1.svg",27),
            ("new line","blank_template.svg",28),
            ]
    result_layout = ss.VBoxLayout()
    i = 0
    while i < len(ftuples):
        j = 0
        line_layout = ss.HBoxLayout()
        while j < 5:
            line_layout.addSVG(ftuples[i][1])
        j += 1
    i += 1

    result_layout.addLayout(line_layout)  
    print(result_layout.get_size().width)     
    doc.setLayout(result_layout)
    doc.save('api_test.svg')
    
if __name__ == "__main__": main()
