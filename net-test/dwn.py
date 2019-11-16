""" Final Project
    Download Files Test
    Elijah Reyes """

import wget, time

print('                       This test will run once...')
print('Choose one of the options to download:')
print('(1) A 200MB file')
print('(2) A 512MB file')
print('(3) A 1GB file')

try:
    # python 2
    choice = str(raw_input('Enter your choice: '))
except:
    # python 3
    choice = str(input('Enter your choice: '))

# 3 links for testing. 200MB file a 512MB file and a 1GB file
link1 = 'http://ipv4.download.thinkbroadband.com/200MB.zip'
link2 = link1.replace('200MB', '1GB')
link3 = link1.replace('200', '512')

startTime = time.time()
if choice == '1':
    wget(link1)
elif choice == '2':
    wget(link3)
elif choice == '3':
    wget(link2)
else:
    print('there is no option {}'.format(choice))
    quit()

endTime = time.time() - startTime
endTime = round((endTime * 1000000), 3)
print('Download took {} microseconds'.format(str(endTime)))
