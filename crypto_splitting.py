""""
crypto_splitting.py - A simple file splitting module
Copyright (c) 2020 Mathieu Chollet (https://mchollet.eu)
"""


def split_file(path_in: str, path_out_1: str, path_out_2: str) -> None:
    """"Reads the file in path path_in and bit-split its into path_out_1 and path_out_2"""

    # Opening the source file and reads its content
    f_in = open(path_in, "rb")
    input_bytes = f_in.read()
    f_in.close()

    # Initialising the output buffers
    output_1_str = ''
    output_2_str = ''

    # Reading input one character at a time, splitting into two character
    # c1 gets odd-numbered bits 1, 3, 5, 7
    # c2 gets even-numbered bits 2, 4, 6, 8
    # Adding them to output_1 and output_2, respectively
    for c in input_bytes:
        c1 = c & 0xAA  # 0xAA = 10101010
        c2 = c & 0x55  # Ox55 = 01010101
        output_1_str = output_1_str + chr(c1)
        output_2_str = output_2_str + chr(c2)

    # Writing the first output file to disk
    f_out1 = open(path_out_1, "wb")
    f_out1.write(output_1_str.encode('raw_unicode_escape'))
    f_out1.close()

    # Writing the second output file to disk
    f_out2 = open(path_out_2, "wb")
    f_out2.write(output_2_str.encode('raw_unicode_escape'))
    f_out2.close()


def merge_files(path_in_1: str, path_in_2: str, path_out: str) -> None:
    """"Reads the files in paths path_in_1 and path_in_2, merges them to path_out"""

    # Opening the source files and reading their contents
    f_in_1 = open(path_in_1, "rb")
    input_1_str = (f_in_1.read()).decode('raw_unicode_escape')
    f_in_1.close()

    f_in_2 = open(path_in_2, "rb")
    input_2_str = (f_in_2.read()).decode('raw_unicode_escape')
    f_in_2.close()

    # Initialising the output buffer
    output_str = ''

    # Iterating through the inputs character by character, adding them, concatenating the new character to the buffer
    for c1, c2 in zip(input_1_str,input_2_str):
        out_byte_int = ord(c1) + ord(c2)
        output_str = output_str + chr(out_byte_int)

    # Writing the merged file to disk
    f_out = open(path_out, "wb")
    f_out.write(output_str.encode('raw_unicode_escape'))
    f_out.close()
