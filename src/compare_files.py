"""
Compare if two files are the same.
Given two files input_1, input_2 this script compares if the two files are the same.
"""
import sys

# Files to be compared
input_1, input_2 = sys.argv[1:]


with open(input_1, 'rb') as inp_1:
    with open(input_2, 'rb') as inp_2:
        n_lines = 1
        inp_1_line = inp_1.readline()
        inp_2_line = inp_2.readline()

        while len(inp_1_line) > 0 or len(inp_2_line) > 0:
            if inp_1_line != inp_2_line:
                print('\033[91mFAIL\033[0m: Line', n_lines, 'of the output',input_2,'does not match the sample output',input_1)
                sys.exit(0)

            inp_1_line = inp_1.readline()
            inp_2_line = inp_2.readline()

        print('\n\x1b[6;30;42mPASS\x1b[0m: Returned output',input_2, 'matches the expected output',input_1,'\n')
