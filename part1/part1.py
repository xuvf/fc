"""This module should filter and sort uk phone numbers from the text file provided. """
import re
import sys


def main(file):
    '''
    Using Regular Expression to extract UK number and print them 
    '''

    # read file 
    raw_text = file.read() 
    # initialise a result string 
    result = str()

    # remove all blank space
    rule = re.compile(" ")
    raw_text = (rule.sub('',raw_text))

    # extract all uk number 
    rule = re.compile(r"\+44\d{10,}")
    uknumber = rule.findall(raw_text)

    # sort results
    uknumber.sort()

    # print all results with a special format 
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
