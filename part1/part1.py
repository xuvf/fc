"""This module should filter and sort uk phone numbers from the text file provided. """
import re
import sys


def main(file):
    raw_text = file.read()
    result = []
    
    rule = re.compile(" ")
    raw_text = (rule.sub('',raw_text))
    rule = re.compile(r"\+44\d{10,}")
    uknumber = rule.findall(raw_text)
    for i in range(len(uknumber)):
        if (len(uknumber[i])<14):
            result.append(uknumber[i])        
    
    print(len(result))

if __name__ == "__main__" :
    try:
        f = open(sys.argv[1],"r")
    except IOError:
        print("Failed to load the file")
    else:
        main(f)
