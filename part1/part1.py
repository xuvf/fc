"""This module should filter and sort uk phone numbers from the text file provided. """
import re
import sys


def main(file):
    raw_text = file.read()
    result = str()

    rule = re.compile(" ")
    raw_text = (rule.sub('',raw_text))
    rule = re.compile(r"\+44\d{10,}")
    uknumber = rule.findall(raw_text)
    uknumber.sort()
    
    for i in range(len(uknumber)):
        if (len(uknumber[i])<14):
            result += "0" + uknumber[i][3:7] + " " + uknumber[i][7:] + "\n"
    print(result)

if __name__ == "__main__" :
    try:
        f = open(sys.argv[1],"r")
    except IndexError:
        print("Usage: python part1.py <fileName>")
    except IOError:
        print("Failed to load the file")
    else:
        main(f)
        f.close
