# Function parses log and returns 100 lines above and below matching identifier
# Assumption made - log is located in /var/log
# Missing functionality - user enters server ip address
# Possible improvements - command line arguments instead of 'raw_input'
# Function tested on 4.7M log - /var/log/corecaptured.log (typical log on MAC OS)
# Usage - when enter log name mask use corecaptured.*; Identity used - 'Oct 20'


import collections
import itertools
import sys
import os
import fnmatch


ROOT_PATH = '/var/log'


def get_log_name():
    name = raw_input('Enter log name mask: ')
    return str(name)


def get_identity():
    number = raw_input('Enter identification number: ')
    return number


def find_log(name):
    for root, dirs, files in os.walk(ROOT_PATH):
        for filename in fnmatch.filter(files, name):
            return os.path.join(root, filename)


if __name__ == '__main__':
    pattern = get_log_name()
    identity = get_identity()
    log = find_log(pattern)
    with open(log, 'r') as f:
        lines_before = collections.deque(maxlen=100)
        for line in f:
            if identity in line:
                sys.stdout.writelines(lines_before)
                sys.stdout.write(line)
                sys.stdout.writelines(itertools.islice(f, 100))
                break
            lines_before.append(line)

