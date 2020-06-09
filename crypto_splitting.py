def split_file(path_in, path_out_1, path_out_2):

    f_in = open(path_in, "rb")
    input_text = f_in.read()
    print(input_text)
    output_1 = ''
    output_2 = ''

    i = 0
    for c in input_text:
        n1 = c & 0xAA # 0xAA = 10101010
        n2 = c & 0x55 # Ox55 = 01010101

        output_1 = output_1 + chr(n1)
        output_2 = output_2 + chr(n2)

    f_out1 = open(path_out_1, "wb")
    f_out1.write(output_1.encode('raw_unicode_escape'))
    f_out1.close()

    f_out2 = open(path_out_2, "wb")
    f_out2.write(output_2.encode('raw_unicode_escape'))
    f_out2.close()


def merge_files(path_in_1, path_in_2, path_out):
    f_in_1 = open(path_in_1, "rb")
    input_text_1 = (f_in_1.read()).decode('raw_unicode_escape')
    f_in_1.close()

    f_in_2 = open(path_in_2, "rb")
    input_text_2 = (f_in_2.read()).decode('raw_unicode_escape')
    f_in_2.close()

    output = ''

    for c2, c1 in zip(input_text_2,input_text_1):
        out_byte_int = ord(c1) + ord(c2)
        output = output + chr(out_byte_int)

    f_out = open(path_out, "wb")
    f_out.write(output.encode('raw_unicode_escape'))
    f_out.close()
