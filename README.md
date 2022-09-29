# bachin-writer

## Follow these instructions to run the writer locally. 

Start by cloning this repository. (in a terminal, run `git clone https://github.com/martinvaughn/bachin-writer.git`)

Once you've downloaded the files, make your way in a terminal to the newly cloned bachin-writer directory. (using cd, you should be able to ls and see bachin-writer.py in the current directory)

Make sure you have python 3 downloaded. This can be done by running `python3 --version` or `python --version` in your terminal. 
If this returns an error or anything other than Python 3._._, then you'll need to download python 3 here: https://www.python.org/downloads/

Once downloaded, you should be able to run `python3 --version` and have it return something like Python 3.10.0

Next you'll download your python packages. Run the following commands in your terminal:

`pip3 install lxml`
`pip3 install six`
`pip3 install svg-stack`
`pip3 install svgwrite`


Now everything is ready!

The way to run your code is to type in the terminal this command, with the sentence you want to include in quotation marks:

`python3 bachin-writer.py "your sentence goes here"`

To add new lines to a sentence, do it like this: 
`python3 bachin-writer.py "first line ~second line ~~double new line"` 

Note: make sure there's a space directly before the new line character

To make a sentence of centered text, use the same command but change the filename to bachin-centered.py like this:

`python3 bachin-centered.py "centered sentence goes here"`


If you want to change the list of svgs that are used in the future, just make sure that the directory of the svgs is named `svgs`

Common Mistakes:
1. If you get an error that says something like `no module named svgwrite` then you just need to run `pip3 install svgwrite` in your terminal.
2. Make sure you're using python 3.0.0 or above!
3. The files `blank_template.svg`, `white_space.svg`, and all the svg folders are necessary to use the code. If you change file names, change the naming conventions (such as adding capitals when it should be lower case), or move around the folders, then the code will break. That doesn't mean you can't add or change characters, just stick to the naming conventions and don't change the file structure.
4. Make sure to run the code in the same directory as the python files. You should be able to run `ls` (Mac) or `pwd` (Windows) and see the bachin-writer.py and bachin-centered.py files
5. On windows (which I'm not as familiar with), it seems that your python instance can have different names such as "python", "py", "python3", etc. If using python3 isn't working in the above terminal commands, try using "python" or "py"




