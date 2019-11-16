""" Final Project
    Create 'n' files and delete
    Elijah Reyes
    CSCI 604 """

import time. os

try:
    n = sys.argv[1]
except:
    print('Please inlcude number of files. EX: 100-files.py 20')
    quit()

startWrite = time.time()

for k in range(1, n + 1):
    
    # create the file
    with open( 'file-{}.txt'.format(str(k)), 'w') as newFile:
        newFile.write('I am file {}'.format(str(k)))

endWrite = time.time() - startWrite
endWrite = round((endWrite * 1000000), 3)
print('{}us to create {} files.'.format(str(endWrite), str(n)))

startDelete = time.time()

for k in range(1, n + 1):
    
    # delete the file
    os.remove('file-{}.txt'.format(str(k)))

endDelete = time.time() - startDelete
endDelete = round((endDelete * 1000000), 3)
print('{}us to delete {} files.'.format(str(endDelete), str(n)))
