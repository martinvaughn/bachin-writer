def main():
    import svg_stack as ss

    doc = ss.Document()

    layout1 = ss.HBoxLayout()
    layout1.addSVG('red_ball.svg',alignment=ss.AlignBottom)
    layout1.addSVG('red_ball.svg',alignment=ss.AlignBottom)
    # layout1.addSVG('red_ball.svg',alignment=ss.AlignTop|ss.AlignHCenter)
    layout1.addSVG('blue_triangle.svg',alignment=ss.AlignCenter)

    layout2 = ss.VBoxLayout()

    layout2.addSVG('red_ball.svg',alignment=ss.AlignCenter)
    layout2.addSVG('red_ball.svg',alignment=ss.AlignCenter)
    # layout2.addSVG('red_ball.svg',alignment=ss.AlignCenter)
    layout1.addLayout(layout2)

    doc.setLayout(layout1)

    doc.save('og_test2.svg')

if __name__ == "__main__": main()