""" Final Project
    Calculate file compression
    Elijah Reyes
    CSCI 604 """

import sys, time, zipfile

try:
    jungle_zip = zipfile.ZipFile(sys.argv[1], 'w')
    _file = sys.argv[2]
except Exception as exc:
    print(exc)
    print('Syntax: file-compression.py /path/to/output.zip /path/to/file')
    quit()

startTime = time.time()
jungle_zip.write(_file, compress_type=zipfile.ZIP_DEFLATED)
endTime = time.time() - startTime
endTime = round((endTime * 1000000), 3)
print('File compressed in {}us'.format(str(endTime)))
