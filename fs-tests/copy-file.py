""" Final Project
    Copying <file> and calculating execution time
    Elijah Reyes
    CSCI 604 """

import sys, time, os

try:
    source = sys.argv[1]
    destination = sys.argv[2]
    operating_system = sys.argv[3]
except:
    print('Syntax: copy-file.py /path/to/source /path/to/destination <operating_system>')
    quit()

if operating_system.lower() != 'linux' and operating_system.lower() != 'windows':
    print('unknown os: {}'.format(operating_system))
    quit()

elif operating_system.lower() == 'linux':
    cmd = 'cp'

elif operating_system.lower() == 'windows':
    cmd = 'copy'

cmd = cmd + ' ' + source + ' ' + destination
startTime = time.time()
os.system(cmd)
endTime = time.time() - startTime
endTime = round((endTime * 1000000), 3)
print('File copied in {}us.'.format(str(endTime)))
