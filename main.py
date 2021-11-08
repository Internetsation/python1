# Project 7 regex
# This program imports the re and os modules
# *** I found that the os.uname incompatible with my machine so I have used the "platform" module instead ***
# The platform module provides info regarding the users os.
# The re module searches the data provided from the os module using regular expressions (regex)

import platform
import re

# Search patterns
pattern1 = re.compile("^windows", re.IGNORECASE)
pattern2 = re.compile('64')
pattern3 = re.compile('^Windows')
pattern4 = re.compile('\\w', re.ASCII)
pattern5 = re.compile('\d')
# Takes data from platform modules and converts to strings
# Returns a namedtuple() containing six attributes: system, node, release, version, machine, and processor.
test_string1 = ' '.join(platform.uname())
# Returns a string identifying the Python implementation. Possible values : ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.
test_string2 = ''.join(platform.python_implementation())
# Version information from Windows Registry OS release, version number, service pack and multi/single processor.
test_string3 = ' '.join(platform.win32_ver(release='', version='', csd='', ptype=''))
# Windows edition
test_string4 = ''.join(platform.win32_edition())
# Returns the (real) processor name
test_string5 = ''.join(platform.processor())
# Combine strings
allstrings = test_string1 + ',\n ' + test_string2 + ',\n ' + test_string3 + ',\n ' + test_string4 + ',\n ' + \
             test_string5


# Checks for patterns in allstrings
def rs():
    # looks for "Windows", prints if found
    result1 = re.findall(pattern1, allstrings)
    print("Result 1: \n", result1,"\n")

    # Identifies and prints instances of 64
    result2 = re.findall(pattern2, allstrings)
    print("Result 2: \n", result2,"\n")

    # Replaces "Windows" with "SuperSecretMacOS"
    real_os = 'SuperSecretMacOS'
    result3 = re.sub(pattern3, real_os, allstrings)
    print("Result 3: \n", result3,"\n")

    # Prints all non alphanumeric characters
    result4 = re.split(pattern4, allstrings)
    print("Result 4: \n", result4,"\n")

    # Prints only digits
    result5 = re.findall(pattern5, allstrings)
    print("Result 5: \n", result5,"\n")

    # prints the span of pattern1
    result6 = (pattern1.match(allstrings).span())
    print("Result 6: \n", result6,"\n")

if __name__ == '__main__':
    rs()
