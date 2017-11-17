#This program is lesson 23 in 'Learn Python The hard Way"
import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding='utf8')

main(languages, input_encoding, error)

'''
things that I've never seen before:
*.strip() : strips away trailing \n
*.encode() : use when get error from Python saying it doesn't know how to encode it
*.decode() : if you have raw bytes (b'\xe6\x96...') use .decode to get string
*DBES : DECODE BYTES ENCODE STRINGSat
'''
