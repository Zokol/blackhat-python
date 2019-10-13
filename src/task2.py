import sys
import re

sample = "$8:2>9#2%2$#>90$#%>90"


def is_printable(s):
    if len(set(s)) < 4:
        return False
    return bool(re.match('^[a-zA-Z0-9]+$', s))
    #return not any(repr(ch).startswith("'\\x") or repr(ch).startswith("'\\u") for ch in s)


def testXOR(s):
    for i in range(0, 255):
        s2 = ""
        for c in s:
            if isinstance(c, str):
                tmp = ord(c)
            elif isinstance(c, int):
                tmp = c
            s2 = s2 + chr(i ^ tmp)
        if (is_printable(s2)):
            print(str(i) + ": " + s2)

def list_words(word_length):
    print("Looking for words with length", word_length)
    with open(sys.argv[1], 'rb') as input_file:
        while True:
            buf = input_file.read(word_length)

            if not buf:
                break

            testXOR(buf)

    input_file.close()

if __name__ == '__main__':
    list_words(20)
